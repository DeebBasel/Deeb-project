# how to use css in python_ flask
# flask render_template example

from flask import Flask, request, render_template

# WSGI Application
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')


# @app.route('/')
# def welcome():
#     return "This is the home page of Flask Application"
def add(num1, num2):
        return num1 + num2

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/nermeen')
def nermeen():
    return render_template('nermeen.html')

@app.route('/fadi')
def fadi():
    return render_template('fadi.html')

@app.route('/naseem', methods=['GET','POST'])
def naseem():
    num1 = request.form.get('num1', type=int)
    num2 = request.form.get('num2', type=int)
    return add(num1, num2)

if __name__ == '__main__':
    app.run(debug=True)
