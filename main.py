import google.genai as genai
import pandas as pd
client = genai.Client(api_key="ENTER_API_KEY")

def generate_long_tail_keywords(topic):
    prompt = f"Act as an expert SEO strategist. My niche is sustainable gardening. My target audience is urban homeowners. Task: Generate a list of 10 highly relevant and low-competition long-tail keywords centered around the topic: \n\n{topic}. For each keyword, provide the Keyword Phrase, the estimated Search Intent for Informational, Commercial, Navigational, Transactional), and a 1-sentence description of the Ideal Target Article Angle."
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def generate_article_outline(long_tail_keywords):
    prompt = f"Use the top-performing informational long-tail keyword from the previous step: \n\n{long_tail_keywords}. Task: Develop a comprehensive, SEO-optimized article outline for a target word count of 800 words. The outline must include an engaging H1 Title that incorporates the primary keyword. 2-3 main H2 sections that logically cover the topic and address the specified Search Intent. 1-2 H3 sub-sections under each H2, structured to address common 'People Also Ask' (PAA) questions and secondary LSI keywords. A final Conclusion H2 with a strong Call-to-Action (CTA)."
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def generate_primary_keyword(long_tail_keywords):
    prompt = f"From the list of long tail keywords generated from prompt 1: \n\n{long_tail_keywords}, select the primary keyword for the article draft."
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def generate_article_draft(article_outline, primary_keyword):
    prompt = f"Using the complete outline generated in the previous step: \n\n{article_outline} and the primary keyword from prompt 3: \n\n{primary_keyword}, draft the complete article. Guidelines: Write in a friendly and conversational tone. Ensure a seamless, natural flow. Do not bold keywords. Integrate the primary keyword (from Prompt 2) into the introduction, first H2, and conclusion. Strategically integrate at least 5 of the other long-tail keywords from Prompt 1 into the body of the text where they naturally fit the H2/H3 context. Draft the content section-by-section, following the exact H2/H3 structure."
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def generate_seo_title_tag(article_draft, primary_keyword):
    prompt = f"Based on the fully drafted article content from the previous step: \n\n{article_draft} and the primary keyword\n\n{primary_keyword}, generate the SEO Title Tag. Must be 55-60 characters long, include the primary keyword near the beginning, and use a power word (e.g., Guide, Secret, Proven)."
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def generate_meta_description(article_draft, primary_keyword):
    prompt = f"Based on the fully drafted article content from the previous step: \n\n{article_draft} and the primary keyword:\n\n{primary_keyword}, generate the Meta Description. Must be 150-160 characters long, be highly compelling, include the primary keyword, and clearly state the value the user will receive upon clicking."
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

topic = "Drip Irrigation for Small Gardens",
long_tail_keywords = generate_long_tail_keywords(topic)
article_outline = generate_article_outline(long_tail_keywords)
primary_keyword = generate_primary_keyword(long_tail_keywords)
article_draft = generate_article_draft(article_outline, primary_keyword)
seo_title_tag = generate_seo_title_tag(article_draft, primary_keyword)
meta_description = generate_meta_description(article_draft, primary_keyword)

seo_data = {
    'topic': [topic],
    'primary_keyword': [primary_keyword],
    'seo_title_tag': [seo_title_tag],
    'meta_description': [meta_description],
    'long_tail_keywords': [long_tail_keywords],
    'article_outline': [article_outline],
    'article_draft': [article_draft]
}

df = pd.DataFrame(seo_data)

df.to_csv(r"C:\Users\Bhaskar Rana\OneDrive\Desktop\seo_blog_generation.csv", index = False)
print("Blog is generated and saved to seo_blog_generation.csv")