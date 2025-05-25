from flask import Flask,request,render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    Day = datetime.today().strftime('%A')
    return render_template('index.html',CurrentDay=Day)

@app.route('/sayHi')
def newHome():
    
    age = request.values.get('age')
    name = request.values.get('name')

    result ={
        'Age':age,
        'Name':name
    }

    return result

if __name__ == '__main__':
    app.run(debug=False)