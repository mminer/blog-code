"""Demonstrates a function that fetches pages of results from a REST API."""

from functools import partial
from itertools import chain
import requests


def fetch_all_pages(url, request_func=requests.get):
    """Fetches paged results from a REST endpoint."""
    def fetch_page(next_page):
        """Generator that fetches pages of results until none are left."""
        while next_page:
            response = request_func(next_page)
            yield response.json()

            # Get next page from the response's Link header.
            next_page = response.links.get('next', {}).get('url')

    results = chain.from_iterable(page for page in fetch_page(url))
    return results


# Example usage:

# Fetch all commits in Zulko/moviepy GitHub repository (but only since 2015).
url = 'https://api.github.com/repos/Zulko/moviepy/commits'
request_func = partial(requests.get, params={'since': '2015-01-01T00:00:00Z'})
results = fetch_all_pages(url, request_func)
print(results)
