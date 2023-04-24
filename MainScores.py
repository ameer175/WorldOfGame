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
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)