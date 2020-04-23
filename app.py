#!/usr/bin/env python3
import Tethys
import os



def main():

    config = dict()
    config["tethys_token"] = os.environ['TETHYS_TOKEN']
    config["log_channel"] = os.environ['TETHYS_LOG_CHANNEL']
    config["data_dir"] = os.environ['TETHYS_DATA']

    bot = Tethys.Tethys(config)
    bot.run()


if __name__ == "__main__":
    main()
