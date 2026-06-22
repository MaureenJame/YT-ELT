import requests
import json


import os
from dotenv import load_dotenv

#env_path = r"C:\Users\maureen.kerubo\YT-ELT\.env"
#load_dotenv(env_path)

#load_dotenv(dotenv_path=r"C:\Users\maureen.kerubo\YT-ELT\.env")
#load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))
#API_KEY="AIzaSyCBFTXUhA7UGTaGZxzxr1hO_V--UJDzuq0"
API_KEY= os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not found in .env file")
CHANNEL_HANDLE="MrBeast"
def get_playlist_id():
  try:
   url=f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"
   response=requests.get(url)
   response.raise_for_status()
##print(response)
   data=response.json()
   ##print(json.dumps(data,indent=4))

   channel_items=data['items'][0]
   channel_playlistId= channel_items['contentDetails']['relatedPlaylists']['uploads']
   print(channel_playlistId)   
   return channel_playlistId
  except requests.exceptions.RequestException as e :
    raise e 
if __name__=="__main__":
  #print("Get playlist will be executed")
  get_playlist_id()
  #print(API_KEY)
#else:
 # print ("Get playlist_id wont be executed")
  
      
