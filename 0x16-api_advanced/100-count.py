#!/usr/bin/python3
"""
Module 100-count
Contains the function count_words to count keywords in hot posts
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    # Normalize word_list to lowercase and initialize word_count dictionary
    if not word_count:
        word_list = [word.lower() for word in word_list]
        word_count = {word: 0 for word in word_list}
    
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
        
        # Iterate over the titles and count keywords
        for child in children:
            title = child.get('data', {}).get('title', "").lower().split()
            for word in word_list:
                word_count[word] += title.count(word)
        
        # Get the next 'after' value for pagination
        after = data.get('data', {}).get('after', None)
        
        # If 'after' is not None, make a recursive call
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            # Sort the word_count dictionary and print the results
            sorted_word_count = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
            for word, count in sorted_word_count:
                if count > 0:
                    print("{}: {}".format(word, count))
            return
    else:
        # If response is not successful, return
        return


