import re
from datetime import datetime

import requests

# Endpoint de personagens
CHARACTER_ENDPOINT = "https://rickandmortyapi.com/api/character"

# Padrão de formatação de string de data de Episódio
# (x, y)
# Onde x é como a API envia
#    E y é como eu exibo
EPISODE_DATE_FORMAT = ("%B %d, %Y", "%d/%m/%Y")


def get_all_characters():
    response = requests.get(CHARACTER_ENDPOINT)
    data = response.json()

    while data['info']['next'] is not None:
        yield from data['results']
        data = requests.get(data['info']['next']).json()


def get_episodes_for_character(character):
    episode_url_list = character['episode']
    (in_format, out_format) = EPISODE_DATE_FORMAT

    for ep_url in episode_url_list:
        data = requests.get(ep_url).json()

        yield {
            "name": data['name'],
            "release": datetime.strptime(data['air_date'], in_format)
                               .strftime(out_format),
            "episode": data['episode']
        }
