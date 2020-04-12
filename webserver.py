from flask import Flask
from ec2_metadata import ec2_metadata

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to Smile Edu Portal!"

@app.route('/loadtest1')
def loadtest1():
    return "<H1>"+ec2_metadata.region+"</H1><P><H1>" + ec2_metadata.instance_id + "</H1>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
