import requests

FREESOUND_API_KEY = 'aeM1QyVnCipYahTON2P2k0GEv1OxB4aMGmbB0ThD'
url = 'https://freesound.org/apiv2/search/text/'

params = {
    'query': '',
    'filter': 'duration:[0 TO 0.5]',
    'sort': 'downloads_desc',
    'token': FREESOUND_API_KEY
}

response = requests.get(url, params=params)

results = response.json()['results']

for result in results:
    id = result['id']
    # download the sound
    url = 'https://freesound.org/apiv2/sounds/{}/download/'.format(id)
    params = {'token': FREESOUND_API_KEY}
    response = requests.get(url, params=params)
    # save the sound
    with open('samples/{}.wav'.format(id), 'wb') as f:
        f.write(response.content)
    

   