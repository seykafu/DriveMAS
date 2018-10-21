from flask import Flask, render_template
import accountFunc
import calculation

app = Flask(__name__)
@app.route('/')
def home():

    result = accountFunc.getAccountInfoFromID(1)
    carType = result[4]
    CO2Output = 18.0
    if carType == 'electric':
	CO2Output = 1.77

    return render_template('index.html', **locals())



if __name__ == '__main__':
    app.run(debug=True)
