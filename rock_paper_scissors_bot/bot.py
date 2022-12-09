# https://stepik.org/lesson/759407/step/6?unit=761423

import asyncio
import logging


from aiogram import Bot, Dispatcher

from config_data.config import load_config
from handlers.user_handlers import register_user_handlers
from handlers.other_handlers import register_other_handlers


logger = logging.getLogger(__name__)


def register_all_hadlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)
    register_other_handlers(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
            u'[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')

    config = load_config()

    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot)

    register_all_hadlers(dp)

    try:
        # If need to skip updates when bot was offline:
        # await dp.skip_updates()
        await dp.start_polling()
    finally:
        await bot.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped!')
