from flask import Flask

from src.routes import main

app = Flask(__name__, template_folder='src/templates', static_folder='src/static')
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
