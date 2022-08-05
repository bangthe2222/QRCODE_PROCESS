import cv2
from pyzbar import pyzbar
import qrcode


class QR_CODE_PROCESS:
    def __init__(self):
        self.image = []
    def decode_qrcode(self,image_url = False, image_data = False , print_data = False):
        """***decode qrcode***\n
            image_url -> input is qrcode image url\n 
            image_data -> input is qrcode image
            set print_data = True -> print qrcode data
        """
        if image_url:
            self.image = cv2.imread(image_url)
        if image_data:
            self.image = image_data
        self.barcodes = pyzbar.decode(self.image)
        if print_data:
            i = 0
            for barcode in self.barcodes:
                print("qrcode", i)
                print("data: ",barcode.data.decode('utf-8'))
                print("rect:", barcode.rect)
                print()
                i+=1
        return self.barcodes
    def show_qrcode(self):
        """***show qrcode with data and bouding box***
        """
        for barcode in self.barcodes:
            if barcode.rect:
                (x,y,w,h) = barcode.rect
                cv2.rectangle(self.image, (x, y), (x+w, y+h),(0, 0, 255), 1)
                cv2.putText(self.image,barcode.data.decode('utf-8'),(x,y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,0), thickness=1, lineType= cv2.LINE_AA)
        cv2.imshow("image", self.image)
        cv2.waitKey(0)
    def encode_qrcode(self, data , out_image_url, fill_color = 'black', back_color = 'white', version = 2):
        """***encode qrcode***\n
            data -> data encode to qrcode\n
            out_image_url -> output image url\n
            version -> size of qrcode from 1 -> 40
        """
        qr = qrcode.QRCode(version = version,
                        box_size = 10,
                        border = 2)
        
        # Adding data to the instance 'qr'
        qr.add_data(data)
        
        qr.make(fit = True)
        img = qr.make_image(fill_color = fill_color,
                            back_color = back_color )
        
        img.save(out_image_url)

if __name__ == '__main__':
    # ko đặt tên biến là qrcode
    # khởi tạo
    qrcode_new = QR_CODE_PROCESS()

    # encode qrcode
    qrcode_new.encode_qrcode("Hello World","test_qrcode.png")

    # decode qrcode
    data = qrcode_new.decode_qrcode(image_url='test_qrcode.png', print_data= True)
