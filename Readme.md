
1. Enable local env.
```commandline
<VirtualEnvPath>\Scripts\activate
```
If you don't know how to create virtual env, ask ChatGPT.

2. Install requirements.
```commandline
pip install -r requirements.txt
```
3. Update the config file.

Copy the `config/config_sample.py` to `config/config.py` and fill in the required tokens/keys.

Some additional guidances:
* ChatGPT API key: https://platform.openai.com/api-keys
* Discord bot token: https://discord.com/developers/applications
* DeepSeek API key: https://platform.deepseek.com/usage
* Stratz token: https://stratz.com/api

4. Run the bot.
```commandline
python discord_bot.py
```

5. Disable local env.
```commandline
deactivate
```