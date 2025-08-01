from flask import Blueprint, render_template

bp = Blueprint('tesoro', __name__)

@bp.route('/')
def get_tesoro_page():
    return render_template('index.html')