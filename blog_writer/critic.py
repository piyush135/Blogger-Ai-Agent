import openai
from config import config

openai.api_key = config["openai_api_key"]

def refine_blog(content, keywords):
    prompt = f"Refine the following blog content to improve readability, tone, grammar, and SEO (keywords: {', '.join(keywords)}):\n\n{content}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024,
        temperature=0.7
    )
    return response.choices[0].message['content']