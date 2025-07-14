from quart import Quart
from src.apis import bp
from src.database.db import Base, engine
from src.extensions import jwt
from src.database.models import User
from src.database.db import async_session
from src.configs import config

app = Quart(__name__)


def create_app(config_name="dev"):
    app.config.from_object(config[config_name])

    jwt.init_app(app)

    @app.before_serving
    async def init_db():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        await engine.dispose()

    app.register_blueprint(bp, url_prefix="/api/v1")
    return app
