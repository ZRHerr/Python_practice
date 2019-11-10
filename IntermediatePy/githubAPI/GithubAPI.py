# Flask application to view/sort GitHub Repos based off stars.
import requests
from githubAPI.models import GitHubRepo

GITHUB_API_URL = "https://api.github.com/search/repositories"

def create_query(languages, min_stars): #creating the query string
    query = " ".join(f"language:{language.strip()}" for language in languages) # to clear it of leading and trailing whitespace
    query = query + f" stars:>{min_stars}"
    return query

def repos_with_most_stars(languages, min_stars=40000, sort = "stars", order = "desc"):
    query = create_query(languages, min_stars)
    parameters = {"q": query, "sort": sort, "order": order}
    print(parameters)
    response = requests.get(GITHUB_API_URL, params=parameters)

    response_json = response.json()
    items = response_json["items"]
    return [GitHubRepo(item["name"], item["language"], item["stargazers_count"]) for item in items]
