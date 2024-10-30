from github import Github
import os
from .data_storage import DataStorage

# Get the GitHub token from environment variables
token = os.environ.get("GIT_TOKEN")

class Collector:
    def __init__(self, access=None):
        if access:
            self.g = Github(access[0])
        else:
            raise ValueError("No access token provided.")
        self.storage = DataStorage()

    def get_org(self, org):
        """Fetch organization details."""
        try:
            o = self.g.get_organization(org)
            return o
        except Exception as e:
            raise Exception(f"Error fetching organization: {str(e)}")

    def get_org_repos(self, org):
        """Fetch all repositories of an organization."""
        try:
            o = self.g.get_organization(org)
            repos = [repo.full_name for repo in list(o.get_repos())]
            self.storage.save_data(repos, f"{org}_repos")
            return repos
        except Exception as e:
            raise Exception(f"Error fetching repositories: {str(e)}")


    def get_saved_contributors(self, url):
        """Retrieve saved contributors for a repository."""
        try:
            return self.storage.retrieve_data(f"{url}_contributors")
        except Exception as e:
            raise Exception(f"Error retrieving saved contributors: {str(e)}")

    def get_all_contributors(self, url):
        """Fetch all contributors of a repository."""
        try:
            r = self.g.get_repo(url)
            contributors = [user.login for user in list(r.get_contributors())]
            self.storage.save_data(contributors, f"{url}_contributors")
            return contributors
        except Exception as e:
            raise Exception(f"Error fetching contributors: {str(e)}")
    def get_commits(self, repo_url):
        """Fetch all commits of a repository."""
        try:
            r = self.g.get_repo(repo_url)
            commits = [
                {
                    'sha': commit.sha,
                    'author': commit.author.login if commit.author else 'Unknown',
                    'message': commit.commit.message,
                    'date': commit.commit.committer.date.isoformat()
                }
                for commit in list(r.get_commits())
            ]
            self.storage.save_data(commits, f"{repo_url}_commits")
            return commits
        except Exception as e:
            raise Exception(f"Error fetching commits: {str(e)}")

    def get_pull_requests(self, repo_url):
        """Fetch all pull requests of a repository."""
        try:
            r = self.g.get_repo(repo_url)
            pull_requests = [
                {
                    'number': pr.number,
                    'title': pr.title,
                    'state': pr.state,
                    'created_at': pr.created_at.isoformat() if pr.created_at else None,
                    'merged_at': pr.merged_at.isoformat() if pr.merged_at else None
                }
                for pr in list(r.get_pulls(state='all'))
            ]
            self.storage.save_data(pull_requests, f"{repo_url}_pull_requests")
            return pull_requests
        except Exception as e:
            raise Exception(f"Error fetching pull requests: {str(e)}")

    def get_issues(self, repo_url):
        """Fetch all issues of a repository."""
        try:
            r = self.g.get_repo(repo_url)
            issues = [
                {
                    'number': issue.number,
                    'title': issue.title,
                    'state': issue.state,
                    'created_at': issue.created_at.isoformat() if issue.created_at else None,
                    'closed_at': issue.closed_at.isoformat() if issue.closed_at else None
                }
                for issue in list(r.get_issues(state='all'))
            ]
            self.storage.save_data(issues, f"{repo_url}_issues")
            return issues
        except Exception as e:
            raise Exception(f"Error fetching issues: {str(e)}")  
        """from github import Github
import os
from data_storage import DataStorage

# Get the GitHub token from environment variables
token = os.environ.get("GIT_TOKEN")
print(f"Token: {token}")

class Collector:
    def __init__(self, access=[]):
        if len(access) == 1:
            self.g = Github(access[0])
        self.storage = DataStorage()

    def get_org(self, org):
        o = self.g.get_organization(org)
        return o

    def get_org_repos(self, org):
        o = self.g.get_organization(org)
        print("Fetching repositories for organization...")
        repos = [repo.full_name for repo in list(o.get_repos())]
        
        # Store data in JSON
        self.storage.save_data(repos, f"{org}_repos")
        
        return repos

    def get_all_contributors(self, url):
        r = self.g.get_repo(url)
        print("Fetching contributors...")
        contributors = [user.login for user in list(r.get_contributors())]
        
        # Store data in JSON
        self.storage.save_data(contributors, f"{url}_contributors")
        
        return contributors

    def get_stats_contributors(self, url):
        r = self.g.get_repo(url)
        print("Fetching contributor stats...")
        items = [
            {item.author.login: item.raw_data['weeks']}
            for item in list(r.get_stats_contributors())
        ]
        
        # Store data in JSON
        self.storage.save_data(items, f"{url}_contributor_stats")
        
        return items

    def get_commits(self, repo_url):
        r = self.g.get_repo(repo_url)
        print("Fetching commits...")
        commits = [
            {
                'sha': commit.sha,
                'author': commit.author.login if commit.author else 'Unknown',
                'message': commit.commit.message,
                'date': commit.commit.committer.date.isoformat()  # Convert datetime to ISO format
            }
            for commit in list(r.get_commits())
        ]
        
        # Store data in JSON
        self.storage.save_data(commits, f"{repo_url}_commits")
        
        return commits

    def get_pull_requests(self, repo_url):
        r = self.g.get_repo(repo_url)
        print("Fetching pull requests...")
        pull_requests = [
            {
                'number': pr.number,
                'title': pr.title,
                'state': pr.state,
                'created_at': pr.created_at,
                'merged_at': pr.merged_at
            }
            for pr in list(r.get_pulls(state='all'))
        ]
        
        # Store data in JSON
        self.storage.save_data(pull_requests, f"{repo_url}_pull_requests")
        
        return pull_requests


    def get_issues(self, repo_url):
        r = self.g.get_repo(repo_url)
        print("Fetching issues...")
        
        issues = [
            {
                'number': issue.number,
                'title': issue.title,
                'state': issue.state,
                'created_at': issue.created_at.isoformat() if issue.created_at else None,  # Convert to ISO format
                'closed_at': issue.closed_at.isoformat() if issue.closed_at else None  # Convert to ISO format
            }
            for issue in list(r.get_issues(state='all'))
        ]
        
        # Store data in JSON
        self.storage.save_data(issues, f"{repo_url}_issues")
        
        return issues

    def get_pull_requests(self, repo_url):
        r = self.g.get_repo(repo_url)
        print("Fetching pull requests...")
        
        pull_requests = [
            {
                'number': pr.number,
                'title': pr.title,
                'state': pr.state,
                'created_at': pr.created_at.isoformat() if pr.created_at else None,  # Convert to ISO format
                'merged_at': pr.merged_at.isoformat() if pr.merged_at else None  # Convert to ISO format
            }
            for pr in list(r.get_pulls(state='all'))
        ]
        
        # Store data in JSON
        self.storage.save_data(pull_requests, f"{repo_url}_pull_requests")
        
        return pull_requests
    def get_reviews(self, repo_url):
        try:
            repo = self.g.get_repo(repo_url)
            print("Fetching reviews...")
            reviews_data = []
            pulls = repo.get_pulls(state='all')
            for pr in pulls:
                pr_number = pr.number
                reviews = pr.get_reviews()
                for review in reviews:
                    reviews_data.append({
                        'pr_number': pr_number,
                        'review_id': review.id,
                        'reviewer': review.user.login,
                        'state': review.state,
                        'submitted_at': review.submitted_at.isoformat() if review.submitted_at else None,
                        'body': review.body  # Added body of the review for additional context
                    })
                
            self.storage.save_data(reviews_data, f"{repo_url}_reviews")

        except Exception as e:
            print(f"An error occurred: {e}")
    
        return reviews_data
if __name__ == '__main__':
    credentials = [token]
    collector = Collector(credentials)
    
    # Replace with actual repo URLs
    org_name = "open-mmlab"
    repo_url = "open-mmlab/mmdetection"
    
    # Fetch and store data
    collector.get_org_repos(org_name)
    collector.get_all_contributors(repo_url)
    collector.get_stats_contributors(repo_url)
    collector.get_commits(repo_url)
    collector.get_pull_requests(repo_url)
    collector.get_issues(repo_url)
    #collector.get_reviews(repo_url)
    
    print("Data collection completed and stored.")"""
