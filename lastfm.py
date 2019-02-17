import requests
import sys
import json

def main():
    """Main entry point for the script"""
    url = 'http://ws.audioscrobbler.com/2.0/'
    user = 'michaelnoteric'
    key = 'c551e97f9bd049453b719999e7bd3717'
    friends = get_friends(url, user, key)

def get_friends(url, user, key):
    """Get list of friends"""
    friend_names = []

    friends = requests.get(url + '?method=user.getfriends&user=' + user + '&api_key=' + key + '&format=json').json()
    friends = friends['friends']['user']
    for f in friends:
        friend_names.append(f['name'].encode('Latin-1'))

    return friend_names

def get_top_artits():
    """Get top artists and artist count"""
    pass

def get_top_albums():
    """Get top albums and album count"""
    pass

def get_top_tracks():
    """Get top tracks and track count"""
    pass



if __name__ == '__main__':
    sys.exit(main())
