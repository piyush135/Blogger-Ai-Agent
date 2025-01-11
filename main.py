from blog_writer.writer import generate_blog
from blog_writer.critic import refine_blog
from blog_writer.readability import evaluate_readability
from blog_writer.seo import seo_analysis
from services.blogspot_poster import post_to_blog
from config import config

# Replace with your Blogspot blog ID
BLOG_ID = "6627333371495103873"

def main():
    # Input details
    topic = "How AI is Transforming Blogging"
    keywords = ["AI", "blogging", "content creation", "automation", "images"]
    
    # # Generate blog content
    print("Generating blog content...")
    content = generate_blog(topic, keywords)
    print("Initial Blog Content:\n", content)
    
    # # Evaluate readability
    print("\nEvaluating readability...")
    readability = evaluate_readability(content)
    print("Readability:", readability)
    
    # # Perform SEO analysis
    print("\nPerforming SEO analysis...")
    seo = seo_analysis(content, keywords)
    print("SEO Analysis:", seo)
    
    # # Refine blog content
    print("\nRefining blog content...")
    refined_content = refine_blog(content, keywords)
    print("Refined Blog Content:\n", refined_content)
    
    # Post to WordPress
    print("\nPublishing the blog post...")
    post_to_blog(BLOG_ID, f"Exploring {topic}", refined_content)
    # response = post_to_blog(
    #     title=f"AI-Generated Blog: {topic}",
    #     content=refined_content,
    #     categories=config["wordpress"]["categories"],
    #     tags=config["wordpress"]["tags"],
    #     wp_url=config["wordpress"]["url"],
    #     username=config["wordpress"]["username"],
    #     password=config["wordpress"]["password"]
    # )
    print("WordPress Response:", response)

if __name__ == "__main__":
    main()
