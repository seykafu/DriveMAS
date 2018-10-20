
def calcCurrCoins(carbonEmiss, milage):
	# Calculate amount of coins based from stats

	return int((10**6)/(carbonEmiss*milage))

def calcPassiveRefCoins(carbonEmiss, milage):
	# Calculate amount of coins from person you referred to
	return int(0.25*((10**6)/(carbonEmiss*milage)))

def calcReferalCoins():
	# Amount of coins you would get from referring someone
	
	# Temporarily, it's an arbitrary value
	return 5

def getCostFromGas(stateGasCost, milesPerGallon):
	
	return stateGasCost*milesPerGallon


def getCostfromElectric(stateElecCost, milesPerBatt):

	return stateElecCost*milesPerBatt

