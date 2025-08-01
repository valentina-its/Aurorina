from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.controllers import sfida_controller
app.register_blueprint(sfida_controller.bp)

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tesoro.db'
    app.config['SECRET_KEY'] = 'chiave-segreta-tesoro'
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    return app