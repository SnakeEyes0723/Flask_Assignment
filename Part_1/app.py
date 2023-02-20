from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/GET /')
def home():
    time = datetime.now()
    date_time = time.strftime("%m/%d/%Y, %H:%M:%S")
    return render_template('timedisplay.html', date_time=date_time)

if __name__ == "main":
    app.run(debug = True)


