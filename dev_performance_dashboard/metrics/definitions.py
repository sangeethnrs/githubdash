# Define terms for the metrics
METRIC_DEFINITIONS = {
    'avg_commit_contributors': "The average number of unique contributors per commit.",
    'pr_acceptance_rate': "The ratio of merged pull requests to total pull requests, expressed as a percentage.",
    'contributor_activity': "The sum of unique contributors based on commits and PR authorship.",
    'top_contributors': "The top 10 contributors based on the number of commits.",
    'issue_fix_rate': "The percentage of closed issues out of total issues.",
    'commit_growth': "The number of commits made over time, grouped by month.",
    'pr_merge_time': "The average time (in hours) it takes to merge a pull request.",
    'issue_resolution_time': "The average time (in hours) it takes to resolve (close) an issue.",
    'open_closed_issues': "The number of open vs closed issues in the repository.",
    'inactive_contributors': "Contributors who have not made a commit in the last 6 months.",
    'avg_changes_per_commit': "The average number of code changes (additions + deletions) per commit.",
    'code_reviews_pr': "The number of code reviews per pull request.",
    'active_inactive_prs': "The number of active vs merged or closed pull requests.",
    'issue_comments': "The number of comments per issue.",
    'bug_non_bug_issues': "The proportion of issues labeled as bugs vs non-bugs."
}
COMMIT_FREQUENCY = "commit_frequency"
PR_MERGE_RATE = "pr_merge_rate"
ISSUE_RESOLUTION_TIME = "issue_resolution_time"
CONTRIBUTOR_ACTIVITY = "contributor_activity"
TOP_CONTRIBUTORS = "top_contributors"
AVG_COMMITS_PER_CONTRIBUTOR = "avg_commits_per_contributor"
PR_ACCEPTANCE_RATE = "pr_acceptance_rate"
OPEN_ISSUES_RATIO = "open_issues_ratio"
BUG_NON_BUG_ISSUES = "bug_non_bug_issues"
COMMIT_GROWTH = "commit_growth"
INACTIVE_CONTRIBUTORS = "inactive_contributors"
ISSUE_COMMENTS = "issue_comments"