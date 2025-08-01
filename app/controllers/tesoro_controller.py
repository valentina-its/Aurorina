from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('tesoro', __name__)

@bp.route('/inizio', methods=['GET', 'POST'])
def inizio():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'BadGirl' and password == 'BuonCompleanno!':
            return redirect(url_for('sfide.prima_sfida'))
        else:
            return render_template('inizio.html', errorMessage='Faccia da schiaffi non ti ricordi come ti ho salvata?? PS. non è "Faccia da schiaffi"')
    
    return render_template('inizio.html')

@bp.route('/')
def index():
    return render_template('index.html')