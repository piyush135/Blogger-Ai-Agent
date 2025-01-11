pip # AI Blog Writer

This Python project automates blog writing, critiquing, and posting to WordPress using OpenAI's GPT and WordPress API.

## Features
- Generate blog posts based on a given topic and keywords.
- Critique and refine blog content for readability, tone, grammar, and SEO.
- Analyze readability and keyword density.
- Automatically post blogs to a WordPress site.
- Schedule blog generation and posting tasks.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ai_blog_writer.git
   cd ai_blog_writer


Go to the Google Developer Console.
Navigate to your project.
Under APIs & Services > Credentials, look for the OAuth 2.0 Client IDs section.
Find the client ID you're using and click on it to open the configuration page.
Under the Authorized redirect URIs section, ensure that the URI you are using in your Python script matches exactly with one of the URIs listed there.
For example, if you're using http://localhost, make sure that this is listed as an authorized redirect URI.
If you're using http://localhost:8080, make sure that exact URI is included in the list.
Note: For local development, the typical redirect URI is:

arduino
Copy code
http://localhost
If you haven't configured this, add it as a new redirect URI.