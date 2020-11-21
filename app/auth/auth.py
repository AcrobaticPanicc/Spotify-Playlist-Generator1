import os
from flask import Blueprint, request, redirect, url_for, session

from app.spotify_api.spotify_client import SpotifyClient

auth_blueprint = Blueprint('auth_bp', __name__)

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

spotify_client = SpotifyClient(client_id, client_secret, port=8002)


@auth_blueprint.route("/login", methods=['POST', 'GET'])
def login():
    """
    redirect to Spotify's log in page
    """
    auth_url = spotify_client.get_auth_url()
    return redirect(auth_url)


@auth_blueprint.route("/callback/q")
def callback():
    """
    set the session's authorization header
    """
    auth_token = request.args['code']
    spotify_client.get_authorization(auth_token)
    authorization_header = spotify_client.authorization_header
    session['authorization_header'] = authorization_header
    return redirect(url_for("loading_bp.loading"))
