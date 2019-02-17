import requests
import sys

def main():
    """Main entry point for the script"""
    url = 'http://ws.audioscrobbler.com/2.0/'
    user = 'michaelnoteric'
    key = 'c551e97f9bd049453b719999e7bd3717'
    friends = get_friends(url, user, key)

def get_friends(url, user, key):
    """Get list of friends"""
    r = requests.get(url + '?method=user.getfriends&user=' + user + '&api_key=' + key)
    #r = requests.get('http://ws.audioscrobbler.com/2.0/?method=user.getfriends&user=michaelnoteric&api_key=c551e97f9bd049453b719999e7bd3717')
    print r.text


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
