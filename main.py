import streamlit as st
import openai
from openai import OpenAI
import praw

#cant be asked to make a .env file or anything else just import manually 😗

OPENAI_API_KEY = "pls type your own key"
openai.api_key = OPENAI_API_KEY
client = OpenAI(api_key = OPENAI_API_KEY)

REDDIT_CLIENT_ID = "Enter your ID"
REDDIT_CLIENT_SECRET = "Enter your secret 🤫"
REDDIT_USER_AGENT = "Enter your user agent"
REDDIT_USERNAME = "your username"
REDDIT_PASSWORD = "your password"

#reddit init
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD
)
#openai prompt
def generate_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages={"role": "user", "content": prompt}
    )
    return response.choices[0].message['content']

def postToReddit(subreddit_name, title, content):
    subreddit = reddit.subreddit(subreddit_name)
    subreddit.submit(title, selftext=content)

def main():
    st.title("Reddit Post Generator")

    subreddit = st.text_input('Subreddit Name:')
    
    prompt = st.text_area('Prompt for the post:')
    
    title = st.text_input('Title of the post:')

    if st.button('Generate and Post to Reddit'):
        thePost = generate_response(prompt)
        postToReddit(subreddit, title, thePost)
        
        st.success('Post successfully submitted to Reddit.')

if __name__ == "__main__":
    main()
