#!/usr/bin/python3
"""
Module 0-subs
Contains the function number_of_subscribers to get subreddit subscriber count
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If an invalid subreddit is given,
    the function returns 0.
    """
    # Define the URL for the API request
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'python:subreddit.subscriber.counter:v1.0 (by /u/your_username)'}
    
    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response is successful
    if response.status_code == 200:
        # Parse the JSON response to get subscriber count
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
    else:
        # Return 0 for invalid subreddit
        return 0
