from deck_pkg.CardModule import CardDeck

def main():
    print("Starting up Blackjack Card Game")
    gameDeck = CardDeck()
    gameDeck.fillDeck()
    gameDeck.shuffleDeck()
    print("Cards in deck: ", gameDeck.getCardCount())

    print("\nBeginning Blackjack Card Game\n")

    playerAmount = getPlayerAmount()

    #Game Setup
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

##    printPlayingHands(dealerHand, players)
    gameRunning = True

    while gameRunning:
        printPlayingHands(dealerHand, players)

        for i in range(playerAmount):
            playerTurn(players, i, gameDeck)
            
    
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

def playerTurn(players, index, deck):
    print("\nPlayer", index, "'s Turn")
    playing = True
    while playing:
        printPlayerHand(players, index)
        playerInput = input("Hit (H), Stay (S)")
        if playerInput.lower() == "h":
            playing = True
            players[index].append(deck.drawCard())
            continue
        elif playerInput.lower() == "s":
            playing = False
            break
        else:
            print("Unexpected input, try again!")
            continue

def printPlayingHands(dealer, players):
    #print dealer's hand
    printDealerHand(dealer)
    print()
    #print player hands
    printPlayerHands(players)

def printDealerHand(dealer):
    dealerStr = ""
    for i in range(len(dealer)):
        dealerStr += dealer[i].getCardInfoString()
        dealerStr += " "
    dealerStr += " -> "
    dealerStr += str(sumValue(dealer))
    print("Dealer's hand:", dealerStr)

def printPlayerHands(players):
    for i in range(len(players)):
        printPlayerHand(players, i)

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

def sumValue(cardHand):
    tempsum = 0
    for i in range(len(cardHand)):
        tempsum += blackjackFaceValueConvert(cardHand[i].getRawValue())
    finalSum = aceValueCheck(cardHand, tempsum)
    return finalSum

def blackjackFaceValueConvert(value):
    if value > 10:
        return 10
    else:
        return value

def aceValueCheck(cardHand, tempsum):
    finalSum = tempsum
    for i in range(len(cardHand)):
        if cardHand[i].getRawValue() == 1:
            if finalSum < 11:
                finalSum += 10
    return finalSum

def isSafeFromBust(value):
    if value <= 21:
        return True
    else:
        return False



main()
