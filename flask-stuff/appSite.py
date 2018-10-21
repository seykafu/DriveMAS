from flask import Flask, render_template, request
import accountFunc
import calculation

app = Flask(__name__)
@app.route('/')
def home():

    milesPerGallon = 24 

    result = accountFunc.getAccountInfoFromID(1)

    userId = result[0]
    username = result[1]
    coinsTotal = result[3]
    carType = result[4]
    milage = result[5]

    milage = 1000

    CO2OutputGas = 18.0
    CO2OutputElectric = 1.77

    totalCO2 = calculation.totalCarbonOutput(CO2OutputGas,milage) 
    totalCO2Electric = calculation.totalCarbonOutput(CO2OutputElectric,milage)
 
    stateFuelCost = accountFunc.getGasStatsByState('MA') 
    gasCost = round(calculation.getCostFromGas(stateFuelCost[1], milesPerGallon),2)

    electricCost = round(calculation.getCostfromElectric(stateFuelCost[2], milesPerGallon),2)
    

    amountOfMoneySaved = gasCost - electricCost
   

    coinsEarned = round(calculation.calcCurrCoins(CO2OutputGas, milage),3)
 
    # **locals() allows us to pass all local variables
    return render_template('index.html', **locals())

@app.route('/referal',methods=['GET'])
def reroute():
	refCode = request.args.get('code',None)
	print refCode
	return "<html>"+refCode+"</html>"

if __name__ == '__main__':
    app.run(debug=True)
