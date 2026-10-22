import os
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

SOURCE_CHANNELS = [
    "almaskhodro4",
    "Almaskhodro1",
]

TARGET_CHANNEL = "erfantayebii"
SELLER_NAME = "عرفان طیبی"
PHONE_NUMBER = "09122729582"

PRICE_INCREASE_TOMAN = 50_000_000
CHECK_INTERVAL_HOURS = 1


def main():
    logging.info("ربات خودرو آماده راه‌اندازی است.")
    logging.info("نام فروشنده: %s", SELLER_NAME)
    logging.info("شماره تماس: %s", PHONE_NUMBER)
    logging.info("کانال مقصد: %s", TARGET_CHANNEL)
    logging.info("افزایش قیمت: %s تومان", PRICE_INCREASE_TOMAN)
    logging.info(
        "فاصله بررسی: هر %s ساعت",
        CHECK_INTERVAL_HOURS
    )

    if not BOT_TOKEN:
        logging.warning(
            "توکن تنظیم نشده است؛ هنوز هیچ پیامی ارسال نمی‌شود."
        )

    logging.info("زمان شروع: %s", datetime.now().isoformat())


if name == "main":
    main()
