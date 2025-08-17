from flask import Blueprint, render_template
import random

bp = Blueprint('duck', __name__)

DUCKS = [
    'duck1.jpg', 'duck2.jpg', 'duck3.jpg', 'duck4.jpg', 'duck5.jpg', 
    'duck6.jpg', 'duck7.jpg', 'duck8.jpg', 'duck13.jpg', 'duck14.jpg', 
    'duck15.jpg', 'duck16.jpg', 'duck17.jpg'
]

@bp.route('/randomDuck')
def show_random_duck():
    duck_img = random.choice(DUCKS)
    return render_template('randomDuck.html', duckImg=duck_img)

@bp.route('/duckRight')
def show_duck_right():
    return render_template('duckRight.html')

@bp.route('/duckIndizio')
def show_duck_indizio():
    return render_template('duckIndizio.html')  # Assicurati che il nome file corrisponda esattamente