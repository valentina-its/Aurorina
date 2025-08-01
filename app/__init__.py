from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tesoro.db'
    app.config['SECRET_KEY'] = 'chiave-segreta-tesoro'
    
    db.init_app(app)
    
    from app.controllers import sfida_controller, duck_controller, tesoro_controller
    app.register_blueprint(sfida_controller.bp)
    app.register_blueprint(duck_controller.bp)
    app.register_blueprint(tesoro_controller.bp)
    
    with app.app_context():
        db.create_all()
    
    return app