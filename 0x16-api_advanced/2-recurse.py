import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Recursively queries the Reddit API to retrieve titles of all hot
        articles in a given subreddit.
    Args:
        subreddit (str): The name of the subreddit to check.
        hot_list (list): store the titles of hot articles.
        after (str): pagination, starting point for the next page.
    Returns:
        list or None: contains titles of all hot articles for the
        given subreddit,or None if no results are found. """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    data = requests.get(url, headers={'User-agent': 'my-bot'},
                        params={'after': after}, allow_redirects=False)

    if data.status_code == 200:
        after = data.json().get('data').get('after')
        posts = data.json().get('data').get('children')

        for post in posts:
            hot_list.append(post.get("data").get("title"))

        if after is None:
            # If there is no new page
            if len(hot_list) == 0:
                return None

            return hot_list
        else:
            # If there is another page
            return recurse(subreddit, hot_list, after)
    else:
        return None
