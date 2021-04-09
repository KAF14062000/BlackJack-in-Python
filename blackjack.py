from art import logo
import random

print(logo)

game = False
def gameState(user, ai):
  gameIs = False
  if user <= 1 or ai <= 1:
    gameIs = True
    return gameIs
  else:
    return gameIs




def cards():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def getScore(cards):
  Score = sum(cards)
  if Score == 21 and len(cards) == 2:
    return 0
  elif 11 in cards and Score > 21 and len(cards) == 2:
    cards.remove(11)
    cards.append(1)
    Score = sum(cards)
    return Score
  elif Score > 21:
    return 1
  else:
    return Score



user = []
ai = []
winUser = 0
winAi = 0

for _ in range(2):
  user.append(cards())
  ai.append(cards())

print(f"You have {user} in your hand and your score is: {sum(user)}")
print(f"The dealer has: {random.choice(ai)}")
userScore = getScore(user)
aiScore = getScore(ai)
game = gameState(userScore, aiScore)
if game:
  if userScore == 0 and aiScore > 1:
    print("You have won. Blackjack!")
  elif aiScore == 0 and userScore > 1:
    print(f"The dealer has {ai} and a score of {sum(ai)}.")
    print("You Lost. Dealer has Blackjack!")
  elif aiScore == userScore:
    print("It's a draw")
else:
  while not game and len(user) < 4:
    if input("'y' for another card: ") == "y":
      user.append(cards())
      userScore = sum(user)
      if userScore == 21:
        game = True
        print(f"Your hand has : {user} and your score is: {userScore}")
        print("You have won!")
        break
      elif userScore < 21:
        print(f"Your hand has : {user} and your score is: {userScore}")
      elif userScore > 21:
        print(f"Your hand has : {user} and your score is: {userScore}")
        print("You went over 21. You have lost.")
        game = True
        break
    else:
      break

  #code for AI
  if not game:
    if aiScore < 18:
      while not game and aiScore < 18 and len(ai) < 4:
        ai.append(cards())
        aiScore = sum(ai)
        if aiScore == 21:
          game = True
          print(f"Dealer has {ai} and a score of: {aiScore}")
          print("You have lost.")
          break
        elif aiScore < 21:
          pass
        elif aiScore > 21:
          print("You have won!")
          print(f"Dealer has {ai} and a score of: {aiScore}")
          game = True
          break
    else:
      if aiScore < userScore:
        print(f"Dealer has {ai} and a score of: {aiScore}")
        print("You've won.")
        game = True
      elif userScore < aiScore:
        print("You've lost")
        print(f"Dealer has {ai} and a score of: {aiScore}")
        game = True

    if not game:
      if aiScore < 21:
        if aiScore < userScore:
          print(f"Dealer has {ai} and a score of: {aiScore}")
          print("You have won.")
        elif userScore < aiScore:
          print("You have lost.")
          print(f"Dealer has {ai} and a score of: {aiScore}")
        elif aiScore == userScore:
          print("It's a draw")
          print(f"Dealer has {ai} and a score of: {aiScore}")
