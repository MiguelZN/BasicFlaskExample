from flask import Flask
app = Flask(__name__)


#Route Examples:
@app.route('/')
def index():
    return 'Index Page3'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/claudia')
def claudia():
    return 'happy hoyan'




#Starting Flask Local Server: (below)--------------
#export FLASK_APP=hello.py    #set FLASK_APP variable to your main python flask app path file
#python3 -m flask run
#OR
#flask run --host=0.0.0.0   #this tells to listen and accept ALL IPs in current network

#-----------
#This runs a server on url:
# http://127.0.0.1:5000/


#-------------
#If you want to have the Flask app to constantly update any saved code:
#export FLASK_ENV=development

#Then rerun