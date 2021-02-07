from github import Github
import datetime
import os

ACCESS_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")

owner, repository = REPO_NAME.split("/")

gh = Github(ACCESS_TOKEN)

open_prs = []
rep = gh.get_user(owner).get_repo(repository)
pulls = rep.get_pulls(state="open")
for pull in pulls:
    open_prs.append(
        {
            "title": pull.title,
            "state": pull.state,
            "created_at": pull.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": pull.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
            "mergeable": pull.mergeable,
            "mergeable_state": pull.mergeable_state,
            "merged": pull.merged,
        }
    )

print(f"::set-output name=pulls::{open_prs}")
