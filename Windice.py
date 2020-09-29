import requests
import json
import strgen
import time
seed = strgen.StringGenerator("[\d\w]{15}").render()

class Windice:

  def __init__(self,api,base_url):
    self.api = api
    self.base_url = base_url

  def get_seed(self):
    response = requests.get(
      self.base_url + '/seed',
      headers={'Authorization': self.api},
    )
    res = response.json()
    if res['status'] != 'success':
      print(res['message'])
      quit()
    return response.json()  

  def change_seed(self,newseed=seed):
    seed_dict = {
      "value":newseed
    }
    response = requests.post(
      self.base_url + '/seed',
      headers={
        'Content-type': 'application/json',
        'Authorization': self.api,
        },
      data = json.dumps(seed_dict)
    )
    res = response.json()
    if res['status'] != 'success':
      print(res['message'])
      quit()
    return response.json()

  def get_user(self):
    response = requests.get(
      self.base_url + '/user',
      headers={'Authorization': self.api},
    )
    return response.json()

  def get_stats(self):
    response = requests.get(
      self.base_url + '/stats',
      headers={'Authorization': self.api},
    )
    return response.json()

  def create_bet_data(self,curr,bet_size,game_bool,low,high):
    if low < 0:
      print('low has to be over 0')
      quit() 
    elif high > 9999:
      print('high has to be under 9999')
      quit() 
    # in == True, out == False 
    if game_bool == True:
      game = "in"
    else:
      game = "out"  
    
    data = {
      "curr": curr,
      "bet": bet_size,
      "game": game,
      "low": low,
      "high": high
    }	
    return data     

  def roll(self,roll_data):
    try:
      response = requests.post(
        self.base_url + '/roll',
        headers={
          'Content-type': 'application/json',
          'Authorization': self.api,
          },
        data=json.dumps(roll_data),
        #verify = False
      )
    except:
      time.sleep(5)
       
    res = response.json()
    if res['status'] != 'success':
      print(res['message'])
      quit()
    else:
      res = res['data']  
    return res

  def make_single_bet(self,*args):
    bet = self.create_bet_data(*args)
    res = self.roll(bet)
        
    return res