# Configuration
import time
import random


# Repetitive Functions
def print_pause(message):
    print(message)
    time.sleep(1.5)


def answer(opition1, opition2, function1, function2):
    print_pause('\nWhat do you want to do?')
    while True:
        answer = input('\nEnter (1) if you want to ' + opition1 + '\nOR\
 \nEnter (2) if you want to ' + opition2 + '\n')
        if answer == "1":
            time.sleep(2)
            function1()
            break
        elif answer == "2":
            time.sleep(2)
            function2()
            break
        else:
            print('Invalid Entry')


# Playing Function
def start_game():
    print_pause('\nWelcome To The Adventure Game')
    print_pause('\nHope You Will Get Some Fun Playing')
    print_pause('\nAre You Ready To Play?')
    answer('Play', 'Play Later', first_step, good_bye)


def first_step():
    print_pause('\nOK let us start the Game\n\n')
    print_pause('\nYou waked up in the morning and become surprised that there\
 is no one in the house.')
    print_pause('\nYour brothers and sisters')
    print_pause('\nYour mother and father')
    print_pause('\nEverone is gone')
    print_pause('\nNO ONE IN THE HOUSE')
    answer('search for your family inside the house', 'go outside\
 and look for your family', inside_search, ouside_search)


def inside_search():
    print_pause('\nYou are walking into the basement very slowly')
    print_pause('\nEverything is there except your family')
    print_pause('\nYou tried walk into the garage')
    print_pause('\nBut still there is no one there')
    answer('go back to your room', 'go outside and look for your\
 family', back_to_room, ouside_search)


def back_to_room():
    print_pause('You are goign back to your room and there is no one there')
    print_pause('\nWhat do you want to do?')
    answer('go and search inside the house again', 'go outside and look\
 for your family', inside_search, ouside_search)


def ouside_search():
    print_pause('\nYou are going outside but you heard a sound\
     coming from the inside of the house')
    print_pause('\nIt seems that there is something going inside')
    print_pause('\nIs it you family?')
    print_pause('\nIs it someone else?')
    answer('go Back to the house to check the sound', 'continue searching\
 for them outside', sound_search, continue_search_oustide)


def sound_search():
    animal = random.choice(['Cat', 'Dog'])
    print_pause('\nYou are entering the house again from the backyard door')
    print_pause('\nYou are reaching the kitchen')
    print_pause('\nTrying to hear the sound again')
    print_pause('\nOoops it nothing but the ' + animal + ' is messing with\
 the staff')
    print_pause('\nOMG you just lost your mind because of the sound and it\
 was the cat!!!!')
    answer('go back to the house and search for your\
 family', 'go outside and continue\
 searching for your family', inside_search, continue_search_oustide)


def continue_search_oustide():
    car_color = random.choice(['RED', 'BLACK', 'BLUE', 'YELLOW'])
    print_pause('\nYou are walking around the house')
    print_pause('\nYou are looking into the front yard and you find nothing ')
    print_pause('\nYou try go to the backyard where the big storage room is')
    print_pause('\nOn your way to the backyard you find a\
 strange ' + car_color + ' car parking near the house')
    answer('continue your way to the storage room', 'go to check\
 the strange car', go_to_storage, check_car)


def check_car():
    neighbor = random.choice(['Abdullah', 'Jon', 'Michel'])
    print_pause('\nYou are walking your way to the car ')
    print_pause('\nYour neighbor ' + neighbor + ' come out')
    print_pause('\nYou looked at him being surprised by the strange car ')
    print_pause('\nHe just said: This is my brother car he could not\
 find a place to park except here')
    answer('go back to the home', 'continue going to the\
 storage room', back_home, go_to_storage)


def back_home():
    print_pause('\nYou are in your way back home')
    print_pause('\nWalking')
    print_pause('\nWalking')
    print_pause('\nWalking')
    print_pause('\nOMG you just failed into a big hole & You\
 can not get out of it')
    game_over()


def go_to_storage():
    print_pause('\nYou are going back your way to the storage room')
    print_pause('\nYou are in the front of the door hearing sounds\
 from inside')
    print_pause('\nYou just opened the door and there was a\
 monster that is holding your family')
    answer('fight with the monster', 'run back to the home', fight, run_back)


def run_back():
    print_pause('\nYou are trying to run back to the home')
    print_pause('\nBUT Guess What')
    print_pause('\nThe monster catches you and held you along\
 with your family')
    print_pause('\nYou Have to wait for someoen to come and\
 rescue you and your family')
    game_over()


def fight():
    weapon = random.choice(['Sword', 'Knife', 'Rock'])
    print_pause('\nYou fight hard with the monster')
    print_pause('\nYou took his ' + weapon)
    print_pause('\nAnd')
    print_pause('\nYou Killed him')
    print_pause('\nYou saved your family and get them back to home')
    print_pause('\nYou’re a WINNER')
    restart_or_exist()


def restart_or_exist():
    answer('restart the game', 'exist the game', start_game, good_bye)


def game_over():
    print_pause('\nGAME OVER, You Could Not Find Or Rescue Your Family ... ')
    restart_or_exist()


def good_bye():
    print_pause('\nOk That Is Fine. Please be back Once\
 You Want To Have Some Fun \nSee You Soon!!!')


start_game()
