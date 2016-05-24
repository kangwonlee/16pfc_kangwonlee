# -*-coding:utf8
# http://learnpythonthehardway.org/book/ex34.html
from sys import exit


def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if 50 > how_much:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if "take honey" == choice:
            dead("The bear looks at you then slaps your face off.")
        elif "taunt bear" == choice and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif "taunt bear" == choice and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif "open door" == choice and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


# 여기까지 입력 후 add, commit  # 각 행 주석 입력 후 commit

# 각자 Study drills 시도 후 필요시 commit  # 오류노트 에 각자 오류노트 작성
