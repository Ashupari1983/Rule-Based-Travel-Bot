import re, random
from colorama import Fore, init

init(autoreset = True) 

destinations = {

"beaches": ["Bali", "Maldives", "Phuket"],

"mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],

"cities": ["Tokyo", "Paris", "New York"]

}

jokes = [

"Why don't programmers like nature? Too many bugs!",

"Why did the computer go to the doctor? Because it had a virus!",

"Why do travelers always feel warm? Because of all their hot spots!"

]

def normalize(text):
    return re.sub(r'\s+'," ", text.strip().lower())

def showhelp():
    print("I can do the following things:")
    print("Reccomend destinantions. (type reccomend)")
    print("Give packing tips. (type tips)")
    print("Tell a joke. (type joke)")
    print("Type exit or bye to leave.")

def reccomend():
    print("Enter your preference. (Beaches, Mountains, Cities)")
    preference = input("You: ")
    preference = normalize(preference)

    if preference not in destinations:
        print("I cannot reccomend destinations of this type.")
    else:
        print("Suggestion: ", random.choice(destinations[preference]))
        ans = input("Do you like it? ")
        if normalize(ans) == "yes":
            print("Great! enjoy your travles.")
        else:
            reccomend()

def tips():
    place = input("Which place?")
    days = input("How many days?")
    print("\n Packing tips:")
    print("\n1. Pack versatile clothing.")
    print("2. Check the weather forecast.")
    print("3. Pack charging cables and adapters.")

def joke():
    print(random.choice(jokes))

def chat():
    print(f"{Fore.BLUE} Welcome to TravelBot!!")
    print("Enter your name.")
    name = input("")
    name = normalize(name)

    showhelp()

    while True:

        inp = input(f"{name}: ")
        inp = normalize(inp)

        if "reccomend" in inp or "suggest" in inp:
            reccomend()

        elif "tips" in inp or "packing" in inp:
            tips()

        elif "joke" in inp or "funny" in inp:
            joke()
        
        elif "exit" in inp or "bye" in inp:
            print(f"Goodbye {name}, safe travels.")
            break

        else:
            print("Please rephrase your request.")

if __name__ == "__main__":
    chat()