# Tethys
![Publish](https://github.com/Catbuttes/Tethys/workflows/Publish/badge.svg) ![Lint and Test](https://github.com/Catbuttes/Tethys/workflows/Lint%20and%20Test/badge.svg)

Tethys is a discord bot written in python. It is capable of running across multiple servers providing services across all.

## Usage
To use Tethys on your server, you will need to create logging channels with appropriate names. These are listed below:
- `tethys-logs` (Essential)
- `edit-delete-logs` (Optional)
- `join-leave-logs` (Optional)

The bot will need to be able to read/write messages in these channels in order to function properly. Logs are written to the appropriate log channel for each server it is part of, falling back to a log channel specified by ID in the config file. The fallback channel in the config file will also be used for system messages such as startup announcements and crash logs. This should not be outputting any server specific data.

Once these are set up, simply click [Here](https://discordapp.com/api/oauth2/authorize?client_id=696837495978983465&permissions=0&scope=bot) to invite the bot. You must have server management permissions to do this.

## Development
Tethys is intended to be an open source bot. Please feel free to offer any contributions you feel may help in it's development.
If you do wish to develop the bot, it has a test suite using the python unittest module, which can be run using `python -m unittest`. Pull requests are welcome although it is preferred that they come with tests to prove their behaviour!

Setting up your development environment is simply a case of running `pip install -r requirements.txt`. To spin up the bot, create the environment variables set using the sample .env file and then run `python3 app.py`

Please ensure that all code can pass a flake8 run as these are done automatically and no pull requests will be accepted until those checks are green. The tests that it will need to pass are
`flake8 . --count --max-complexity=10 --max-line-length=120 --statistics` and `flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics`