import pandas as pd
from .definitions import (
    COMMIT_FREQUENCY, PR_MERGE_RATE, ISSUE_RESOLUTION_TIME,
    CONTRIBUTOR_ACTIVITY, AVG_COMMITS_PER_CONTRIBUTOR, OPEN_ISSUES_RATIO, PR_ACCEPTANCE_RATE
)

class MetricsCalculator:
    def __init__(self, data_storage):
        self.data_storage = data_storage

    def calculate_commit_frequency(self, repo_url):
        """Calculate commit frequency for a repository."""
        commits = self.data_storage.retrieve_data(f"{repo_url}_commits")
        if not commits:
            return None
        df = pd.DataFrame(commits)
        df['date'] = pd.to_datetime(df['date'])
        frequency = df['date'].diff().dt.days.mean()
        return frequency

    def calculate_pr_merge_rate(self, repo_url):
        """Calculate PR merge rate for a repository."""
        prs = self.data_storage.retrieve_data(f"{repo_url}_pull_requests")
        if not prs:
            return None
        df = pd.DataFrame(prs)
        df['merged_at'] = pd.to_datetime(df['merged_at'])
        merge_rate = df['merged_at'].notnull().sum() / len(df)
        return merge_rate

    def calculate_issue_resolution_time(self, repo_url):
        """Calculate issue resolution time for a repository."""
        issues = self.data_storage.retrieve_data(f"{repo_url}_issues")
        if not issues:
            return None
        df = pd.DataFrame(issues)
        df['created_at'] = pd.to_datetime(df['created_at'])
        df['closed_at'] = pd.to_datetime(df['closed_at'])
        resolution_times = (df['closed_at'] - df['created_at']).dt.days
        avg_resolution_time = resolution_times.mean()
        return avg_resolution_time

    def calculate_contributor_activity(self, repo_url):
        """Calculate contributor activity for a repository."""
        contributors = self.data_storage.retrieve_data(f"{repo_url}_contributors")
        if not contributors:
            return None
        return len(contributors)

    def calculate_avg_commits_per_contributor(self, repo_url):
        """Calculate average commits per contributor."""
        commits = self.data_storage.retrieve_data(f"{repo_url}_commits")
        contributors = self.data_storage.retrieve_data(f"{repo_url}_contributors")
        if not commits or not contributors:
            return None
        total_commits = len(commits)
        total_contributors = len(contributors)
        return total_commits / total_contributors if total_contributors > 0 else None

    def calculate_open_issues_ratio(self, repo_url):
        """Calculate the ratio of open issues to total issues."""
        issues = self.data_storage.retrieve_data(f"{repo_url}_issues")
        if not issues:
            return None
        df = pd.DataFrame(issues)
        total_issues = len(df)
        open_issues = df[df['state'] == 'open'].shape[0]
        return open_issues / total_issues if total_issues > 0 else None

    def calculate_pr_acceptance_rate(self, repo_url):
        """Calculate the PR acceptance rate (merged vs closed without merge)."""
        prs = self.data_storage.retrieve_data(f"{repo_url}_pull_requests")
        if not prs:
            return None
        df = pd.DataFrame(prs)
        merged_prs = df['merged_at'].notnull().sum()
        total_prs = len(df)
        return merged_prs / total_prs if total_prs > 0 else None

    def get_metrics(self, repo_url):
        """Get all metrics for a repository."""
        metrics = {
            COMMIT_FREQUENCY: self.calculate_commit_frequency(repo_url),
            PR_MERGE_RATE: self.calculate_pr_merge_rate(repo_url),
            ISSUE_RESOLUTION_TIME: self.calculate_issue_resolution_time(repo_url),
            CONTRIBUTOR_ACTIVITY: self.calculate_contributor_activity(repo_url),
            AVG_COMMITS_PER_CONTRIBUTOR: self.calculate_avg_commits_per_contributor(repo_url),
            OPEN_ISSUES_RATIO: self.calculate_open_issues_ratio(repo_url),
            PR_ACCEPTANCE_RATE: self.calculate_pr_acceptance_rate(repo_url)
        }
        return metrics