from flask import render_template, Blueprint, request, session
from app.spotify_api.spotify_handler import SpotifyHandler

select_blueprint = Blueprint('select_bp', __name__, template_folder='templates')
spotify_handler = SpotifyHandler()


@select_blueprint.route("/select_tracks", methods=['GET', 'POST'])
def select_tracks():
    authorization_header = session['authorization_header']

    def extract_letters(string):
        return ''.join([letter for letter in string if not letter.isdigit()])

    if request.method == 'GET':
        # -------- Get user's name, id, and set session --------
        profile_data = spotify_handler.get_user_profile_data(authorization_header)
        user_display_name, user_id = profile_data['display_name'], profile_data['id']
        session['user_id'], session['user_display_name'] = user_id, user_display_name

        # -------- Get user playlist data --------
        playlist_data = spotify_handler.get_user_playlist_data(authorization_header, user_id)

        return render_template('select_tracks.html',
                               user_display_name=user_display_name,
                               playlists_data=playlist_data,
                               func=extract_letters)

    return render_template('select_tracks.html')
