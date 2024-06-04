#!/usr/bin/python3
"""
Module 1-top_ten
Contains the function top_ten to get titles of the first 10 hot posts
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If an invalid subreddit is given,
    the function prints None.
    """
    # Define the URL for the API request
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'python:subreddit.hot.posts:v1.0 (by /u/your_username)'}
    
    # Set the parameters to limit the number of posts
    params = {'limit': 10}
    
    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if the response is successful
    if response.status_code == 200:
        # Parse the JSON response to get the titles of the first 10 hot posts
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        
        # Print the titles of the posts
        for post in posts:
            print(post.get('data', {}).get('title', None))
    else:
        # Print None for invalid subreddit
        print(None)

