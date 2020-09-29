import numpy as np

def generate_highs(payout,amount):
  val=((10000 / payout) - ((10000 / payout)*0.01)-1)
  highs = np.linspace(val,9999,amount,dtype='int')

  return list(highs)

def get_low_value_from_high(payout,high_vals):
  lows = []
  val = high_vals[0]
  for i in high_vals:
    lows.append(i-val)

  return lows

def win_counter(lows,highs,result,counter):
  hi_lo = dict(zip(lows,highs))
  for index,(k,v) in enumerate(hi_lo.items()):
    if k < result['result'] < v:
      counter[index] += 1 
  return   
    
      
def bot(site_obj):
  #basic stuff
  baselow = 1000
  basehigh = 9999

  curr = "doge"
  basebet = 0.35
  betlow = True
  low = baselow
  high = basehigh
  nextbet = basebet

  bet_count = 0

  #for 
  payout=5
  amount_payout_range=55
  counter = [0 for i in range(amount_payout_range)]

  highs = generate_highs(payout,amount_payout_range)
  lows = get_low_value_from_high(payout,highs)

  has_started_strat = False
  has_started_count = 0


  #bet starting here
  while True:
    previousbet = nextbet
    balance = site_obj.get_user()
    bet_count += 1


    if bet_count > payout:
      for i in counter:
        counter[i] -= 1
      has_started_strat = True
      has_started_count += 1
      position = counter.index(min(counter))
      low = int(lows[position])
      high = int(highs[position])
      nextbet = 1

    if has_started_count > payout:
      has_started_strat = False
      has_started_count = 0
      bet_count = 0
      low = baselow
      high = basehigh
      nextbet = basebet


    res = site_obj.make_single_bet(curr,nextbet,betlow,low,high)
    win_counter(lows,highs,res,counter)

    if res['win'] != 0:
      if has_started_strat == True:
        has_started_strat = False
        has_started_count = 0
        bet_count = 0
        low = baselow
        high = basehigh
        nextbet = basebet
        
      print(str(balance['data']['balance'][curr] )+ curr)
    else:
      if has_started_strat == True:
        nextbet = previousbet + 0.25
      else:
        nextbet = basebet  
      print(str(balance['data']['balance'][curr] )+ curr)
      
 
  return




