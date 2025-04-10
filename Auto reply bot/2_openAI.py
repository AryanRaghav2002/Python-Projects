from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

command='''
[3:45 pm, 7/4/2025] @®`/@√\/: Killer smirk
[5:07 pm, 7/4/2025] Shama Amity: Bc😂
[5:08 pm, 7/4/2025] Shama Amity: Kya galat lagg raha hu
[5:02 pm, 10/4/2025] Shama Amity: Bhai yeh woh choti height wala driver hai
[5:02 pm, 10/4/2025] Shama Amity: 😂😂
[5:02 pm, 10/4/2025] Shama Amity: Yeh mast chalata hai but
[5:02 pm, 10/4/2025] @®`/@√\/: Chota par tez hai
[5:02 pm, 10/4/2025] Shama Amity: Haan
'''
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role" : "system" , "content": "You are a person named Aryan who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Aryan."
        },
        {   "role" : "user", "content" : command}
    ]
)

print(completion.choices[0].message.content)