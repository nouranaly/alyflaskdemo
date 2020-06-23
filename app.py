# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect
from model import get_breakfast_rating
from datetime import datetime

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time=datetime.now())

#the default for any route is a GET request
#writing methods= GET & POST will allow for multiple types of interactions
 
@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        print(request.form["breakfast"])
        user_breakfast=request.form["breakfast"] #this will grab the what the user entered for breakfast and store it in a variable called user_breakfast
        user_nickname=request.form["nickname"]
        breakfast_rating = get_breakfast_rating(user_breakfast)
        return render_template("breakfast.html", user_breakfast=user_breakfast, user_nickname=user_nickname, breakfast_rating=breakfast_rating) #this sends user_breakfast to the final page 
    else: 
        return redirect('/') # thi swill just send you back to the index page if you dont do it properly 

@app.route('/secret')
def secret():
    return "You found the secret page!"