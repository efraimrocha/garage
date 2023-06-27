from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/fotos')
def fotos():
    return render_template('fotos.html')

@app.route('/portifolio')
def portifolio():
    return render_template('portifolio.html')

@app.route('/rider')
def rider():
    return render_template('rider.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')
    
    