# query_interface/nlp_processor.py

class NLPProcessor:
    def __init__(self):
        self.keywords = {
            'contributors': 'No. of Contributors',
            'commits': 'No. of Commits',
            'pull requests': 'No. of PR',
            'issues': 'Remaining Issues',
            'commit frequency': 'commit_frequency_chart',
            'pull request merge rate': 'pr_merge_rate_chart',
            'issue resolution time': 'issue_resolution_time_chart',
            'open vs closed issues': 'open_vs_closed_issues_chart',
            'contributor activity': 'contributors_chart',
            'commits per contributor': 'commit_per_contributor_chart',
        }

    def process_query(self, query):
        """Match user query to defined metrics or charts."""
        matched_metrics = []
        query_lower = query.lower()

        # Simple keyword matching
        for keyword, metric in self.keywords.items():
            if keyword in query_lower:
                matched_metrics.append(metric)

        return matched_metrics
