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

@app.route('/sobre-nos')  #api_key=YOUR_GOOGLE_MAPS_API_KEY)
def sobre_nos():
    return render_template('sobre-nos.html')

#@app.route('/login')
#def membro_login():
#    return render_template('user_login.html')

#@app.route('/cadastro')
#def membro_cadastro():
#    return render_template('cadastro.html')

#@app.route('/perfil')
#def perfil():
#    return render_template*('perfil_')
