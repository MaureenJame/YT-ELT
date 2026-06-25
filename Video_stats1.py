import requests
import os
from dotenv import load_dotenv

# ✅ Load .env FIRST
load_dotenv(dotenv_path=r"C:\Users\maureen.kerubo\YT-ELT\.env")

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found in .env file")

CHANNEL_HANDLE = "MrBeast"
MAX_RESULTS = 50


def get_playlist_id():
    try:
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if not data.get("items"):
            raise ValueError("No channel data returned")

        playlist_id = data['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        print("Playlist ID:", playlist_id)
        return playlist_id

    except requests.exceptions.RequestException as e:
        print("Request error:", e)
        raise


if __name__ == "__main__":
    playlist_id = get_playlist_id()
