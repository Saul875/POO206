from flask import Flask
from config import Config
from extensions import mysql 
from controllers.albumController import albumsBP

app = Flask(__name__)
app.config.from_object(Config)
mysql.init_app(app)

# Registro del Blueprint
app.register_blueprint(albumsBP)

@app.errorhandler(404)
def pagNoE(e):
    return 'La princesa está en otro castillo', 404

if __name__ == '__main__':
    app.run(port=3000, debug=True)
