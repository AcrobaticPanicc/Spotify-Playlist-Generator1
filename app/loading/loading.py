from flask import render_template, Blueprint, request, redirect, url_for, session

loading_blueprint = Blueprint('loading_bp', __name__, template_folder='templates')


@loading_blueprint.route("/loading", methods=['GET', 'POST'])
def loading():
    if request.method == 'GET':
        return render_template('loading.html')
