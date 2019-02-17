import requests
import sys
import json


def main():
    """Main entry point for the script"""
    url = 'http://ws.audioscrobbler.com/2.0/'
    user = 'michaelnoteric'
    key = 'c551e97f9bd049453b719999e7bd3717'
    friends = get_friends(url, user, key)
    names = ['michaelnoteric'] + friends

    friend_stats = {}

    for name in names:
        top_artist, artists_listened = get_top_artist(url, name, key)
        top_album, albums_listened = get_top_album(url, name, key)
        top_track, tracks_listened = get_top_track(url, name, key)
        total_scrobbles = get_scrobble_count(url, name, key)
        friend_stats[name] = {
            'name': name,
            'top_artist': top_artist,
            'top_album': top_album,
            'top_track': top_track,
            'artists_listened': artists_listened,
            'albums_listened': albums_listened,
            'tracks_listened': tracks_listened,
            'total_scrobbles': total_scrobbles}

    print friend_stats


def get_friends(url, user, key):
    """Get list of friends"""
    friend_names = []

    friends = requests.get(
        url +
        '?method=user.getfriends&user=' +
        user +
        '&api_key=' +
        key +
        '&format=json').json()
    friends = friends['friends']['user']
    for f in friends:
        friend_names.append(f['name'].encode('Latin-1'))

    return friend_names


def get_top_artist(url, user, key):
    """Get top artist of a user"""
    artists = requests.get(
        url +
        '?method=user.gettopartists&user=' +
        user +
        '&api_key=' +
        key +
        '&format=json&limit=1').json()

    top_artist = artists['topartists']['artist'][0]['name']
    artists_listened = artists['topartists']['@attr']['total']

    return top_artist, artists_listened


def get_top_album(url, user, key):
    """Get top album of a user"""
    albums = requests.get(
        url +
        '?method=user.gettopalbums&user=' +
        user +
        '&api_key=' +
        key +
        '&format=json&limit=1').json()

    top_album = albums['topalbums']['album'][0]['name'] + \
        ' - ' + albums['topalbums']['album'][0]['artist']['name']
    albums_listened = albums['topalbums']['@attr']['total']

    return top_album, albums_listened


def get_top_track(url, user, key):
    """Get top track of a user"""
    tracks = requests.get(
        url +
        '?method=user.gettoptracks&user=' +
        user +
        '&api_key=' +
        key +
        '&format=json&limit=1').json()

    top_track = tracks['toptracks']['track'][0]['name'] + \
        ' - ' + tracks['toptracks']['track'][0]['artist']['name']
    tracks_listened = tracks['toptracks']['@attr']['total']

    return top_track, tracks_listened


def get_scrobble_count(url, user, key):
    """Get scrobble count of a user"""
    scrobbles = requests.get(
        url +
        '?method=user.getinfo&user=' +
        user +
        '&api_key=' +
        key +
        '&format=json').json()

    return scrobbles['user']['playcount']


if __name__ == '__main__':
    sys.exit(main())
