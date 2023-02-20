from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form')

def form():
    return render_template('form.html')

@app.route('/data', methods = ['POST'])

def data():
    number = request.form.get('Number')
    if number.isnumeric():
        number = int(number)
        if (number % 2) == 0:
            return render_template('data.html', result='even')
        else:
            return render_template('data.html', result='odd')
    
    else:
        return render_template('data.html', result='nonumber')
        

