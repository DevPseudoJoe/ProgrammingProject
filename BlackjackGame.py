from random import randint
from getpass import getpass
import sys


def main():
    validoptions = ["Sign In", "Sign Up", "Exit"]
    firstoption = input(
        f"Welcome to BlackJoe! Would you like to:\n\t1 - {validoptions[0]}\n\t2 - {validoptions[1]}\n\t3 - {validoptions[2]}\n>>> "
    )
    try:
        firstoption = int(firstoption)
        if firstoption == 1:
            RetrieveCredentials()
        elif firstoption == 2:
            SignUp()
        elif firstoption == 3:
            sys.exit()
        else:
            print("Please choose a correct option.\n")
            return main()
    except ValueError:
        print("Please enter a valid number.\n")
        return main()
    except Exception as e:
        print("An error has occurred...\n")
        print("(There may be no recorded users. Please Sign Up!)\n")
        return main()


def SignUp():
    newusername = ""
    newpassword = ""
    validoptions = ["Yes", "No"]
    username = input("Please enter your username:\n>>> ")
    randpassword = int(
        input(
            f"Would you like to generate a random password?\n\t1 - {validoptions[0]}\n\t2 - {validoptions[1]}\n>>> "
        )
    )
    try:
        if randpassword == 1:
            for i in range(15):
                newpassword += chr(randint(33, 126))
            print(
                f"You password is '{newpassword}', please save it in a password manager."
            )
            encrypted = ""
            for each in newpassword:
                encrypted += chr(ord(each) + 3)
            newpassword = encrypted
        elif randpassword == 2:
            password = getpass("Please enter your password:\n>>> ")
            repeatpassword = getpass("Please re-enter you password:\n>>> ")
            while password != repeatpassword:
                print("Passwords do not match!")
                password = getpass("Please enter your password:\n>>> ")
                repeatpassword = getpass("Please re-enter you password:\n>>> ")
            for char in password:
                newpassword += chr(ord(char) + 3)
        else:
            print("Please choose a correct option")
            while randpassword not in validoptions:
                return SignUp()
    except Exception as e:
        print("An error has occurred...\n")
        return SignUp()
    for char in username:
        newusername += chr(ord(char) + 3)
    with open("usernames.txt", "a") as MyFile:
        MyFile.write(f"{newusername}\n")
    with open("passwords.txt", "a") as MyFile:
        MyFile.write(f"{newpassword}\n")
    return main()


def RetrieveCredentials():
    with open("usernames.txt", "r") as MyFile:
        usernames = [line.strip() for line in MyFile]
    for i in range(len(usernames)):
        newusername = ""
        for char in usernames[i]:
            newusername += chr(ord(char) - 3)
        usernames[i] = newusername
    with open("passwords.txt", "r") as MyFile:
        passwords = [line.strip() for line in MyFile]
    for i in range(len(passwords)):
        newpassword = ""
        for char in passwords[i]:
            newpassword += chr(ord(char) - 3)
        passwords[i] = newpassword
    SignIn(usernames, passwords)


def SignIn(usernames, passwords):
    inputtedusername = input("Please enter your username:\n>>> ")
    inputtedpassword = getpass("Please enter your password:\n>>> ")
    if inputtedusername in usernames and inputtedpassword == passwords[
        usernames.index(inputtedusername)
    ]:
        print("Signing In...")
        game(total)
    else:
        validoptions = ["Enter Again", "Quit"]
        firstoption = input(
            f"Username or Password Incorrect:\n\t1 - {validoptions[0]}\n\t2 - {validoptions[1]}\n>>> "
        )
        try:
            firstoption = int(firstoption)
            if firstoption == 1:
                return SignIn(usernames, passwords)
            elif firstoption == 2:
                sys.exit()
        except Exception:
            print("An error has occured...\n")
            return SignIn(usernames, passwords)


def sortCards():
    cardType = ["King","Queen","Jack","10","9","8","7","6","5","4","3","2"]
    cardSuit = ["Spades","Hearts","Clubs","Diamonds"]
    cards = []
    for x in cardSuit:
        for y in cardType:
            cards.append([y, x])
    return cards


def playerTakeCard(cards):
    randomcard = cards[randint(0, len(cards)-1)]
    cards.remove(randomcard)
    tens = ["King","Queen","Jack"]
    if randomcard[0] in tens:
        value = 10
    else:
        value = int(randomcard[0])
    return randomcard, value


