from builtins import Exception
from flask import *
from Utils import SCORES_FILE_NAME
import os
app = Flask(__name__)

@app.route("/")
def score_server():
    #os.system('python MainGame.py')
    try:
        f = open(SCORES_FILE_NAME,"r")
        numScoure = f.read()
        numScoure = int(numScoure)
        f.close()
        return (
            f'<html><head><title>Scores Game</title></head><body><h1>The score is <div id="score">{numScoure}</div></h1></body></html>')
    except Exception as e:
        return(f'<html><head><title>Scores Game</title></head><body><h1>The Exception is:  <div id="score">{type(e)}</div></h1></body></html>')
    

host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
port = int(os.environ.get('FLASK_RUN_PORT', 5000))
debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

if __name__ == '__main__':
    app.run(host=host, debug=debug, port=port)