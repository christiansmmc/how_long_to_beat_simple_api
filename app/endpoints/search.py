from fastapi import APIRouter, HTTPException
from app.services.how_long_to_beat import fetch_game_data

router = APIRouter()


@router.get("/")
def search_game(game_name: str = ""):
    try:
        response = fetch_game_data(game_name)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# STILL NEEDS SEARCH WITHOUT GAME NAME TO GET SOME DEFAULT GAMES
#
# @router.get("/hltb-api")
# def search_game_hltb_api(game_name: str = ""):
#     try:
#         response = fetch_game_data_hltb_api(game_name)
#         return response
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
