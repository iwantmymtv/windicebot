import random
import json

class Sim:
  def __init__(self,balance):
    self.balance = balance

  def make_single_bet(self,curr,bet,game,low,high):
    if game == True:
      game = "in"
    else:
      game = "out" 
      
    if game == "in":
      chance =((high - low ) + 1) / 100
      gamein = True
    else:
      chance =((10000 - (high - low ))-1) / 100
      gamein = False

    chance = round(chance,2)  
    payout = round((100/chance * 0.99),4)

    response = {
          "curr": curr,
          "bet": bet,
          "win": 0,
          "pointLow": low,
          "pointHigh": high,
          "game": game,
          "chance": chance,
          "payout": payout,
          "result": 0,
        }
    if bet > self.balance:
      return print('balance is too low')
      
      
    number = random.randrange(0, 9999)
    if gamein:
      if (low<= number <= high):
        print('won')
        self.balance += (bet * payout) - bet
        win = {
          "win": (bet * payout) - bet,
          "result": number,
        }
        response.update(win)
      else:
        print('lost')
        self.balance -= bet
        lost = {
          "result": number,
        }
        response.update(lost)
    else:
      if (not low<= number <= high):
        print('won')
        self.balance += (bet * payout) - bet
        win = {
          "win": (bet * payout) - bet,
          "result": number,
        }
        response.update(win)
      else:
        print('lost')
        self.balance -= bet
        lost = {
          "result": number,
        }
        response.update(lost)      
      
    return response


      
      