from deck_pkg.CardModule import CardDeck

#Driver function
def main():
    print("Starting up Blackjack Card Game")

    print("\nBeginning Blackjack Card Game\n")

    playerAmount = getPlayerAmount()

    gameRunning = True

    #Main game loop
    while gameRunning:
        #Game Setup
        gameDeck = CardDeck()
        gameDeck.fillDeck()
        gameDeck.shuffleDeck()
        print("Cards in deck: ", gameDeck.getCardCount())

        dealerHand = []
        players = []
        for i in range(playerAmount):
            players.append([])

        #Dealer draws
        for i in range(2):
            dealerHand.append(gameDeck.drawCard())

        #Players draw
        for i in range(playerAmount):
                for j in range(2):
                    players[i].append(gameDeck.drawCard())
                
        printPlayingHands(dealerHand, players)

        #Players take their turn
        for i in range(playerAmount):
            playerTurn(players, i, gameDeck)

        #Dealer takes turn
        dealerTurn(dealerHand, gameDeck)

        #Display results of the round
        roundResults(dealerHand, players)

        #Ask if still playing
        gameRunning = continuePlayCheck()

#Print results of the round
def roundResults(dealerHand, players):
    print("***Round Over***")
    print("Results:")
    printPlayingHands(dealerHand, players)
    
    if isSafeFromBust(sumValue(dealerHand)):
        print("Dealer safe from bust")
        for i in range(len(players)):
            if isSafeFromBust(sumValue(players[i])):
                if sumValue(players[i]) > sumValue(dealerHand):
                    print("Player", i, " won!")
                else:
                    print("Player", i, " lost!")
            else:
                print("Player", i, " lost because they busted!")
    else:
        print("Dealer busted")
        for i in range(len(players)):
            if isSafeFromBust(sumValue(players[i])):
                print("Player", i, " won!")
            else:
                print("Player", i, " lost because they busted!")

#Determine if playing anther round or not  
def continuePlayCheck():
    while True:
        playerInput = input("\nWould you like to play again? (Y/N)")
        if playerInput.lower() == "y":
            print("Restarting game.")
            return True
        elif playerInput.lower() == "n":
            print("Thanks for playing! See you later!")
            return False
        else:
            print("Unexpected input. Try Again!")
            continue

#Dealer turn logic
def dealerTurn(dealerHand, gameDeck):
    print("\n***Dealer Drawing***")
    printDealerHand(dealerHand)
    while(sumValue(dealerHand) < 17):
        dealerHand.append(gameDeck.drawCard())
        printDealerHand(dealerHand)
    print()
    
#Get the amount of players playing
def getPlayerAmount():
    choice = 0
    gettingInput = True
    val = 0
    while gettingInput:
        try:
            choice = input("\nHow many players?\n")
            val = int(choice)
            if val > 0:
                gettingInput = False
            else:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("That's not a number")    
    return val

#Player turn logic
def playerTurn(players, index, deck):
    print("\nPlayer", index, "'s Turn")
    playing = True
    while playing:
        printPlayerHand(players, index)
        playerInput = input("Hit (H), Stay (S)")
        #Hit
        if playerInput.lower() == "h":
            playing = True
            players[index].append(deck.drawCard())
            if(isSafeFromBust(sumValue(players[index]))):
                if(sumValue(players[index]) == 21):
                    print("BlackJack!")
                    printPlayerHand(players, index)
                    break
                else:
                    continue
            else:
                playing = False
                print("Player", index, " busted!")
                printPlayerHand(players, index)
                break
        #Stay
        elif playerInput.lower() == "s":
            playing = False
            break
        else:
            print("Unexpected input, try again!")
            continue

#Print dealer and players' hands
def printPlayingHands(dealer, players):
    #print dealer's hand
    printDealerHand(dealer)
    print()
    #print player hands
    printPlayerHands(players)

#Print dealer's hand
def printDealerHand(dealer):
    dealerStr = ""
    for i in range(len(dealer)):
        dealerStr += dealer[i].getCardInfoString()
        dealerStr += " "
    dealerStr += " -> "
    dealerStr += str(sumValue(dealer))
    print("Dealer's hand:", dealerStr)

#Print all player hands
def printPlayerHands(players):
    for i in range(len(players)):
        printPlayerHand(players, i)

#Print a player's hand
def printPlayerHand(players, index):
    playerStrTemp = ""
    playerStrTemp += "Player"
    playerStrTemp += str(index)
    playerStrTemp += "'s hand: "
    for j in range(len(players[index])):
        playerStrTemp += players[index][j].getCardInfoString()
        playerStrTemp += " "
    playerStrTemp += " -> "
    playerStrTemp += str(sumValue(players[index]))
    print(playerStrTemp);

#Calculate the value of a hand
def sumValue(cardHand):
    tempsum = 0
    for i in range(len(cardHand)):
        tempsum += blackjackFaceValueConvert(cardHand[i].getRawValue())
    return aceValueCheck(cardHand, tempsum)

#Modifies face card values to 10
def blackjackFaceValueConvert(value):
    if value > 10:
        return 10
    else:
        return value

#Modifies the value of aces depending on the overall value
def aceValueCheck(cardHand, tempsum):
    finalSum = tempsum
    for i in range(len(cardHand)):
        if cardHand[i].getRawValue() == 1:
            if finalSum < 11:
                finalSum += 10
    return finalSum

#Check if the value is below 21
def isSafeFromBust(value):
    if value <= 21:
        return True
    else:
        return False

main()
