import pyautogui
import time
import pyperclip
from openai import OpenAI
from dotenv import load_dotenv

import os
load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def is_last_message_from_sender(chat_history_text, your_name="@®`/@√\\/"):
    # Split by lines and strip empty ones
    messages=chat_history_text.strip().split("/2025] ")[-1]
    
    if your_name not in messages:
        return True
    else: return False

 # Step 0: Open WhatsApp chat or focus on it
pyautogui.click(x=1041, y=1047)  # Adjust this to your chat icon location
time.sleep(2)  # Let it load

while True:

    # Step 1: Click and hold from start of visible conversation
    start_x, start_y = 675, 266
    end_x, end_y = 1869, 900

    pyautogui.moveTo(start_x, start_y, duration=0.5)
    pyautogui.mouseDown()

    # Step 2: Drag down to end of visible conversation
    pyautogui.moveTo(end_x, end_y, duration=1.5)
    pyautogui.mouseUp()

    # Step 3: Copy selected content
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.click(1855, 814)#To deslect the chat

    # Step 4: Retrieve it from clipboard
    chat_history = pyperclip.paste()
    print(chat_history)

    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                "role": "system",
                "content": (
                    "You are a person named @®`/@√\\/ who is from India and speaks both Hindi and English. "
                    "You are chill,wise and very intellectual while chatting. You respond exactly like @®`/@√\\/ would. "
                    "You never say you're an AI, and you never mention anything about being a model or assistant. "
                    "Your job is to reply *only to the most recent message* sent by the other person in the chat. "
                    "Don't add greetings unless the message clearly needs one. Don't include time, date, or anything else — just the next chat message only."
                )
                },
                {
                    "role": "user",
                    "content": chat_history
                }
            ]
        )
        response = completion.choices[0].message.content.strip()
        print("Auto-reply:", response)
        # Step 5: Copy the response to clipboard
        pyperclip.copy(response)
        time.sleep(2)

        # Step 6: Click the input box and paste
        pyautogui.click(975, 956)  # Adjust if needed
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter") 
    else:
        print("No reply needed — you sent the last message.")

     