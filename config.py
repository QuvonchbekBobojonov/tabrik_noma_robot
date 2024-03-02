from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("BOT_TOKEN")

CHANNELS = [
    # ('https://t.me/Urganch_lenta_N1', '@Urganch_lenta_N1'),
    ('https://t.me/QuvonchbekBobojonov', '@QuvonchbekBobojonov')
]

