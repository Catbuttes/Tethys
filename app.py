import Tethys
import yaml

def main():
    config_file = open("config.yaml")
    config = yaml.load(config_file, Loader=yaml.FullLoader)
    config_file.close()

    bot = Tethys.Tethys()
    bot.run(config["tethys_token"])

if __name__ == "__main__":
    main()