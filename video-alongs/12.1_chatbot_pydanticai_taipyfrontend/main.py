import taipy.gui.builder as tgb
from taipy.gui import Gui
from chat import JokeBot

bot = JokeBot()

user_prompt = ""
messages = []
chat_history = []
users = ["human", "bot"]

def send_message(state, var_name: str, payload: dict):
    message = payload.get("args")[2]
    user = payload.get("args")[3]
    print(user, message)
    
    messages.append((str(len(messages)), message, user[0]))

    try: 
        result = bot.chat(message)
        bot_msg = result.get("bot")
    except Exception as e:
        bot_msg = f"Bot error: {e}"
    
    
    messages.append((str(len(messages)), bot_msg, user[1]))
    state.messages = messages


with tgb.Page() as page:
    with tgb.part(class_name="chat-window"):
        tgb.text("# Chat with JokeBot", mode="md")

        tgb.chat(
            "{messages}",
            users="{users}",
            sender_id="{users[0]}",
            on_action=send_message,
        )

if __name__ == "__main__":
    Gui(page=page).run(use_reloader=True, port=8080, host="0.0.0.0")
