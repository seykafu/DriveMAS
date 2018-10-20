
def calcCurrCoins(carbonEmiss, milage):
	# Calculate amount of coins based from stats

	return (10**6)/(carbonEmiss*milage)

def calcPassiveRefCoins(carbonEmiss, milage):
	# Calculate amount of coins from person you referred to
	return 0.25*((10**6)/(carbonEmiss*milage))

def calcReferalCoins():
	# Amount of coins you would get from referring someone
	
	# Temperarly, it's an abritrary vaue
	return 5
