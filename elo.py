class Player:

	def __init__(self, pid, elo):
		self.id = int(pid)
		self.elo = float(elo)

def ExpectedResult (p1, p2):
    exp = (p1-p2)/400.0
    return 1/((10.0**(exp))+1)

def GameDone (winner, loser):
    result = ExpectedResult(winner.elo, loser.elo)
    winner.elo = winner.elo + (20*(1-result))
    loser.elo = loser.elo + (20*(0-(1-result)))
    

    