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
    if request.method == 'POST':
        risposta = request.form.get('risposta')
        soluzione = 'flag{HaiRisoltoLEnigma}'
        
        if risposta and risposta.strip() == soluzione:
            esito = 'Complimenti! Hai risolto la seconda sfida.'
        else:
            esito = 'Risposta errata. Riprova!'
            
        return render_template('secondaSfida.html', esito=esito)
    
    return render_template('secondaSfida.html')

@bp.route('/TerzaSfida', methods=['GET', 'POST'])
def terza_sfida():
    if request.method == 'POST':
        risposta = request.form.get('risposta', '').lower().strip()
        # Definisci qui la risposta corretta per la terza sfida
        soluzione = 'risposta_corretta_terza_sfida'
        
        if risposta == soluzione:
            # Reindirizza alla pagina successiva o mostra un messaggio di successo
            return redirect(url_for('duck.show_duck_right'))
        else:
            # Mostra un messaggio di errore
            return render_template('terzaSfida.html', esito='Risposta errata. Riprova!')
    
    return render_template('terzaSfida.html')