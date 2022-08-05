## QRCODE_PROCESS

# khởi tạo
qrcode_new = QR_CODE_PROCESS() 

# encode qrcode
qrcode_new.encode_qrcode("Hello World","test_qrcode.png")

# decode qrcode
data = qrcode_new.decode_qrcode(image_url='test_qrcode.png', print_data= True)