def dealerTakeCard(cards):
    randomcard = cards[randint(0, len(cards)-1)]
    cards.remove(randomcard)
    tens = ["King","Queen","Jack"]
    if randomcard[0] in tens:
        value = 10
    else:
        value = int(randomcard[0])
    return randomcard, value


def showcardsv1(dealer, player, playerTotal):
    print("\nYour deck: ")
    for i in range(len(player)):
        print(f"Card {i+1}: {player[i][0]} of {player[i][1]}")
    print(f"Player total: {playerTotal}\n")
    print("Dealer's deck: ")
    print(f"Card 1: {dealer[0][0]} of {dealer[0][1]}")
    print("Card 2: Hidden")


def showcardsv2(dealer, player, playerTotal, dealerTotal):
    print("\nYour deck: ")
    for i in range(len(player)):
        print(f"Card {i+1}: {player[i][0]} of {player[i][1]}")
    print(f"Player total: {playerTotal}\n")
    print("Dealer's deck: ")
    for i in range(len(dealer)):
        print(f"Card {i+1}: {dealer[i][0]} of {dealer[i][1]}")
    print(f"Dealer total: {dealerTotal}")


def formatCard(card):
    return f"{card[0]} of {card[1]}"


def game(total):
    if total == 0:
        print("You are out of chips, please restart the game")
        return

    cards = sortCards()
    player = []
    dealer = []
    playerTotal = 0
    dealerTotal = 0

    try:
        bet = int(input(f"\nYour chips total to £{total}. How much will you bet?\n>>> "))
    except:
        print("\nPlease enter a number! Game Restarting...\n")
	    total += bet
        return game(total)

    if bet > total:
        print("\nPlease enter a bet that is lower than your total.\n")
        return game(total)

    print("Bet accepted")
    total -= bet

    for i in range(2):
        playerSelection, value = playerTakeCard(cards)
        player.append(playerSelection)
        playerTotal += value

    for i in range(2):
        dealerSelection, value = dealerTakeCard(cards)
        dealer.append(dealerSelection)
        dealerTotal += value

    showcardsv1(dealer, player, playerTotal)
    print("Options:")
    validOptions = ["Stand", "Hit"]
    for i in range(len(validOptions)):
        print(f"{i+1} - {validOptions[i]}")

    try:
        playerDecision = int(input("\nPlease enter an option >>> "))
    except:
        print("Invalid input")
        total += bet
        return game(total)

    if playerDecision == 1:
        while dealerTotal < 17:
            dealerSelection, value = dealerTakeCard(cards)
            dealer.append(dealerSelection)
            dealerTotal += value
            print(f"\n>The dealer's new card is a{formatCard(dealerSelection)}")

        showcardsv2(dealer, player, playerTotal, dealerTotal)

        if dealerTotal > 21:
            total += 2 * bet
            print("\nDealer busts! You win!\n")
        elif playerTotal > dealerTotal:
            total += 2 * bet
            print("\nYou have won!\n")
        elif dealerTotal > playerTotal:
            print("\nYou have lost.\n")
        else:
            print("Draw.")
            total += bet

        return game(total)

    elif playerDecision == 2:
        while playerTotal < 21:
            playerSelection, value = playerTakeCard(cards)
            player.append(playerSelection)
            playerTotal += value
            print(f">Your new card is {formatCard(playerSelection)}")
            print(f">Your new total is {playerTotal}")

            if playerTotal >= 21:
                break

            print("Options:")
            validOptions = ["Stand", "Hit",]
            for i in range(len(validOptions)):
                print(f"{i+1} - {validOptions[i]}")
                
            try:
                playerDecision = int(input("\nPlease enter an option >>> "))
            except:
            print("Invalid input")
	        total += bet
            return game(total)

            if playerDecision == 1:
                break

        if playerTotal > 21:
            print("\nYou have lost.")
            return game(total)

        while dealerTotal < 17:
            dealerSelection, value = dealerTakeCard(cards)
            dealer.append(dealerSelection)
            dealerTotal += value
            print(f">The dealer's new card is a {formatCard(dealerSelection)}")

        showcardsv2(dealer, player, playerTotal, dealerTotal)

        if dealerTotal > 21 or playerTotal > dealerTotal:
            total += 2 * bet
            print("\nYou have won!")
        elif dealerTotal > playerTotal:
            print("\nYou have lost.")
        else:
            print("Draw.")
            total += bet

        return game(total)

    else:
        print("Invalid option")
        return game(total)


if __name__ == "__main__":
    total = 5000
    main()
