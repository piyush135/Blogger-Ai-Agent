import requests

def post_to_wordpress(title, content, categories, tags, wp_url, username, password):
    url = f"{wp_url}/wp-json/wp/v2/posts"
    credentials = (username, password)
    data = {
        "title": title,
        "content": content,
        "status": "publish",
        "categories": categories,
        "tags": tags
    }
    response = requests.post(url, json=data, auth=credentials)
    if response.status_code == 201:
        print("Blog posted successfully!")
    else:
        print("Failed to post the blog:", response.json())
    return response.json()
