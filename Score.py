from Utils import SCORES_FILE_NAME,BAD_RETURN_CODE

def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    def WriteScore(num):
        file = open(SCORES_FILE_NAME,"w")
        file.write(num)
        file.close()
    try:
        file = open(SCORES_FILE_NAME,"r")
        num = file.read()

        num = int(num) + POINTS_OF_WINNING
        WriteScore(str(num))
        file.close()
    except:
        file = open(SCORES_FILE_NAME,"w")
        file.write(str(POINTS_OF_WINNING))
        file.close()