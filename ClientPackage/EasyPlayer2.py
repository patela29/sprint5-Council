__author__ = 'Anand'
"""
This class will act like the game administrator. It should be connected by the person handling the
tournament. This 'player' will manage the current tournament, game, number of players, etc...
"""
__author__ = 'Paul Council'
import time

from PlayerClient import *
from AvailablePlayers.TestPlayer2 import *


HOST = "150.250.190.225"

player1 = TestPlayer2()

client1 = PlayerClient(player1)

# attempt to connect game controller to the server room
client1.client_connect(host=HOST)
client1.set_name("Fuzzy")
client1.verify_connection
client1.register_player()
client1.verify_registration()
time.sleep(10)
#TODO need to query server for number of players and do the math to find out the number of matches we will be participating in
for x in range(0,3):        #this look here for convenience
    client1.submit_move()
client1.get_tournament_results()