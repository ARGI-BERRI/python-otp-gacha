import contextlib
import datetime as dt
import itertools
import zoneinfo

import tqdm
from loguru import logger

import otp

logger.remove()
logger.add(lambda msg: tqdm.tqdm.write(msg, end=""), colorize=True)


def main() -> None:
    key = otp.get_secret_key()
    logger.info(f"{key=}")

    now = dt.datetime.now(zoneinfo.ZoneInfo("Asia/Tokyo"))

    for _ in tqdm.tqdm(itertools.count()):
        if otp.get_time_based_otp(key, unix_time=now.timestamp()) == "777777":
            logger.info(f"{now.isoformat()=}")

        now += dt.timedelta(seconds=30)


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        main()
