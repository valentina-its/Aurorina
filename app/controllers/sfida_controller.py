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

@bp.route('/QuartaSfida')
def quarta_sfida():
    return render_template('quartaSfida.html')

@bp.route('/QuintaSfida', methods=['GET', 'POST'])
def quinta_sfida():
    if request.method == 'POST':
        codice = request.form.get('codice', '').strip()
        soluzione = 'piazza conte rosso'
        
        if codice == soluzione:
            return redirect(url_for('sfide.sesta_sfida'))
        else:
            return render_template('quintaSfida.html', 
                                 esito='&#x2728; <strong>Non ti hanno detto questo le stelle...<br>Ascolta meglio il loro sussurro.</strong> &#x2728;<br>'
                                    )
    
    return render_template('quintaSfida.html')

@bp.route('/SestaSfida')
def sesta_sfida():
    return render_template('sestaSfida.html')
    