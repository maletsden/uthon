# lb_17 /titter_friend_locator_server
from flask import Flask, render_template, request  # , redirect


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
    login = request.form.get("login")
    pasw = request.form.get("pasw")
    if not login or not pasw:
        return render_template('register_fail.html')
    phonenum = request.form.get("phonenum")
    e_mail = request.form.get("E-mail")
    Telegram = request.form.get("Telegram")
    # SQL...
    return render_template("index.html")


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


@app.route("/info", methods=["GET"])
def friend_post_request():
    """
    what the friend, who want get the credentials of the specific user through
    the QR code, will see
    """
    return render_template("info.html")


if __name__ == '__main__':
    app.run()
