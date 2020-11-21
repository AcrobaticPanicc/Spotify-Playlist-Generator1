from flask import Blueprint, request, redirect, url_for, session, render_template

error_blueprint = Blueprint('error_blueprint', __name__)


# @error_blueprint.app_errorhandler(404)
# def handle_404(err):
#     return render_template('404.html'), 404
#

# @error_blueprint.app_errorhandler(500)
# def handle_500(err):
#     return render_template('500.html'), 500
