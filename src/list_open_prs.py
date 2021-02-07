from github import Github
import sys

access_token = sys.argv[1]
repo = sys.argv[2]

owner, repository = repo.split("/")

gh = Github(access_token)

rep = gh.get_user(owner).get_repo(repository)
pulls = rep.get_pulls(state="open")
for pull in pulls:
    print(pull)
    print(dir(pull))
    print(pull.mergeable_state)
