import spotipy
import spotipy.util as util
import sys

if len(sys.argv) < 2:
    print("Please pass a username as the first argument:\n\npython app.py yourUserName\n")
    exit()

scope = 'user-library-read user-follow-modify'
token = util.prompt_for_user_token(sys.argv[1], scope)

artistIDs = []

if token:
    sp = spotipy.Spotify(auth=token)
    offset = 0
    results = sp.current_user_saved_tracks(offset=offset)
    print("Getting artists...")
    while len(results['items']) > 0:
        offset += len(results['items'])
        for item in results['items']:
            track = item['track']
            artist = track['artists']
            artistList = set([ x['id'] for x in artist ])
            for x in artistList:
                if not x in artistIDs:
                    artistIDs.append(x)
                    print(x)
            results = sp.current_user_saved_tracks(offset=offset)

    print("Following artists...")

    # do this individually, since the API aggressively rejects long URLs
    for artistID in artistIDs:
        sp.user_follow_artists(ids=[artistID])
        
else:
    print("Can't get token for that user...")
