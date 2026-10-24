import re, random
from colorama import Fore, init

init(autoreset = True) 

destinations = {

"beaches": ["Bali", "Maldives", "Phuket"],

"mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],

"cities": ["Tokyo", "Paris", "New York"]

}

spot = {
    "Bali": ["Uluwatu Temple", "Tanah Lot", "Ubud Monkey Forest"],
    "Maldives": ["Malé", "Maafushi Island", "Banana Reef"],
    "Phuket": ["Patong Beach", "Big Buddha", "Phi Phi Islands"],

    "Swiss Alps": ["Matterhorn", "Jungfraujoch", "Lake Geneva"],
    "Rocky Mountains": ["Rocky Mountain National Park", "Lake Louise", "Banff National Park"],
    "Himalayas": ["Rohtang Pass", "Valley of Flowers", "Everest Base Camp"],

    "Tokyo": ["Tokyo Tower", "Shibuya Crossing", "Senso-ji Temple"],
    "Paris": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"],
    "New York": ["Statue of Liberty", "Central Park", "Times Square"]
}

cuisines = {
    "Bali": ["Nasi Goreng", "Satay", "Babi Guling"],
    "Maldives": ["Mas Huni", "Garudhiya", "Bis Keemiya"],
    "Phuket": ["Pad Thai", "Tom Yum Goong", "Massaman Curry"],

    "Swiss Alps": ["Cheese Fondue", "Raclette", "Rösti"],
    "Rocky Mountains": ["Bison Burger", "Rocky Mountain Trout", "Elk Steak"],
    "Himalayas": ["Momos", "Thukpa", "Dal Bhat"],

    "Tokyo": ["Sushi", "Ramen", "Tempura"],
    "Paris": ["Croissants", "Coq au Vin", "French Onion Soup"],
    "New York": ["New York Pizza", "Bagels", "Cheesecake"]
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
    print("Reccomend tourist spots. (type spots)")
    print("Reccomend popular cuisines from your destination. (type food)")
    print("Give packing tips. (type tips)")
    print("Tell a joke. (type joke)")
    print("Play a game. (type game)")
    print("Type exit or bye to leave.")

def cuisine():
    des = input("Enter your destination: ")

    if des not in cuisines:
        print("This feature is not available for this particular place.")
    else:
        print(f"Popular cuisine from {des}: {cuisines[des]}")

def spots():
    des = input("Enter destination: ")
    if des not in spot:
        print("This feature is not available for this particular place.")
        spots()
    else:
        print(f"Popular tourist spots in {des}: {spot[des]}")
    

def playgame():
    print("Guess the number I chose. (1-100)")
    num = random.randint(1,100)
    
    while True:

      guess = int(input("You: "))
      
      if guess < num:
        print("Hint: Higher")
      elif guess > num:
        print("Hint: Lower")
      elif guess == num:
        print("You win!")
        break


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

    showhelp()

    while True:

        inp = input(f"{name}: ")
        inp = normalize(inp)

        if "reccomend" in inp or "suggest" in inp:
            reccomend()

        elif "spots" in inp:
            spots()
        elif "cuisine" in inp or "food" in inp:
            cuisine()

        elif "tips" in inp or "packing" in inp:
            tips()

        elif "joke" in inp or "funny" in inp:
            joke()

        elif "game" in inp or "play" in inp:
            playgame()
         
        elif "exit" in inp or "bye" in inp:
            print(f"Goodbye {name}, safe travels.")
            break

        else:
            print("Please rephrase your request.")

if __name__ == "__main__":
    chat()