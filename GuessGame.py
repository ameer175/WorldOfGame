import random
def generate_number(Difficulty):
     return random.randint(1,Difficulty)
########################################
def get_guess_from_user(Difficulty):
    return random.randint(1,Difficulty)
#####################################3###
def compare_results(Secret_number,Difficulty):
    x = get_guess_from_user(Difficulty)
    return Secret_number == x
############################################
def play(Difficulty):
    Secret_number = generate_number(Difficulty)
    return compare_results(Secret_number,Difficulty)

