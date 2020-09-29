from profile import Profile
from Windice import Windice
from bot import bot
from Sim import Sim
from simbot import simbot
import config

windice = Windice(config.API,config.WINDICE_BASE_URL)
sim = Sim(1110)

def main():
  #bot(windice,100000)
  simbot(sim,10000)

if __name__ == '__main__':
    main()
