# Ebola-info-chatbot

This chatbot is a simple Ebola information chatbot implemented in telegram and uses the twitter api to get tweets from the ministry of health twitter account.

This chatbot fuctionality requires an existing telegram bot.

1. Create a virtual environment.

2. Use pip to install requirements from requirements.txt

3. Add a telegram bot token to .env file < TOKEN = '...' >

4. Create a config.ini file for twitter api tokens, of this format;

    [twitter]

    api_key = ...
    api_key_secret = ...

    access_token = ...
    access_token_secret = ...