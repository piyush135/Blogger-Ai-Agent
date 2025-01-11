import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/blogger"]

def authenticate():
    """
    Authenticate with Google and return a Blogger API service instance.
    """
    creds = None
    if os.path.exists('token.json'):
        os.remove('token.json')
    else:
        print("token.json not found, skipping deletion.")
    
    token_path = "token.json"
    client_secret_file = "client_secret.json"
  

    if os.path.exists(token_path):       
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, SCOPES)
            creds = flow.run_local_server(port=8080)
        with open(token_path, "w") as token_file:
            token_file.write(creds.to_json())

    return build("blogger", "v3", credentials=creds)

def post_to_blog(blog_id, title, content):
    """
    Post content to Blogspot.
    """
    service = authenticate()

    body = {
        "kind": "blogger#post",
        "title": title,
        "content": content,
    }

    post = service.posts().insert(blogId=blog_id, body=body).execute()
    print(f"Post published! URL: {post['url']}")
