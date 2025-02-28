import requests

def get_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_repo_commits(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
    response = requests.get(url)
    response.raise_for_status()
    return len(response.json())

def get_repo_commit_counts(username):
    try:
        repos = get_user_repos(username)
        return [
            f'Repo: {repo["name"]} Number of commits: {get_repo_commits(username, repo["name"])}'
            for repo in repos
        ]
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"