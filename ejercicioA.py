
def show_next_track():
    playlist = ["Hey Jude",
                "Helter Skeleter",
                "Something"]
    for track in playlist:
        print(f"Next up: {track}")

show_next_track()

def display_players(team):
    number = 1
    for name in team:
        print(f"Player {number}: {name}")
        #number += 1

team_1 = ["Kim", "Lee"]
team_2 = ["Meg", "Jo"]
display_players(team_1)

def helve_prices(cart):
    for price in cart :
        print(f"New price: {price/2}")
cart_list = [5, 20, 8]
helve_prices(cart_list)


def do_countdown(counter):
    while counter > 0:
        print(counter)
        counter -= 1
    print("Go")
do_countdown(3)

def onboard_passengers(bookings):
    counter = 1
    while counter <= bookings:
        print(f"Passengers {counter} on board")
        counter += 1
onboard_passengers(3)

def get_winner(top_players):
    winner = top_players[1]
    print(f"Game winner: {winner}")
top_players = ["Jay", "Meg", "Cy"]
get_winner(top_players)


def is_booked(passengers):
    print(len(passengers) >= 4)
passengers = ["June", "Sam", "Lee"]
is_booked(passengers)


def calculate(operator, x, y):
    if operator == "+":
        print(x + y)
    elif operator == "-":
        print(x - y)
    else:
        print(f"unknown: {operator}")
calculate( "-", 30, 10)

