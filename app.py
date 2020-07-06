from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps

#Cria o objeto  da aplicação
app = Flask(__name__)

app.secret_key = 'teste'

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Você precisa estar logado para acessar a página.')
            return redirect(url_for('login')) 
    return wrap

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

""" @app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    #verifica se a requisicao eh do tipo post
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Usuário ou senha inválidos. Por favor tente novamente.'
        else:
            session['logged_in'] = True
            flash('Você logou!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error) """

#Inicia o servidor 
if __name__ == '__main__':
    app.run(debug=True)
