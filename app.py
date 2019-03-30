from flask import Flask, render_template, request  # , redirect
import sqlite3


def profile_html_former(user):
    """
    Program that returns the HTML with user interface to configure QR

    :param user: str
    :return: ? (HTML)
    """
    return "login.html"


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
    username = request.form.get("login")
    password = request.form.get("pasw")
    if not username or not password:
        return render_template('register_fail.html')
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
    return render_template("index.html")


@app.route("/sign_up", methods=["POST"])
def sign_up():
    """
    the register page
    """
    return render_template("register.html")


@app.route("/login", methods=["POST"])
def profile():
    """
    What the authorized user see and can manage
    """
    if not request.form.get("pasw") or not request.form.get("login"):
        return render_template("fail.html")
    login = request.form.get("login")
    pasw = request.form.get("pasw")
    # SQL...
    return render_template(profile_html_former(login))


@app.route("/info", methods=["POST"])
def friend_post_request():
    """
    what the friend, who want get the credentials of the specific user through
    the QR code, will see
    """
    return render_template("info.html")

#
# @app.route('/profile/<command>')
# def profile():
#     return render_template("profile.html")


@app.route('/profile/<command>/<arg>')
def profile_sq(command, arg):
    # Remove any args that are None
    return render_template("fail.html")



if __name__ == '__main__':
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
