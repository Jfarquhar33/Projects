# Justin Farquhar Project 2


# The dictionary links a room to other rooms.
rooms = {
        'Porch': {'East': 'Dining Room'},
        'Dining Room': {'North': 'Living Room', 'East': 'Kitchen', 'West': 'Porch', 'item': 'Laser Pointer'},
        'Living Room': {'North': 'Bedroom', 'South': 'Dining Room', 'item': "Olive's Favorite Ball"},
        'Kitchen': {'North': 'Laundry Room', 'West': 'Dining Room', 'item': 'Couple of Treats'},
        'Laundry Room': {'South': 'Kitchen', 'item': 'Dryer Sheet'},
        'Bedroom': {'West': 'Bathroom', 'East': 'Closet', 'South': 'Living Room', 'item': 'Dinosaur Outfit'},
        'Bathroom': {'East': 'Bedroom', 'item': 'Drink of Water'},
        'Closet': {'West': 'Bedroom', 'item': 'Maintenance Person'}
    }

# start in Porch, and print all the introductory items.
current_room = 'Porch'
inventory = []
print("Welcome to the text based Olive's Great Adventure Game\n""Blueberry has been caught by the Maintenance Person!")
print('Collect all 6 items to save Blueberry and win the game, or be caught by the Maintenance Person')
print("Possible move commands: go North, go South, go East, go West\n" "If you'd like to exit, just type 'exit'")
print("Add to Inventory: get 'item name'\n")
print('You are in the', current_room)
print('Inventory: []')
# initializing a while loop to keep the game going until conditions are met
while current_room != 'Exit' or current_room != 'exit':
    # defining a 'lose' condition and ending the session
    if current_room == 'Closet' and len(inventory) != 6:
        current_room = 'Exit'
        print('The Maintenance Person has caught Olive!')
        print('Thanks for trying the game and feel free to try again!')
        break
    # defining a 'win condition and ending the session
    elif current_room == 'Closet' and len(inventory) == 6:
        print('Congratulations!You were able to collect all of the items and save Blueberry!')
        print('Thanks for playing :)')
        break
    action = input('Enter your move: ')
    action_tokens = action.split()
    # ruling out if input is longer than two words, making it invalid
    if len(action_tokens) > 5:
        print('That is not a valid command!')
    # determining if input is a valid option
    elif action_tokens[0] == 'go':
        # second if clause to determine if its a valid direction
        if action_tokens[1] in rooms[current_room]:
            current_room = rooms[current_room][(action_tokens[1])]
            print('\nYou are in the', current_room)
            print('Inventory: {}'.format(inventory))
            if 'item' in rooms[current_room]:
                room_item = rooms[current_room]['item']
                if room_item not in inventory:
                    print('You see a', room_item)
            print('------------------------')
        # outputting for invalid direction
        else:
            print("You can't go that way!")
    # determining if player is trying to 'get' item
    elif action_tokens[0] == 'get':
        current_item = rooms[current_room]['item']
        # seeing if item typed is in the current room does get slightly redundant restating inventory and current
        # room after picking up the item, but think it is more user-friendly to be reminded.
        if action_tokens[1] in current_item:
            inventory.append(current_item)
            print('You pick up the ', current_item)
            print('------------------------')
            print('You are in the', current_room)
            print('Inventory: {}'.format(inventory))
            print('------------------------')
            # or printing out that it is not
        else:
            print("That's not a valid item")
    # determining if player is trying to leave the game and ending loop
    elif action_tokens[0] == 'exit' or action_tokens[0] == 'Exit':
        current_room = 'Exit'
        print('You have successfully exited.')
        break
        # was really convinced setting current_room to 'Exit' would have ended the loop,
        # but used this as a workaround.
    # outputting if move does not include 'go'
    else:
        print("That is not a valid move!")

ending = input('Please type "exit" once you are finished!:')
