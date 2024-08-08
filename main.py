"""
Python script to upload files to a Telegram channel.

The quick start guide is in the README.md file.
"""

import os

from environs import Env
from telethon import TelegramClient

env = Env()
env.read_env()

# Your credentials in your .env file.
api_id = env.str("api_id")
api_hash = env.str("api_hash")
phone_number = env.str("phone_number")
channel_name = env.str("channel_name")

# Connecting to your Telegram app;
# The first time it asks for credentials
client = TelegramClient("session_name", api_id, api_hash)


# Main async function
async def main():
    await client.start(phone=phone_number)

    dialogs = await client.get_dialogs()

    # Find your channel
    channel = None
    for dialog in dialogs:
        if dialog.name == channel_name:
            channel = dialog.entity
            break

    if not channel:
        print("Channel not found")
        return

    # Path to your media_directory
    media_directory = env.str("media_directory")

    # Supported file extensions
    # Can be extended to include other document formats as well.
    supported_extensions = (
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".mp4",
        ".mov",
        ".avi",
        ".mkv",
    )

    # Upload media files
    for media_name in os.listdir(media_directory):
        media_path = os.path.join(media_directory, media_name)
        if os.path.isfile(media_path) and media_name.lower().endswith(
            supported_extensions
        ):
            await client.send_file(channel, media_path, force_document=True)
            print(f"Uploaded {media_name}")


with client:
    client.loop.run_until_complete(main())
