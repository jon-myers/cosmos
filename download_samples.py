# FREESOUND_API_KEY = 'aeM1QyVnCipYahTON2P2k0GEv1OxB4aMGmbB0ThD'   
# import api key from .envrc file
# from dotenv import load_dotenv
# load_dotenv()
import os
FREESOUND_API_KEY = os.getenv("API_KEY")

import freesound
client = freesound.FreesoundClient()
client.set_token(FREESOUND_API_KEY, "token")
# get all most downloaded sounds less than .5 seconds long
page = 1
while page < 10:
    results = client.text_search(query="", filter="duration:[0 TO 0.5]", sort="downloads_desc", page=page)
    if not results:
        break
    # download the sounds
    for sound in results:
        sound.retrieve_preview(".", 'samples/' + str(sound.id) + ".wav")
        print(sound.name)
    page += 1

   