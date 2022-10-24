friend_list = []
option_list = ['7']
client_name = input("Hello! What is your name? ")

print("Welcome to your friend list " + client_name)
print('''
Type 1 for viewing your complete friend list
Type 2 for checking a particular name in your friend list
Type 3 for adding someone to your friend list
Type 4 for removing someone from your friend list
Type 5 for checking the number of friends you have on your friend list
Type 6 for deleting your entire friend list
Type 7 for exiting the program''')
option = input("Type your number here: ")

while option not in option_list:
    if option == '1':
        if len(friend_list) != 0:
            for friends in friend_list:
                print(friends)
        else:
            print("You don't have any friends added in your list right now")
        option = input("Type your number again: ")
    elif option == '2':
        friend_check = input("Type the name of the friend you want to check: ")
        if friend_check in friend_list:
            print("Yes, " + friend_check + " is there on your friend list.")
            option = input("Type your number again: ")
        else:
            print("No, " + friend_check + " is not on your friend list.")
            option = input("Type your number again: ")
    elif option == '3':
        add_friend = input("Type the name of the person you would like to add in this list: ")
        if add_friend in friend_list:
            print(add_friend + " is already in your list.")
            option = input("Type your number again: ")
        else:
            friend_list.append(add_friend)
            print(add_friend + " has been added to your friend list.")
            option = input("Type your number again: ")
    elif option == '4':
        remove_friend = input("Type the name of the person you would like to remove from this list: ")
        if remove_friend in friend_list:
            friend_list.remove(remove_friend)
            print(remove_friend + " has been removed from your friend list")
            option = input("Type your number again: ")
        else:
            print(remove_friend + " is not there in your friend list")
            option = input("Type your number again: ")
    elif option == '5':
        print("you have " + str(len(friend_list)) + " friends in your friend list")
        option = input("Type your number again: ")
    elif option == '6':
        friend_list.clear()
        friend_list.append(" ")
        print("Your friend list has been cleared")
        option = input("Type your number again: ")
    else:
        print("invalid")
        option = input("Type your number again: ")
if option == '7':
    print("Thank you for visiting your friend list. Bye!")
