from config.config import Config
import openai
from llm.llm_prompt import LlmPrompt


class Llm:

    model = None
    client = None

    @classmethod
    def setup_llm(cls):
        if Config.llm_model_in_use == "gpt":
            cls.client = openai.OpenAI(api_key=Config.gpt_api_key)
            cls.model = "gpt-4o"
        else:
            raise Exception("Invalid model selected.")

    @classmethod
    def get_randon_car_type(cls):
        cls.setup_llm()
        response = cls.client.chat.completions.create(
            model=cls.model,
            messages=[
                {"role": "user", "content": LlmPrompt.get_random_car_type_prompt()}
            ],
            temperature=1.8,
            top_p=0.9,
        )

        print("")

    @classmethod
    def get_praise(cls, match_data: str, play_as: str, word_cnt: int, token_cnt: int):
        cls.setup_llm()

        response = cls.client.chat.completions.create(
            model=cls.model,
            messages=[
                {"role": "system", "content": LlmPrompt.get_system_prompt()},
                {"role": "user", "content": LlmPrompt.get_user_prompt_for_priase(match_data, play_as, word_cnt)}
            ],
            temperature=1.8,
            top_p=0.9,
            max_tokens=token_cnt
        )

        reply = response.choices[0].message.content
        print("PRAISE:  ---   " + reply)
        print("------------------------")
        return reply

    @classmethod
    def get_snide(cls, match_data: str, play_as: str, word_cnt: int, token_cnt: int):
        cls.setup_llm()

        response = cls.client.chat.completions.create(
            model=cls.model,
            messages=[
                {"role": "system", "content": LlmPrompt.get_system_prompt()},
                {"role": "user", "content": LlmPrompt.get_user_prompt_for_snide(match_data, play_as, word_cnt)}
            ],
            temperature=1.8,
            top_p=0.9,
            max_tokens=token_cnt
        )

        reply = response.choices[0].message.content
        print("SNIDE:  ---   " + reply)
        print("------------------------")
        return reply

    @classmethod
    def get_profanity(cls, match_data: str, play_as: str, word_cnt: int, token_cnt: int):
        cls.setup_llm()

        response = cls.client.chat.completions.create(
            model=cls.model,
            messages=[
                {"role": "system", "content": LlmPrompt.get_system_prompt()},
                {"role": "user", "content": LlmPrompt.get_user_prompt_for_profanity(match_data, play_as, word_cnt)}
            ],
            temperature=1.8,
            top_p=0.9,
            max_tokens=token_cnt
        )

        reply = response.choices[0].message.content
        print("PROFANITY:  ---   " + reply)
        print("--------------------------")
        return reply

