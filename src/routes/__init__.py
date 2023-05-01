from flask import Blueprint

main = Blueprint('main', __name__)

from src.routes import index
from src.routes import beautiful_page
