import openai
from config import config

openai.api_key = config["openai_api_key"]

def generate_blog(topic, keywords):
    prompt = f"Write a professional, SEO-optimized blog post about {topic}. Include these keywords: {', '.join(keywords)}. Make it engaging, informative, and easy to read."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful and professional assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024,
        temperature=0.7
    )
    return response["choices"][0]["message"]["content"]