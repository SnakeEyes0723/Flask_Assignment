from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form')

def form():
    return render_template('form.html')

@app.route('/data', methods = ['POST'])

def data():
    org = request.form.get('Organization')
    if org.isnumeric():
        org = int(org)
    if org == 1:
        return render_template('data.html', result = 'game')
    elif org == 2:
        return render_template('data.html', result = 'drama')
    elif org == 3:
        return render_template('data.html', result = 'hack')
    elif org == 4:
        return render_template('data.html', result = 'run')
    elif org == 5:
        return render_template('data.html', result = 'cook')
    else:
        return render_template('data.html', result = 'invalid')