import Tethys
import yaml

def main():
    config_file = open("config.yaml")
    config = yaml.load(config_file, Loader=yaml.FullLoader)
    config_file.close()

    bot = Tethys.Tethys(config)
    bot.run()

if __name__ == "__main__":
    main()