import json
import requests


class SpotifyHandler:
    # Spotify API URLS
    API_VERSION = "v1"
    SPOTIFY_API_BASE_URL = "https://api.spotify.com"
    SPOTIFY_API_URL = f"{SPOTIFY_API_BASE_URL}/{API_VERSION}"

    def get_user_profile_data(self, auth_header):
        user_profile_api_endpoint = f"{self.SPOTIFY_API_URL}/me"
        profile_data = requests.get(user_profile_api_endpoint, headers=auth_header).text
        return json.loads(profile_data)

    def get_user_playlist_data(self, auth_header, user_id):
        """
        :return: list of dictionaries with playlist information
        """
        playlist_api_endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"
        playlists = json.loads(requests.get(playlist_api_endpoint, headers=auth_header).text)
        playlists = playlists['items']

        playlist_data = []

        for playlist in playlists:
            playlist_data.append({
                'playlist_name': playlist['name'],
                'playlist_url': playlist['external_urls']['spotify'],
                'playlist_img_url': playlist['images'][0]['url'],
                'playlist_tracks_url': playlist['tracks']['href'],
                'playlist_id': playlist['id'],
                'playlist_tracks': self._get_playlist_tracks(auth_header, playlist['id'])
            })
        return playlist_data

    @staticmethod
    def _get_playlist_tracks(auth_header, playlist_id):
        """
        :return: list of dictionaries with track information
        """
        playlist_api_endpoint = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
        tracks = json.loads(requests.get(playlist_api_endpoint, headers=auth_header).text)['items']

        return [
            {
                'track_artist': track['track']['artists'][0]['name'],
                'track_name': track['track']['name'],
                'track_image': track['track']['album']['images'][0]['url'],
                'track_url': track['track']['external_urls']['spotify'],
                'track_id': track['track']['id']
            } for track in tracks
        ]
