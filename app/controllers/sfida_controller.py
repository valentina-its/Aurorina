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
            'capitale=attività-passività'
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
    if request.method == 'POST':
        risposta = request.form.get('risposta')
        soluzione = 'flag{HaiRisoltoLEnigma}'
        
        if risposta and risposta.strip() == soluzione:
            esito = 'Complimenti! Hai risolto la seconda sfida.'
        else:
            esito = 'Risposta errata. Riprova!'
            
        return render_template('secondaSfida.html', esito=esito)
    
    return render_template('secondaSfida.html')