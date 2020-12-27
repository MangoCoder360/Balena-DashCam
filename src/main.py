# web interface for checking status of device and controlling recording operations
# if you need to shutdown the device, use the balena dashboard

from flask import Flask
app = Flask(__name__)

def initCam():
    import dashcamMain
    print("Initializing dashcam...")

@app.route('/')
def init():
    return 'DashCam Web Interface'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
