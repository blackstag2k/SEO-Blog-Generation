# SEO Blog Generation with Gemini API

This project is about generating an 800-word blog/article along with a **list of keywords** and a **primary keyword** from a topic through **Google GenAI**

## Workflow

genai package - pandas - long tail keywords - article outline - primary keyword - article draft - seo title tag - meta description - saved in csv

## Steps to Run the Code

1. Cloning the repository:

git clone https://github.com/blackstag2k/SEO-Blog-Generation.git

2. Installing the Dependencies for the project:

* dependencies listed in the requirements.txt

pip install -r requirements.txt 

* If you want to execute the installed pip module instead of a script file, then use the command below in Command Window

pip -m install -r requirements.txt

### Example:

- python -m pip install pandas,
- python -m pip install google-generativeai

3. Add your API Key 

* Google AI API, Open AI API, etc. generated from any platform. Google Genai key is used here.

export GOOGLE_API_KEY="YOUR_KEY"

4. Run

python main.py

**Output**

Output CSV:
| Topic | Primary Keyword | SEO Title Tag | Meta Description | Long Tail Keywords | Article Outline | Article Draft |
|-------|--------|--------|--------|--------|--------|--------|
| Drip Irrigation for Small Gardens | Reduce water usage urban vegetable patch drip | Guide to DIY Drip: Reduce Water Usage Urban Vegetable Patch | Transform your urban balcony garden! Build a DIY drip system & reduce water usage in your urban vegetable patch drip setup. Save water, time, & grow healthier plants with our easy guide. | List of long tail keywords | Outline of the blog/article | Final Article Draft of 800 words |

## Tools Used

- Google AI API (Gemini)
- Pandas
- Python 3.14

## Lessons to be Learned

- Using the Pandas DataFrame as a worksheet to save the particulars of the prompt.
- Executing the code through a virtual environment (.venv) like VS Code.
- Prompt chaining to execute multiple prompts and get the best results.


Documented during the Prompt Engineering Course for Prompt Chaining and Content Generation
