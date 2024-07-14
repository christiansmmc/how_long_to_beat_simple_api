import requests

from app.utils.common import (
    HOW_LONG_TO_BEAT_SEARCH_URL,
    filter_game_fields,
    get_default_headers,
    get_default_search_payload,
)


def fetch_game_data(game_name: str):
    payload = get_default_search_payload()
    payload["searchTerms"] = game_name.split()

    headers = get_default_headers()

    r = requests.post(HOW_LONG_TO_BEAT_SEARCH_URL, json=payload, headers=headers)
    data = r.json().get("data", None)

    return [filter_game_fields(game) for game in data]
