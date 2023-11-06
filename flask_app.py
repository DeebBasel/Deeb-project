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
    try:
        num1 = float(num1)
        num2 = float(num2)
        result = num1 + num2
    except:
        print('Error: input values must be numbers')
        result = None
    return result



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
    if request.method == 'GET':
        return render_template('get_numbers.html')

    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    result = add(num1, num2)
    if result is None:
        return "Error occured , please check the log"
    else:
        return f"The sum is {result}"



if __name__ == '__main__':
    app.run(debug=True)
