import requests

def recurse(subreddit, hot_list=[], after=None):
    """ Recursively queries the Reddit API to retrieve titles of all hot
        articles in a given subreddit.
    Args:
        subreddit (str): The name of the subreddit to check.
        hot_list (list): A list to store the titles of hot articles (default is an empty list).
        after (str): Identifier for pagination, indicating the starting point for the next page.
    Returns:
        list or None: A list containing the titles of all hot articles for the given subreddit,
                     or None if no results are found. """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    response = requests.get(url, headers={'User-agent': 'my-bot'},
                            params={'after': after}, allow_redirects=False)

    if response.status_code == 200:
        after = response.json().get('data', {})['after']
        post_list = response.json().get('data', {}).get('children', [])

        hot_list.extend(post.get("data", {}).get("title", "") for post in post_list)

        # If there is no 'after' value, indicating no more pages
        if after is None:
            return hot_list if hot_list else None
        else:
            # Recursively call the function with the 'after' value
            return recurse(subreddit, hot_list, after)
    else:
        return None
