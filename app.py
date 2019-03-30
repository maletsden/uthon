from flask import Flask, render_template, request  # , redirect
import sqlite3
from qr import render_qr
import cv2
# from camera import VideoCamera, Response

app = Flask(__name__, static_url_path='/static')
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def index():
    """
    The login page
    """
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    """
    the register page
    """
    try:
        username = request.form.get("login")
        password = request.form.get("pasw")
        if not username or not password:
            return render_template('fail.html')
        with sqlite3.connect('Hizer.db') as data_base:
            cursor = data_base.cursor()

            check_user = "SELECT ? FROM hizer WHERE ? IN (SELECT username FROM hizer)"

            cursor.execute(check_user, [(username), (username)])
            result = cursor.fetchall()

        if result != []:
            return render_template('register_fail.html')

        phone = request.form.get("phone")
        mail = request.form.get("email")
        telegram = request.form.get("telegram")
        instagram = request.form.get("instagram")
        twitter = request.form.get("twitter")
        facebook = request.form.get("facebook")

        res = []
        for media in [username, password, facebook, instagram, telegram, mail,
                      phone, twitter]:
            if media == '':
                media = 'NULL'
            res.append((media))

        with sqlite3.connect('Hizer.db') as data_base:
            cursor = data_base.cursor()

            finding_user = """INSERT INTO hizer (username, password, Facebook, Instagram, Telegram,
                    Email, Phone_number, Twitter) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""

            cursor.execute(finding_user, res)
            data_base.commit()
    except Exception:
        pass
    return render_template("index.html")


@app.route("/sign_up", methods=["POST"])
def sign_up():
    """
    the register page
    """
    return render_template("register.html")


# @app.route("/login", methods=["POST"])
# def profile():
#     """
#     What the authorized user see and can manage
#     """
#     if not request.form.get("pasw") or not request.form.get("login"):
#         return render_template("fail.html")
#     login = request.form.get("login")
#     pasw = request.form.get("pasw")
#     # SQL...
#     return render_template(profile_html_former(login))


# @app.route("/info", methods=["POST"])
# def friend_post_request():
#     """
#     what the friend, who want get the credentials of the specific user through
#     the QR code, will see
#     """
#     return render_template("info.html")


@app.route('/check_username', methods=["POST"])
def check_username():
    username = request.args.get("username")
    with sqlite3.connect('Hizer.db') as data_base:
        cursor = data_base.cursor()

        check_user = "SELECT username FROM hizer WHERE username = ?"

        cursor.execute(check_user, [(username)])
        result = cursor.fetchall()

    return '1' if result == [] else '0'


@app.route('/profile', methods=["POST"])
def profile():
    login = request.args.get('login', type=str)
    return render_template("share.html")


@app.route('/qr', methods=["GET", "POST"])
def qr():
    login = request.args.get('login', type=str)
    arg = request.args.get('arg', type=str)
    # refresh or add QR image to qr_coders directory
    render_qr(login, arg)
    # Remove any args that are None
    return render_template("qr.html",
                           sorce="/static/qr_codes/qr_{}_{}.jpg"
                           .format(login, arg))


# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
#
#
# @app.route('/scan_qr')
# def video_feed():
#     return Response(gen(VideoCamera()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


# @app.route('/info', methods=["POST", "GET"])
# def info():
#     username = request.args.get("login")
#     with sqlite3.connect('Hizer.db') as data_base:
#         cursor = data_base.cursor()
#
#         check_user = "SELECT * FROM hizer WHERE username = ?"
#
#         cursor.execute(check_user, [(username)])
#         result = cursor.fetchall()
#     print(result)
#
#     # return '1' if result == [] else '0'
#     # return render_template("show_contacts.html", )
#     return '1'


@app.route('/info', methods=["POST", "GET"])
def info():
    login = request.args.get('login', type=str)
    arg = request.args.get('arg', type=str)
    # get info about account
    with sqlite3.connect('Hizer.db') as data_base:
        cursor = data_base.cursor()

        check_user = "SELECT * FROM hizer WHERE username = ?"

        cursor.execute(check_user, [(login)])
        data_base_response = cursor.fetchall()[0]

    db_indexes = [6, 0, 5, 2, 4, 7, 3]
    lables = ["phone", "username", "email", "facebook", "telegram", "twitter", "instagram"]

    accounts = dict()
    for i in range(7):
        accounts[lables[i]] = data_base_response[db_indexes[i]] if arg[i] == "1" else False

    print(accounts)


    return render_template("show_contacts.html", accounts=accounts)
    # accounts=accounts)


if __name__ == '__main__':

    # create the data base
    # connection = sqlite3.connect('Hizer.db')
    # c = connection.cursor()
    #
    # c.execute("""CREATE TABLE hizer (
    #             username text,
    #             password text,
    #             Facebook text,
    #             Instagram text,
    #             Telegram text,
    #             Email text,
    #             Phone_number text,
    #             Twitter text
    #             )""")
    #
    # connection.commit()
    # connection.close()

    app.run()
