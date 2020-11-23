import random

class MCsim():
    def __init__(self):
        self.match_hist = []
        self.match = None
        self.wr = None
    def play(self, wr=0.5):
        self.match = random.choices(['Win', 'Lose'], [wr, 1-wr])
        self.match_hist.append(self.match)
    def getMatchHist(self):
        return self.match_hist
    def __str__(self):
        return 'League of Legends'

def play(game, numGames, wr, toPrint):
    for i in range(numGames):
        game.play(wr)
    matches = game.getMatchHist()
    act_wr = (matches.count(['Win'])/len(matches)) * 100
    if toPrint:
        print("\t", numGames, "games of", game)
        print("\t", 'Expected win rate', wr*100, '. Actual win rate = ', act_wr)
    return act_wr

random.seed(0)
sim = MCsim()
for numGames in (10, 100, 1000):
    for i in range(3):
        print('Trial', i+1, ':')
        play(sim, numGames, 0.45, True)
        
        