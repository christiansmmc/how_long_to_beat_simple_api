import copy
from typing import Dict
from fake_useragent import UserAgent

HOW_LONG_TO_BEAT_BASE_URL = "https://howlongtobeat.com"
HOW_LONG_TO_BEAT_SEARCH_URL = (
    f"{HOW_LONG_TO_BEAT_BASE_URL}/api/search/4b4cbe570602c88660f7df8ea0cb6b6e"
)
HOW_LONG_TO_BEAT_IMAGES_URL = f"{HOW_LONG_TO_BEAT_BASE_URL}/games"

HOW_LONG_TO_BEAT_SEARCH_DEFAULT_PAYLOAD = {
    "searchType": "games",
    "searchTerms": [],
    "searchPage": 1,
    "size": 20,
    "searchOptions": {
        "games": {
            "userId": 0,
            "platform": "",
            "sortCategory": "popular",
            "rangeCategory": "main",
            "rangeTime": {"min": 0, "max": 0},
            "gameplay": {"perspective": "", "flow": "", "genre": ""},
            "modifier": "",
        },
        "users": {"sortCategory": "postcount"},
        "filter": "",
        "sort": 0,
        "randomizer": 0,
    },
}


def get_hours_from_seconds(seconds: str):
    hours = int(seconds) / 3600
    return round(hours)


def filter_game_fields(game_data: Dict):
    return {
        "game_id": game_data.get("game_id"),
        "game_name": game_data.get("game_name"),
        "game_image": f'{HOW_LONG_TO_BEAT_IMAGES_URL}/{game_data.get("game_image")}',
        "review_score": game_data.get("review_score"),
        "main_story_total_time": get_hours_from_seconds(game_data.get("comp_main")),
        "main_plus_sides_total_time": get_hours_from_seconds(
            game_data.get("comp_plus")
        ),
        "main_complete_total_time": get_hours_from_seconds(game_data.get("comp_100")),
        "main_all_total_time": get_hours_from_seconds(game_data.get("comp_all")),
    }


def filter_game_fields_hltb_api(game_data):
    return {
        "game_id": game_data.game_id,
        "game_name": game_data.game_name,
        "game_image": game_data.game_image_url,
        "review_score": game_data.review_score,
        "main_story_total_time": get_hours_from_seconds(game_data.main_story),
        "main_plus_sides_total_time": get_hours_from_seconds(game_data.main_extra),
        "main_complete_total_time": get_hours_from_seconds(game_data.completionist),
        "main_all_total_time": get_hours_from_seconds(game_data.all_styles),
    }


def get_default_headers():
    ua = UserAgent()

    return {
        "User-Agent": ua.random,
        "content-type": "application/json",
        "origin": "https://howlongtobeat.com",
        "referer": "https://howlongtobeat.com",
    }


def get_default_search_payload():
    return copy.deepcopy(HOW_LONG_TO_BEAT_SEARCH_DEFAULT_PAYLOAD)
