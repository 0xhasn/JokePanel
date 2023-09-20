import requests

stater = False
fresh = False


def get_joke(joke_type="Any"):
    url = f"https://v2.jokeapi.dev/joke/{joke_type}"
    response = requests.get(url)

    if response.status_code == 200:
        joke_data = response.json()
        if 'joke' in joke_data:
            return joke_data['joke']
        elif 'setup' in joke_data and 'delivery' in joke_data:
            return f"{joke_data['setup']} - {joke_data['delivery']}"
        else:
            return "Invalid joke format"
    else:
        return f"Error: {response.status_code}"




joke_programming = get_joke("Programming")
joke_miscellaneous = get_joke("Miscellaneous")
joke_spooky = get_joke("Spooky")
joke_christmas = get_joke("Christmas")
joke_dark = get_joke("Dark")



def display_menu():
    print("Main Menu:")
    print("1. Any Joke")
    print("2. Programming Joke")
    print("3. Dark Joke")
    print("4. Quit")

def option1():
    joke = get_joke("Any")
    print(f"\n You selected Option 1\nHere is your single Joke!\n... \n{joke}\n..")

def option2():
    joke = get_joke("Programming")
    print(f"\n You selected Option 2\nHere is your Programming Joke!\n... \n{joke_programming}\n..")

def option3():
    joke = get_joke("Dark")
    print(f"\n You selected Option 2\nHere is your Dark Joke!\n... \n{joke_dark}\n..")

# Main loop
while stater == False:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        option1()
        stater = True
    elif choice == '2':
        option2()
        stater = True
    elif choice == '3':
        option3()
        stater = True
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
