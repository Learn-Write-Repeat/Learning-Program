import tkinter
import webbrowser
import random
import speech_recognition as sr
print('Greetings to you Boss \nI\'m your GETO \nwhat you want me to do?:\n\n-Games \n-Entertainment \n-Translate \n-Others');
i =(input('\nEnter the option you want: '))
if (i.upper()=="GAMES"):
    root = tkinter.Tk()
    root.title("GAME: ROCK - PAPER -SCISSORS by tp-21-june-py-4")
    root.geometry("400x500")
    random_number = random.randint(1, 3)
    if random_number == 1:
        GETO_choice = "R"
    elif random_number == 2:
        GETO_choice = "P"
    elif random_number == 3:
        GETO_choice = "S"

    rock_image = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)"""
    paper_image = """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)"""
    scissors_image = """
        _______
    ---'   ____)____
              ______)   
           __________)   
          (____)
    ---.__(___)"""

    def rock():
        label_my_choice['text'] = rock_image

        if GETO_choice == "R":
            label_result['text'] = "TIE"
            label_GETO_choice['text'] = rock_image
        elif GETO_choice == "P":
            label_result['text'] = "GETO wins!"
            label_GETO_choice['text'] = paper_image
        elif GETO_choice == "S":
            label_result['text'] = "Congratulations, you win!"
            label_GETO_choice['text'] = scissors_image
    def paper():
        label_my_choice['text'] = paper_image

        if GETO_choice == "P":
            label_result['text'] = "TIE"
            label_GETO_choice['text'] = paper_image
        elif GETO_choice == "S":
            label_result['text'] = "GETO wins!"
            label_GETO_choice['text'] = scissors_image
        elif GETO_choice == "R":
            label_result['text'] = "Congratulations, you win!"
            label_GETO_choice['text'] = rock_image
    def scissors():
        label_my_choice['text'] = scissors_image
        if GETO_choice == "S":
            label_result['text'] = "TIE"
            label_GETO_choice['text'] = scissors_image
        elif GETO_choice == "R":
            label_result['text'] = "GETO wins!"
            label_GETO_choice['text'] = rock_image
        elif GETO_choice == "P":
            label_result['text'] = "Congratulations, you win!"
            label_GETO_choice['text'] = paper_image
    def reset():
        global GETO_choice
        random_number = random.randint(1, 3)
        if random_number == 1:
            GETO_choice = "R"
        elif random_number == 2:
            GETO_choice = "P"
        elif random_number == 3:
            GETO_choice = "S"
        label_GETO_choice['text'] = " "
        label_result['text'] = "Waiting for your input..."

    button_rock = tkinter.Button(root, text="Rock", command=rock)
    button_rock.pack()
    button_paper = tkinter.Button(root, text="Paper", command=paper)
    button_paper.pack()
    button_scissors = tkinter.Button(root, text="Scissors", command=scissors)
    button_scissors.pack()
    label_GETO_choice = tkinter.Label(root, justify=tkinter.LEFT, font="Courier", text="")
    label_GETO_choice.pack()
    label_my_choice = tkinter.Label(root, justify=tkinter.LEFT, font="Courier", text="")
    label_my_choice.pack()
    label_result = tkinter.Label(root, text="Waiting for your input...")
    label_result.pack()
    button_reset = tkinter.Button(root, text="Play Again", command=reset)
    button_reset.pack()
    root.mainloop()
elif (i.upper() == "ENTERTAINMENT"):
    print(
        "Hurray..!! it's chilling time...\nClick |1| to open Netflix \nClick |2| to open AmazonPrimeVideo \nClick |3| to open Hotstar \nClcik |4| to open YouTube \nClick |5| to open Spotify \nClick |6| to open Gaana '")
    Click = int(input('So,what you want me to open:'))
    while Click > 6 or Click < 0:
        Click = int(input(
            'Invalid Click, Please try entering based on the following instructions: \nClick |1| to open Netflix \nClick |2| to open AmazonPrimeVideo \nClick |3| to open Hotstar \nClcik |4| to open YouTube \nClick |5| to open Spotify \nClick |6| to open Gaana '))
    if (Click == 1):
        url = 'https://' + 'www.netflix.com'
        webbrowser.open(url)
    elif (Click == 2):
        url = 'https://' + 'www.primevideo.com'
        webbrowser.open(url)
    elif (Click == 3):
        url = 'https://' + 'www.hotstar.com'
        webbrowser.open(url)
    elif (Click == 4):
        url = 'https://' + 'www.youtube.com'
        webbrowser.open(url)
    elif (Click == 5):
        url = 'https://' + 'www.spotify.com'
        webbrowser.open(url)
    else:
        url = 'https://' + 'www.gaana.com'
        webbrowser.open(url)
elif (i.upper() == "TRANSLATE"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hello Boss..!!, Start speaking now...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("Did you say? {}".format(text))
        except:
            print("Coudn't recognize your voice, Try again")
elif (i.upper() == "OTHERS"):
    print("Hello Boss,\nOther consists of: \n-Social Media \n-NEWS")
    O = input("What you want to open in others:")
    if (O.upper() == "SOCIALMEDIA"):
        print(
            "---Social Media and communication---\nClick |1| to open FaceBook \nClick |2| to open Twitter \nClick |3| to open Instagram \nClcik |4| to open LinkedIn")
        Click = int(input('So,what you want me to open:'))
        while Click > 4 or Click < 1:
            Click = int(input(
                'Invalid Click, Please try entering based on the following instructions:\nClick |1| to open FaceBook \nClick |2| to open Twitter \nClick |3| to open Instagram \nClcik |4| to open LinkedIn '))
        if (Click == 1):
            url = 'https://' + 'www.facebook.com'
            webbrowser.open(url)
        elif (Click == 2):
            url = 'https://' + 'www.twitter.com'
            webbrowser.open(url)
        elif (Click == 3):
            url = 'https://' + 'www.instagram.com'
            webbrowser.open(url)
        else:
            url = 'https://' + 'www.linkedin.com'
            webbrowser.open(url)
    elif (O.upper() == "NEWS"):
        print(
            "---Popular NEWS Sites---\nClick |1| to open Times of India \nClick |2| to open The Hindu \nClick |3| to open Inshorts")
        Click = int(input('So,what you want me to open:'))
        while Click > 3 or Click < 1:
            Click = int(input(
                'Sorry Boss the entered option is invalid, Please try entering:\nClick |1| to open Times of India \nClick |2| to open The Hindu \nClick |3| to open Inshorts\n'))
        if (Click == 1):
            url = 'https://' + 'www.timesofindia.com'
            webbrowser.open(url)
        elif (Click == 2):
            url = 'https://' + 'www.thehindu.com'
            webbrowser.open(url)
        else:
            url = 'https://' + 'www.Inshorts.com'
            webbrowser.open(url)
else:
    print("\n------- ERROR 404 -------- \nRun Again and Try \n\n-Games \n-Entertainment \n-Translate \n-Others")
