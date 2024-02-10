from flask import Flask
app = Flask(__name__)

@app.route("/<file_name>")
def home(file_name):
    file = open('./assets/file1.txt','r')
    return file.read()