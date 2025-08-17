from flask import Flask

def create_app():
    app = Flask(__name__,
                 template_folder='app/templates')
    
    # Registra i blueprint
    from .controllers import tesoro_controller, sfida_controller, duck_controller
    app.register_blueprint(tesoro_controller.bp)
    app.register_blueprint(sfida_controller.bp)
    app.register_blueprint(duck_controller.bp)
    
    return app