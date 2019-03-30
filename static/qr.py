import qrcode


def render_qr(url, login):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image()
    # img.save("image.png")
    # img.save("image.bmp")
    # img.save("image.jpeg")
    img.save("qr_{}.jpg".format(login))


if __name__ == "__main__":
    render_qr("")
