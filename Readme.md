# Tethys

Tethys is a discord bot written in python. It is capable of running across multiple servers providing services across all.

## Usage
To use Tethys on your server, you will need to create logging channels with appropriate names. These are listed below:
- `tethys-logs` (Essential)
- `edit-delete-logs` (Optional)
- `join-leave-logs` (Optional)

The bot will need to be able to read/write messages in these channels in order to function properly. Logs are written to the appropriate log channel for each server it is part of, falling back to a log channel specified by ID in the config file. The fallback channel in the config file will also be used for system messages such as startup announcements and crash logs. This should not be outputting any server specific data.