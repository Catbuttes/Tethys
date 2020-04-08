import Tethys
import yaml
import pathlib

def main():
    config_file_path = pathlib.Path("config.yaml")
    config = dict()
    if config_file_path.exists():
        config_file = open("config.yaml")
        config = yaml.load(config_file, Loader=yaml.FullLoader)
        config_file.close()
    else:
        raise FileNotFoundError("No config found")

    bot = Tethys.Tethys(config)
    bot.run()

if __name__ == "__main__":
    main()