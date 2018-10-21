import sqlPython as sqlpy
from accountFunc import getAccountInfoID
from accountFunc import updateMilageById
from accountFunc import updateCoinsById
from accountFunc import updateCarTypeById
from accountFunc import createAccount
from calculation import calcCurrentCoins
from calculation import getCostFromGas
from calculation import totalCarbonOutput


def main() :
    electricCoin = 0
    createAccount('Brax','braxday','gas')
    updateCarTypeById(1,'gas')
    res = getAccountInfoID(1)
    if res[5] is not None:
        electricCoin = calcCurrentCoins(18,res[5])
        updateCoinsById(1,electricCoin)
        getCostFromGas(2.856,24.7)
        totalCarbonOutput(18,res[5])






