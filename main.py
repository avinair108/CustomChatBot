from openai import OpenAI

client = OpenAI()

personality_prompt = input("Please enter your desired bot type: ")
user_prompt = input("Please enter your prompt: ")

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": personality_prompt,
        },
        {
            "role": "user",
            "content": user_prompt,
        },
    ],
    temperature=0.7,
    max_tokens=64,
    top_p=1,
)

print(response.choices[0].message.content)
