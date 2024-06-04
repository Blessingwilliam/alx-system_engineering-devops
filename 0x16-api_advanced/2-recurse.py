#!/usr/bin/python3
"""
Module 2-recurse
Contains the function recurse to get titles of all hot posts
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for the given subreddit,
    the function returns None.
    """
    # Define the URL for the API request
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'python:subreddit.hot.posts:v1.0 (by /u/your_username)'}
    
    # Set the parameters to handle pagination
    params = {'limit': 100}
    if after:
        params['after'] = after
    
    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if the response is successful
    if response.status_code == 200:
        # Parse the JSON response to get the list of hot posts
        data = response.json()
        children = data.get('data', {}).get('children', [])
        
        # Extract titles and add to hot_list
        for child in children:
            hot_list.append(child.get('data', {}).get('title', None))
        
        # Get the next 'after' value for pagination
        after = data.get('data', {}).get('after', None)
        
        # If 'after' is not None, make a recursive call
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        # Return None for invalid subreddit
        return None

