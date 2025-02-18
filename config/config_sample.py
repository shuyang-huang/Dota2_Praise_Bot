class Config:

    discord_bot_token = "<discord_bot_token>"
    gpt_api_key = "<gpt_api_key>"
    deepseek_api_key = "<deepseek_api_key>"

    llm_model_in_use = "gpt"

    @classmethod
    def get_token(cls, attr):
        return getattr(cls, attr, None)
