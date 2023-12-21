# app.py
from flask import Flask, render_template, request
from calculator import calculate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def perform_calculation():
    expression = request.form['input']
    result = calculate(expression)
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
