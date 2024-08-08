# Upload files to Telegram channel

## Description
Many people use private Telegram channels to store their private files because it is secure, easy, and fast. This script takes a folder and uploads all supported files, which you can configure.
The source code is pretty short and basic, so you can customize it to suit your needs.


## Installation
1. Clone this repository:
   
         git clone https://github.com/HBarotov/Tg-channel-DB.git
         cd Tg-channel-Db
  
2. Create a new virtual environment and activate it:

   Use ```venv``` (Python 3.3+):
   
         python -m venv .venv

   Activate on Windows:

         .venv\Scripts\Activate.ps1

   Activate on Linux/macOS:

         source .venv/bin/activate
   
4. Install the required packages:

         pip install -r requirements.txt

5. Go to [Telegram console](https://my.telegram.org/apps) and create an app. Save the `app_id` and `app_hash`:

6. Create a `.env` file next to `main.py` with the following contents: and fill in your details:

        api_id=
        api_hash=
        phone_number=
        channel_name=
        media_directory=

7. Run `main.py` file.
