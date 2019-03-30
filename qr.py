import qrcode


def render_qr(login, arg):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data("/info/{}/{}".format(login, arg))
    qr.make(fit=True)

    img = qr.make_image()
    # img.save("image.png")
    # img.save("image.bmp")
    # img.save("image.jpeg")
    img.save("static/qr_codes/qr_{}_{}.jpg".format(login, arg))


if __name__ == "__main__":
    render_qr("http://www.city-institute.org/index.php/uk/proekty/243-ngo-networking-stvorennia-merezhi-nuo-shcho-pratsiuiut-u-sferi-detsentralizatsii-u-zakhidnii-ukraini")
