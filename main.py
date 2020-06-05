from flask import Flask
app = Flask(__name__)


#Route Examples:
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'


#Starting Flask Local Server: (below)
#export FLASK_APP=hello.py
#python -m flask run
#OR
#flask run --host=0.0.0.0   #this tells to listen and accept ALL IPs in current network