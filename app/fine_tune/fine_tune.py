from flask import render_template, Blueprint, request, redirect, url_for, session

fine_tune_blueprint = Blueprint('fine_tune_bp', __name__, template_folder='templates')


@fine_tune_blueprint.route("/fine_tune", methods=['GET', 'POST'])
def fine_tune():
    selected_tracks = request.form.get('selected_tracks').split(',')
    session['selected_tracks'] = selected_tracks
    return render_template('fine_tune.html')
