import Tethys
import yaml
import pathlib
import os

def main():
    config_file_path = pathlib.Path("config.yaml")
    config = dict()
    if config_file_path.exists():
        config_file = open("config.yaml")
        config = yaml.load(config_file, Loader=yaml.FullLoader)
        config_file.close()
    else:
        config["tethys_token"] = os.environ.get("TETHYS_TOKEN")
        config["log_channel"] = os.environ.get("TETHYS_LOG_CHANNEL")

    bot = Tethys.Tethys(config)
    bot.run()

if __name__ == "__main__":
    main()