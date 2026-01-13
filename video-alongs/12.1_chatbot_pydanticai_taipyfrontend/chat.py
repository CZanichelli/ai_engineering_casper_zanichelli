from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()

class JokeBot:
    def __init__(self):
        self.chat_agent = Agent(
            "google-gla:gemini-2.5-flash",
            system_prompt="Be a joking programming nerd, always answer with a programming joke no matter what the question is"
        )

        self.result = None

    def chat(self, prompt: str) -> dict:
        message_history = self.result.all_messages() if self.result else None
        self.result = self.chat_agent.run_sync(prompt, message_history=message_history)

        return{"user": prompt, "bot": self.result.output}
    

if __name__ == "__main__":
    bot = JokeBot()
    result = bot.chat("hello There")
    print(result, "\n")

    result = bot.chat("what did i ask you first?")
    print(result)

    