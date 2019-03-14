#!flask/bin/python
from flask import Flask
from flask import request
from flask import Flask, jsonify
import argparse
import socket


def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip=s.getsockname()[0]
    s.close()
    return ip

counter=0
app = Flask(__name__)

@app.route('/')
def index():
    return "Server is running",200

@app.route('/get_info', methods=['GET'])
def get_info():
    if request.method == 'GET':
        global counter
        counter+=1
        data={}
        data["counter"]=counter
        data["ip"]=getIP()
        return str(data), 200
    else:
        return "Port method is not valid for this request", 500

def parseArguments():
    parser = argparse.ArgumentParser(description='Test app')
    parser.add_argument('-p', '--port', type=int, help='Server port', required=False, default=5005)
    return parser.parse_args()

if __name__ == '__main__':
    opts=parseArguments()
    app.run(host="0.0.0.0",debug=True, port = opts.port)