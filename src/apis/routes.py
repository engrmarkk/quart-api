from . import bp
from src.logger import logger


@bp.route("/")
async def hello():
    logger.info("Hello, Mark! Logger")
    return "Hello, Mark!"
