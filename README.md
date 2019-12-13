# Fix-Spotify-Artists
A 2018-2019 Spotify update completely removed the very useful feature of listing your music collection by artist alphabetically.  This is a workaround until they come to their senses.

According to the Spotify support team and forum moderators, you can only filter your artists alphabetically for the artists you follow.  Thus by following every artist you have a saved track for, we can recover this feature.

# Setup
## App Setup
Follow the instructions for establishing a developer account [here](https://developer.spotify.com/documentation/web-api/quick-start/)

You need to name your app, and write down the client ID and client secret somewhere safe.  You also need to specify a callback URL, simply use ```http://localhost/```

## Environment
You should have Python 3 installed and access to Python on the command line.

Before running the script, you need to modify env.sh to include the client ID, client secret, and URL that you set suring the application setup.  Once you have done so, add them to your environment variables:
```shell
source env.sh
```

## Code
Download and install the Python API for Spotify [here](https://github.com/plamere/spotipy).  Note that the pip version is out of date; if you want to install via pip, point directly to the repository:

```pip install git+https://github.com/plamere/spotipy.git --upgrade --user```

# Running the Application
You need to acquire a token to make changes.  As this is a one-off script, we can just request it once rather than keep it locally to remain logged in.

The first time you run the application, it will open your default browser so you can log in to your Spotify account.  This process will generate a token, and you will be redirected to the URL you provided for your application.  Nothing will display, but you will need to copy and paste the address of the page you were redirected to into the command line window.  Make sure you have already added your client information to the environment variables with env.sh.
```shell
python app.py <username>
```

