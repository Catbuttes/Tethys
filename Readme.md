# Tethys

Tethys is a discord bot written in python. It is capable of running across multiple servers providing services across all.

## Usage
To use Tethys on your server, you will need to create logging channels with appropriate names. These are listed below:
- `tethys-logs` (Essential)
- `edit-delete-logs` (Optional)
- `join-leave-logs` (Optional)

The bot will need to be able to read/write messages in these channels in order to function properly. Logs are written to the appropriate log channel for each server it is part of, falling back to a log channel specified by ID in the config file. The fallback channel in the config file will also be used for system messages such as startup announcements and crash logs. This should not be outputting any server specific data.

## Development
Tethys is intended to be an open source bot. Please feel free to offer any contributions you feel may help in it's development.
If you do wish to develop the bot, it has a test suite using the python unittest module, which can be run using `python -m unittest`. Pull requests are welcome although it is preferred that they come with tests to prove their behaviour!

Setting up your development environment is simply a case of running `pip install -r requirements.txt`. To spin up the bot, either create a config file or have the environment variables set using the sample config.yaml and .env files and then run `python3 app.py`