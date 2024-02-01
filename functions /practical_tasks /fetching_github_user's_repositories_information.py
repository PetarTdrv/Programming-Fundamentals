import requests

def fetch_user_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        print("Error!")
        return None
    

def display_repository_info(repositories):
    if repositories:
        print("User's Repositories:")
        for repo in repositories:
            print(f"\nName: {repo['name']}")
            print(f"Description: {repo['description']}")
            print(f"Languagee: {repo['language']}")
            print(f"Stars: {repo['stargazers_count']}")


def main():
    username = input("Enter GitHun username: ")
    repositories = fetch_user_repositories(username)
    if repositories:
        repos = display_repository_info(repositories)
        return repos

print(main())
