from flask import render_template, Blueprint

home_blueprint = Blueprint('home_bp', __name__, template_folder='templates')


@home_blueprint.route("/")
def home():
    return render_template('home.html')
