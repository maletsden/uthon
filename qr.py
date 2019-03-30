import qrcode

def render_qr(login, arg):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data("http://10.10.226.64:5000/info?login={}&arg={}".format(login, arg))
    qr.make(fit=True)

    img = qr.make_image()
    img.save("static/qr_codes/qr_{}_{}.jpg".format(login, arg))
