import requests

from app.utils.common import (
    HOW_LONG_TO_BEAT_SEARCH_URL,
    filter_game_fields,
    get_default_headers,
    get_default_search_payload,
    send_website_request_getcode,
)


def fetch_game_data(game_name: str):
    payload = get_default_search_payload()
    payload["searchTerms"] = game_name.split()

    headers = get_default_headers()

    api_key_result = send_website_request_getcode(False)
    if api_key_result is None:
        api_key_result = send_website_request_getcode(True)

    search_url_with_key = HOW_LONG_TO_BEAT_SEARCH_URL + "/" + api_key_result

    r = requests.post(search_url_with_key, json=payload, headers=headers)
    data = r.json().get("data", None)

    return [filter_game_fields(game) for game in data]


# STILL NEEDS SEARCH WITHOUT GAME NAME TO GET SOME DEFAULT GAMES
#
# def fetch_game_data_hltb_api(game_name: str):
#     hltb_result = HowLongToBeat().search(game_name)
#     return [filter_game_fields_hltb_api(game) for game in hltb_result]
