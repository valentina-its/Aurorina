# Aurorina - Caccia al Tesoro Interattiva

## Descrizione del Progetto
**Aurorina** è un'applicazione web interattiva che implementa una caccia al tesoro personalizzata. Il progetto è stato sviluppato come regalo speciale, combinando elementi digitali e fisici per creare un'esperienza di gioco ibrida.  
L'utente deve risolvere una serie di indovinelli e sfide, scansionare codici QR nel mondo reale e seguire indizi per progredire nell'avventura.

## Caratteristiche Principali
- **Autenticazione Personalizzata**: Sistema di login con credenziali specifiche  
- **Sfide Progressive**: Tre livelli di sfide con indovinelli da risolvere  
- **Integrazione con il Mondo Reale**: Utilizzo di codici QR da scansionare in luoghi fisici  
- **Feedback Interattivo**: Messaggi personalizzati e immagini di papere che guidano l'utente  
- **Design Responsive**: Interfaccia ottimizzata per dispositivi mobili  

## Struttura del Progetto

    Aurorina/
    ├── app/ # Directory principale dell'applicazione
    │ ├── init.py # Inizializzazione dell'app Flask
    │ ├── controllers/ # Controller per gestire le richieste HTTP
    │ │ ├── duck_controller.py # Gestisce le pagine relative alle papere
    │ │ ├── sfida_controller.py # Gestisce le sfide e gli indovinelli
    │ │ └── tesoro_controller.py # Gestisce l'autenticazione e la home
    │ ├── models/ # Modelli di dati
    │ │ └── user.py # Modello per gli utenti
    │ ├── services/ # Servizi per la logica di business
    │ │ └── user_service.py # Servizio per l'autenticazione
    │ ├── static/ # File statici (CSS, immagini)
    │ │ ├── css/ # Fogli di stile
    │ │ └── img/ # Immagini (papere, ecc.)
    │ └── templates/ # Template HTML
    │ ├── DuckIndizio.html # Pagina con indizi
    │ ├── duckRight.html # Pagina per QR code corretto
    │ ├── index.html # Pagina iniziale
    │ ├── inizio.html # Pagina di login
    │ ├── messaggioBar.html # Pagina con messaggio specifico
    │ ├── primaSfida.html # Prima sfida
    │ ├── randomDuck.html # Pagina con papera casuale
    │ ├── secondaSfida.html # Seconda sfida
    │ └── terzaSfida.html # Terza sfida
    ├── instance/ # Database SQLite
    │ └── tesoro.db # Database dell'applicazione
    ├── requirements.txt # Dipendenze Python
    └── run.py # Script per avviare l'applicazione


## Tecnologie Utilizzate
- **Backend**: Flask 3.0.0 (framework Python per applicazioni web)  
- **Database**: SQLite con Flask-SQLAlchemy 3.1.1  
- **Autenticazione**: Sistema personalizzato  
- **Frontend**: HTML, CSS  
- **Deployment**: Configurato per deployment su Vercel  

## Flusso dell'Applicazione
1. **Pagina Iniziale**: Presentazione della caccia al tesoro  
2. **Login**: Autenticazione con credenziali specifiche  
   - username: `???`  
   - password: `BuonCompleanno!`  
3. **Prima Sfida**: Indovinello sulla formula del capitale sociale  
4. **Seconda Sfida**: Indizio che porta l'utente a cercare un QR code in un luogo fisico  
5. **Scansione QR Code**:  
   - QR code **errati**: Mostrano una papera casuale con un messaggio  
   - QR code **corretto**: Porta alla terza sfida  
6. **Terza Sfida**: Ultimo indovinello da risolvere  

## Requisiti di Sistema
- Python 3.x  
- Flask e dipendenze (vedi `requirements.txt`)  
- Browser web moderno  
- Dispositivo mobile con fotocamera per scansionare i QR code  

## Installazione e Avvio
1. Clona il repository:
   ```bash
   git clone [URL_REPOSITORY]
   ```
   ```bash
   cd Aurorina
    ```
2. Crea e attiva un ambiente virtuale (opzionale ma consigliato):

    ```bash
    python -m venv venv
    ```
    ```bash
    venv\Scripts\activate      # Windows
    ```
    ```bash
    source venv/bin/activate  # Linux/Mac
    ```
3. Installa le dipendenze:
    ``` bash
    pip install -r requirements.txt
    ```
4. Avvia l'applicazione:
    ```bash
    python run.py
    ```
5. Accedi all'applicazione tramite browser:
    ``` bash
    http://localhost:5000
    ```
## Personalizzazione
L'applicazione è stata progettata per essere facilmente personalizzabile attraverso diversi componenti:

### Modifica dei Contenuti
- **Indovinelli**: Modifica il file `sfida_controller.py` per cambiare le sfide
- **Immagini**: Aggiungi o sostituisci le immagini delle papere nella directory `static/img/`
- **Testi**: Personalizza messaggi e indizi nei file template HTML

### Note per lo Sviluppo
- Modalità debug attiva per facilitare lo sviluppo e il testing
- Database SQLite con inizializzazione automatica all'avvio
- Architettura modulare che supporta l'aggiunta di nuove funzionalità

### Licenza e Attribuzione
Questo progetto è stato sviluppato come regalo personale e non è destinato all'uso commerciale.

_Creato con ❤️ per Aurorina_
