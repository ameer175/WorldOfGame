from flask import *
from Utils import SCORES_FILE_NAME
import os
app = Flask(__name__)

@app.route("/")
def hello():
    os.system('python MainGame.py')
    f = open(SCORES_FILE_NAME,"r")
    numScoure = f.read()
    numScoure = int(numScoure)
    f.close()

    return(f'<html><head><title>Scores Game</title></head><body><h1>The score is <div id="score">{numScoure}</div></h1></body></html>')

if __name__ == "__main__":
    app.run(debug=True, port=9000)