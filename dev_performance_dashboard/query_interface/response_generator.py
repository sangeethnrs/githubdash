# query_interface/response_generator.py

from visualization.charts import (
    commit_frequency_chart, pr_merge_rate_chart, issue_resolution_time_chart,
    open_vs_closed_issues_chart, contributors_chart, commit_per_contributor_chart
)

class ResponseGenerator:
    def __init__(self, metrics_calculator, collector):
        self.metrics_calculator = metrics_calculator
        self.collector = collector

    def generate_response(self, repo_url, metrics_list):
        """Generates the corresponding charts or metrics based on the user's query."""
        responses = []
        
        # Fetch necessary data
        commits = self.collector.get_commits(repo_url)
        pull_requests = self.collector.get_pull_requests(repo_url)
        issues = self.collector.get_issues(repo_url)
        contributors = self.collector.get_all_contributors(repo_url)
        metrics = self.metrics_calculator.get_metrics(repo_url)

        for metric in metrics_list:
            if metric == 'No. of Contributors':
                responses.append(f"{len(contributors)} Contributors")
            elif metric == 'No. of Commits':
                responses.append(f"{len(commits)} Commits")
            elif metric == 'No. of PR':
                responses.append(f"{len(pull_requests)} Pull Requests")
            elif metric == 'Remaining Issues':
                responses.append(f"{len(issues)} Issues Remaining")
            elif metric == 'commit_frequency_chart':
                responses.append(commit_frequency_chart(commits))
            elif metric == 'pr_merge_rate_chart':
                responses.append(pr_merge_rate_chart(pull_requests))
            elif metric == 'issue_resolution_time_chart':
                responses.append(issue_resolution_time_chart(issues))
            elif metric == 'open_vs_closed_issues_chart':
                responses.append(open_vs_closed_issues_chart({'open_issues_ratio': metrics['open_issues_ratio']}))
            elif metric == 'contributors_chart':
                responses.append(contributors_chart({'contributor_activity': metrics['contributor_activity']}))
            elif metric == 'commit_per_contributor_chart':
                responses.append(commit_per_contributor_chart({'avg_commits_per_contributor': metrics['avg_commits_per_contributor']}))

        return responses
