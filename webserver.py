from flask import Flask
import pycurl
from io import BytesIO
from ec2_metadata import ec2_metadata

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to Smile Edu Portal!"

@app.route('/loadtest')
def loadtest():
    b_obj = BytesIO() 
    crl = pycurl.Curl()
    crl.setopt(crl.URL, 'https://wiki.python.org/moin/BeginnersGuide')
    crl.perform()
    crl.close()
    get_body = b_obj.getvalue()
    return get_body.decode('utf8')

@app.route('/loadtest1')
def loadtest1():
    return "<H1>"+ec2_metadata.region+"</H1><P><H1>" + ec2_metadata.instance_id + "</H1>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
