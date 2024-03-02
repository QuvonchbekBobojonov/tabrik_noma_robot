from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("BOT_TOKEN")

CHANNELS = [
    ('https://t.me/QuvonchbekBobojonov', '@QuvonchbekBobojonov')
    ('https://t.me/yangibozorli_volontyor', '@yangibozorli_volontyor')
]

