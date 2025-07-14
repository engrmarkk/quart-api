from . import bp
from src.logger import logger
from src.utils import returned_response
from src.cruds import get_current_user
from quart_jwt_extended import jwt_required

BASE_PREFIX = "users"


# get current user data
@bp.route(f"{BASE_PREFIX}/me")
@jwt_required
async def me():
    logger.info("Get current user data")
    current_user = await get_current_user()
    return returned_response(
        "Get current user data successful", 200, current_user.to_dict()
    )
