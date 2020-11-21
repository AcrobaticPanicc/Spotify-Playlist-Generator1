import json
import requests
from flask import render_template, Blueprint, request, redirect, url_for, session
from app.spotify_api.spotify_handler import SpotifyHandler

blueprint = Blueprint('app', __name__)


@blueprint.route("/not-found")
def not_found():
    return render_template('../error/templates/error/404.html')


@blueprint.route("/listen")
def listen():
    return render_template('../listen/templates/../your_playlist/templates/listen.html')


@blueprint.route("/refresh", methods=['GET', 'POST'])
def refresh_result():
    return redirect(url_for("app.your_playlist"))
