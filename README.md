# QRCODE_PROCESS
# ko đặt tên biến là qrcode
# khởi tạo
qrcode_new = QR_CODE_PROCESS() \n

# encode qrcode
qrcode_new.encode_qrcode("Hello World","test_qrcode.png")

# decode qrcode
data = qrcode_new.decode_qrcode(image_url='test_qrcode.png', print_data= True)
