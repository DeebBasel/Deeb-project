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
def naseem_sum(num1, num2):
        return num1 + num2

@app.route('/')
def home():
    return 'please navigate to your name'

@app.route('/nermeen')
def nermeen():
    return render_template('nermeen.html')

@app.route('/fadi')
def fadi():
    return render_template('fadi.html')

@app.route('/naseem', methods=['GET','POST'])
def naseem():
    num1 = request.args.get('num1', 1)
    num2 = request.args.get('num2', 1)
    try:
        num1 = int(num1)
        num2 = int(num2)
    except:
        print('the inputs must be integers')

    return naseem_sum(num1, num2)

if __name__ == '__main__':
    app.run()
