import time
import hmac
import hashlib
import base64

from flask import Flask, render_template

app = Flask(__name__)

app.config.from_pyfile("app.cfg")


def createKey(username, secret, expires):
    return base64.encodestring(hmac.HMAC(
        secret, str(expires) + ":" + username,
        hashlib.sha1).digest()).replace(' ', '+').strip()


@app.route("/auth")
def auth():
    expires = int(time.time() + 300)
    key = createKey(app.config['USERNAME'], app.config['SECRET'], expires)
    return 'var voxrtc_config = %s;' % str(
        {"key": key, "expires": expires,
         "username": app.config['USERNAME']})


@app.route("/demo")
def index():
    return render_template("index.html")

app.run(host='0.0.0.0', port=5001)
