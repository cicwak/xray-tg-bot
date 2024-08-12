from pydantic import Field, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn = Field(alias='DATABASE_URL')
    REDIS_URL: RedisDsn = Field(alias="REDIS_URL")
    XRAY_DATABASE_URL: str = Field("xray/db/x-ui.db", alias="XRAY_DATABASE_URL")

    TG_BOT_TOKEN: str = Field(alias='TG_BOT_TOKEN')
    TG_BOT_URL: str = Field(default="https://t.me/vpnlowpricebot")

    DEBUG: bool = Field(default=False, alias='DEBUG')

    DEFAULT_TRAFFIC: int = 20 * 1024 * 1024 * 1024  # 20 ГБ


settings = Settings()
