from dataclasses import dataclass 
from environs import Env  

@dataclass 
class DataBaseConfig:
    database: str 
    db_host: str 
    db_user: str 
    db_password: str

@dataclass
class TgBot:
    token: str 
    admin_ids: list[int]

@dataclass 
class Config:
    tg_bot: TgBot 
    db: DataBaseConfig 

env: Env = Env()

env.read_env()

config = Config(tg_bot=(TgBot(token=env("BOT_TOKEN"),admin_ids=list(map(int, env.list("ADMIN_IDS"))))), db=DataBaseConfig
                (database=env("DATABASE"),
                db_host=env("DB_HOST"),
                db_user=env("DB_USER"),
                db_password=env("DB_PASSWORD")))

print(config.db.db_password)