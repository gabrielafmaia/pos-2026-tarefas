from urllib import response

from flask import Flask, redirect, url_for, session, request, jsonify, render_template
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)

oauth.register(
    name='suap',
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    api_base_url='https://suap.ifrn.edu.br/api/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://suap.ifrn.edu.br/o/token/',
    authorize_url='https://suap.ifrn.edu.br/o/authorize/',
    fetch_token=lambda: session.get('suap_token')
)

def get_user():
    return oauth.suap.get('rh/meus-dados').json()
@app.route('/')
def index():
    if 'suap_token' in session:
        meus_dados = oauth.suap.get('rh/meus-dados')
        return render_template('user.html', user_data=meus_dados.json())
    else:
        return render_template('index.html')

@app.route('/meu-boletim/<int:ano>/<int:periodo>')
def boletim(ano, periodo):
    if 'suap_token' in session:
        boletim_data = oauth.suap.get(f'ensino/meu-boletim/{ano}/{periodo}/')
        user = get_user()
        return render_template('boletim.html', boletim_data=boletim_data.json()["results"], user_data=user)
    else:
        return redirect(url_for('login'))

@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    print(redirect_uri)
    return oauth.suap.authorize_redirect(redirect_uri)


@app.route('/logout')
def logout():
    session.pop('suap_token', None)
    return redirect(url_for('index'))


@app.route('/login/authorized')
def auth():
    token = oauth.suap.authorize_access_token()
    session['suap_token'] = token
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()