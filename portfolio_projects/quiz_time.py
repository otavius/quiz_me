"""
A game based on knowledge
    - 3 levels
    - score board 
    - each level pass the next level will get harder 


"""



class Player:
    def __init__(self, name):
        self.name = name 
        self.score = 0
        
    def score_board(self, points):
        self.score += points

    def __str__(self):
        return "{}".format(self.name)

def answers():
    what_is_your_answer = input("Enter your input: ")
    # answer = "a, b, c"
    if what_is_your_answer == "a":
        print("correct")
    elif what_is_your_answer == "b":
        print("correct")
    elif what_is_your_answer == "c":
        print("correct")
    
    if what_is_your_answer != "a, b, c":
        print("Invalid input")



while True:
    name = input("Enter your name: ")
    player_1 = Player(name)
    current_score = player_1.score
    print("Welcome to Quiz", player_1)
    print("This will be a simple but exciting game")
    answer = input("Are you ready to play (y/n): \n")

    if answer == "y":
        print("The rules of the game are simple")
        print("There is 3 rounds and each question is worth 10 points \n")
    
    elif answer == "n":
        print("What a shame. I guess Game Over ")
        break
    while True:
        print("What year did the French Revolution start?: ")
        print("a) 1789")
        print("b) 1765")
        print("c) 1756")
        answer = input("Enter your answer: ")
        if answer == "a":
            print("correct")
            current_score += 10 
            print("your current score is ", current_score)
            break
        elif answer == "b" or answer == "c":
            print("Better luck next time \n")
            break
        elif answer != "a, b, c":
            print("Must be valid input")
    
    while True:
        print("Who was the first Emperor of Rome?")
        print("a) Nero")
        print("b) Otho")
        print("c) Augustus")
        answer = input("Enter your answer: ")

        if answer == "c":
            print("correct")
            current_score += 10 
            print("your current score is", current_score)
            break
        elif answer == "a" or answer == "b":
            print("Dude really....")
            break
        elif answer != 'a, b, c':
            print("Must be a Valid input")

    while True:
        print("What was the name of the ancient trade route that connected the East with the West")
        print("a) Spice Route")
        print("b) The Silk Road")
        print("c) The Salt Route")

        answer = input("Enter your answer: ")

        if answer == "b":
            print("correct")
            current_score += 10
            print("your current score is", current_score)
            break
        elif answer == "a" or answer == "c":
            print("There once was a boy who cried wolf....sadly you are him")
            break
        elif answer != 'a, b, c':
            print("Must be a valid input")

    
    if current_score == 30:
        print("Look at you. \n")
    elif current_score < 30:
        print("you can still win...hopefully :)")

    break

while True:
    print("Level 2 is all about the music \n")
    
    ready = input("Are you ready to continue?(y/n): ")

    if ready == "y": 
        print("Lets go sing a song or something! \n")
    elif ready == "n":
        print("well.....lets continue then \n")

    while True:
        print("The Wu Tang Clan recommends protecting which body part?")
        print("a) your neck")
        print("b) your back")
        print("c) your arm")

        answer = input("Enter your answer: ")
        if answer == "a":
            print("correct")
            current_score += 10 
            print("your current score is", current_score)
            break
        elif answer == "b" or answer == "c":
            print("watch your step kid(protect ya neck, kid) \n")
            break
        elif answer != "a, b, c,":
            print("Must be a valid input")

    while True:
        print("How many members are there in Korean boy band - BTS?")
        print("a) 10 ")
        print("b) 6 ")
        print("c) 7 ")

        answer = input("Enter your answer: ")
        if answer == "c":
            print("correct")
            current_score += 10
            print("your current score is", current_score)
            break
        elif answer == "a" or answer == "b":
            print("7 is a lucky number")
            break
        elif answer != 'a, b, c':
            print("must be a valid input")

    while True:
        print("Who is the best-selling female artist of all time? ")
        print("a) Madonna")
        print("b) Beyonce")
        print("c) Taylor Swift")

        answer = input("Enter your answer: ")
        if answer == "a":
            print("correct")
            current_score += 10
            print("your current score is", current_score)
            break
        elif   answer == "b" or answer == "c": 
            print("yeah i didn't know either ")
            break
        elif answer != 'a, b, c':
            print("Must be a valid input")

    if current_score == 60:
        print("WOW! \n")
    elif current_score <= 60: 
        while True:
            print("Do you want to answer a bonus question for 50 points?")
            user_input = input("Enter y/n: ")
            print("By the way its a another history question ")
        
            if user_input == 'y':
                print("From 1919 to 1933, the Weimar Republic was the government of what of nation?")
                print("a) England")
                print("b) Germany")
                print("c) Estonia")

                answer = input("Enter your answer: ")

                if answer == "b":
                    print("wow...you are correct")
                    current_score += 50
                    print("your current score is now", current_score)
                    break
                elif answer == "a" or answer == "c":
                    print("mmm sorry ")
                    break

    break 

while True:
    print("Nice made to the third level! \n")
    print("This is just going to be random... sorry")

    while True:
        print("The first McDonald's restaurant was opened in what state? The very first Mcdonald's")
        print("a) Washington")
        print("b) Nevada")
        print("c) California")

        answer = input("Enter your answer: ")

        if answer == "c":
            print("correct")
            current_score += 10
            print("current score is", current_score)
            break
        elif answer =="a" or answer == "b":
            print("you are something special in a good way ")
            break
        elif answer != "a, b, c":
            print("Must be a valid input")

    while True:
        print("last question \n")
        print("What color, aside form their black trim, were the original Converse All-Start Chuck Taylor basketball shoes when they were first produced in 1917?")
        print("a) Brown")
        print("b) White")
        print("c) Red")

        answer = input("Enter your answer: ")
        if answer == "a":
            print("corrrect")
            current_score += 10
            print("your final score is", current_score)
            break
        elif answer =="b" or "c":
            print("well that's it")
            break
        elif answer != 'a, b, c':
            print("Must be a valid input")

    print("Thanks for playing ")
    break

