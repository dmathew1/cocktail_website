from flask import Flask,jsonify,request,render_template
from cocktail import Cocktails
from loggers import logger

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
c = Cocktails()
ingrList = []

@app.route("/")
def index():
    logger.info("Index Page")
    return render_template('index.html')

@app.route('/cocktail/add', methods=['POST'])
def addIngr():
    d = request.form['ingr']
    print(d)
    global ingrList
    ingrList.append(d)
    return render_template('cocktail_table.html', ingrList=ingrList)

@app.route('/viewCocktail')
def viewCocktails():
    return render_template('cocktail_table.html')

@app.route('/clearIngr',methods=['POST'])
def clearIngr():
    global ingrList
    ingrList = []
    return render_template('cocktail_table.html')

@app.route("/cocktail",methods=['POST'])
def getCocktailByIngredient():
    global ingrList
    drinks = c.getDrinkBasedOnIngr(ingrList)
    return render_template('cocktail_table.html', drinks=drinks)

@app.route("/liquids")
def getLiquors():
    liquids = c.identifyLiquorInEach()
    return render_template('liquids.html',liquids=liquids)

if __name__ == '__main__':
    app.run(host='localhost',port=8080,debug=True)
