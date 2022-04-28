from fastapi import HTTPException


def bad_request():
    return HTTPException(status_code=400)


def not_found(model, match_data):
    return HTTPException(
        status_code=404, detail=f"{model}({match_data}) is Not Exists in DB"
    )

def user_bad_input():
    return HTTPException(status_code=422)
