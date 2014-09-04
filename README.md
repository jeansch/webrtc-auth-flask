webrtc-auth-flask
=================

This projects aims to provide an easy way for Voxbone customer to integrate WebRTC ephemeral authentication on their website.

This project is also shipped with a demo.
In order to configure the demo, edit the app.cfg file (you can use app.cfg.example as template):


```
#voxbone webrtc username
USERNAME = "username"
#voxbone webrtc secret
SECRET = "secret"
```

Where username is your Voxbone username and secret is the WebRTC secret password you defined for your voxbone account.


Once the above is done, you can simply run the following command line from project root folder:
Note that your python environment must have Flask installed.
```
python run.py
```
You should then be able to access the demo at the following url: http://localhost:5001/demo
