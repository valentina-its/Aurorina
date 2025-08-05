from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('sfide', __name__)

@bp.route('/PrimaSfida', methods=['GET', 'POST'])
def prima_sfida():
    if request.method == 'POST':
        risposta = request.form.get('risposta', '').lower().replace(' ', '')
        risposte_corrette = [
            'capitalesociale=attività-passività',
            'cs=a-p',
            'capitale sociale = attività - passività',
            'capitale=attività-passività',  
            'capitalesociale=attivita-passivita'
        ]
        
        if risposta in risposte_corrette:
            return redirect(url_for('sfide.seconda_sfida'))
        else:
            return render_template('primaSfida.html', 
                                 esito='&#x1F424; <strong>Non ci siamo!</strong> &#x1F424;<br>' 
                                       '<img src="/static/img/duck1.jpg" alt="Papera">')
    
    return render_template('primaSfida.html')

@bp.route('/SecondaSfida', methods=['GET', 'POST'])
def seconda_sfida():    
    return render_template('secondaSfida.html')

@bp.route('/TerzaSfida')
def terza_sfida():
    return render_template('terzaSfida.html')

@bp.route('/TerzaSfida2', methods=['GET', 'POST'])
def terza_sfida_2():
    if request.method == 'POST':
        risposta = request.form.get('risposta', '').lower().strip()
        soluzione = 'flag{TerzaSfida2}'
        
        if risposta == soluzione:
            return redirect(url_for('sfide.quarta_sfida'))
        else:
            return render_template('terzaSfida2.html', esito='Risposta errata. Riprova!')
    
    return render_template('terzaSfida2.html')

@bp.route('/QuartaSfida')
def quarta_sfida():
    return render_template('quartaSfida.html')