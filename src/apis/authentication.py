from . import bp
from quart import request
from src.logger import logger
from src.cruds import get_user_by_username, create_user
from src.utils import generate_token, returned_response

BASE_PREFIX = "auth"


@bp.post(f"{BASE_PREFIX}/login")
async def login():
    try:
        logger.info("Login")
        data = await request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not any([username, password]):
            return returned_response("Missing username or password", 400)

        if len(password) < 6:
            return returned_response("Password too short", 400)

        user = await get_user_by_username(username)
        logger.info(f"User: {user}")

        if not user:
            return returned_response("User does not exist", 400)

        if not user.verify_password(password):
            return returned_response("Invalid password", 400)

        access_token = generate_token(user.id)

        return returned_response(
            "Login successful", 200, {"access_token": access_token}
        )

    except Exception as e:
        logger.error(e)
        return returned_response("Network Error", 500)


# register
@bp.post(f"{BASE_PREFIX}/register")
async def register():
    try:
        logger.info("Register")
        data = await request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not any([username, password]):
            return returned_response("Missing username or password", 400)

        if len(password) < 6:
            return returned_response("Password too short", 400)

        user = await get_user_by_username(username)

        if user:
            return returned_response("User already exists", 400)

        await create_user(username, password)

        return returned_response("Registration successful", 200)

    except Exception as e:
        logger.error(e)
        return returned_response("Network Error", 500)
