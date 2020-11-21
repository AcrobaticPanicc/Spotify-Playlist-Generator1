import json
import requests
from flask import render_template, Blueprint, request, redirect, url_for, session

result_blueprint = Blueprint('result_bp', __name__, template_folder='templates')


@result_blueprint.route("/your-playlist", methods=['GET', 'POST'])
def your_playlist():
    authorization_header = session['authorization_header']
    fine_tune_vals = json.loads(f"[{request.form.get('fine-tune-values')}]")
    fine_tune_vals = [{val['key']: val['val'] for val in fine_tune_vals}][0]

    if request.method == 'POST':
        params = {
            'seed_tracks': session['selected_tracks'],
            'danceability': float(fine_tune_vals['danceability']) / 10,
            'energy': float(fine_tune_vals['energy']) / 10,
            'loudness': -60 + (float(fine_tune_vals['loudness']) - 1) * 60 / 9,
            'popularity': int(fine_tune_vals['popularity']) * 10
        }

        get_reccomended_url = f"https://api.spotify.com/v1/recommendations?limit={25}"
        response = requests.get(get_reccomended_url,
                                headers=authorization_header,
                                params=params).text
        tracks = list(json.loads(response)['tracks'])
        tracks_uri = [track['uri'] for track in tracks]
        session['tracks_uri'] = tracks_uri

        return render_template('result.html', data=tracks)

    return redirect(url_for('not_found'))


@result_blueprint.route("/save-playlist", methods=['GET', 'POST'])
def save_playlist():
    authorization_header = session['authorization_header']
    user_id = session['user_id']

    playlist_name = request.form.get('playlist_name')
    playlist_data = json.dumps({
        "name": playlist_name,
        "description": "Recommended songs",
        "public": True
    })

    create_playlist_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

    response = requests.post(create_playlist_url,
                             headers=authorization_header,
                             data=playlist_data).text

    playlist_id = json.loads(response)['id']

    tracks_uri = session['tracks_uri']
    tracks_data = json.dumps({
        "uris": tracks_uri,
    })

    add_items_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    response = requests.post(add_items_url, headers=authorization_header, data=tracks_data).text

    return render_template('listen.html', playlist_id=playlist_id)
