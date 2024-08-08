import requests
from howlongtobeatpy import HowLongToBeat

from app.utils.common import (
    HOW_LONG_TO_BEAT_SEARCH_URL,
    filter_game_fields,
    filter_game_fields_hltb_api,
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


def fetch_game_data_hltb_api(game_name: str):
    hltb_result = HowLongToBeat().search(game_name)
    return [filter_game_fields_hltb_api(game) for game in hltb_result]
