# dashboard.py

import streamlit as st
from datacollection.git_api import Collector
from datacollection.data_storage import DataStorage
from metrics.calculator import MetricsCalculator
from visualization.charts import (
    commit_frequency_chart, pr_merge_rate_chart, issue_resolution_time_chart,
    contributors_chart, commit_per_contributor_chart, open_vs_closed_issues_chart
)
import os

def display_dashboard(org_name, repo_url):
    # Initialize Collector and MetricsCalculator classes
    token = os.environ.get("GIT_TOKEN")
    credentials = [token]
    collector = Collector(credentials)
    data_storage = DataStorage()
    metrics_calculator = MetricsCalculator(data_storage)

    st.write(f"Selected Repository: {repo_url}")

    # Fetch and display data
    with st.spinner("Fetching data..."):
        try:
            # Fetch all required data
            contributors = collector.get_all_contributors(repo_url)
            commits = collector.get_commits(repo_url)
            pull_requests = collector.get_pull_requests(repo_url)
            issues = collector.get_issues(repo_url)

            # Calculate metrics
            metrics = metrics_calculator.get_metrics(repo_url)

            # Display Dashboard
            st.write("## Repository Metrics Dashboard")

            # Key Metrics (KPIs)
            kpi1, kpi2, kpi3, kpi4 = st.columns(4)
            kpi1.metric(label="No. of Contributors", value=f"{len(contributors)}")
            kpi2.metric(label="No. of Commits", value=f"{len(commits)}")
            kpi3.metric(label="No. of PR", value=f"{len(pull_requests)}")
            kpi4.metric(label="Remaining Issues", value=f"{len(issues)}")

            # Important Charts
            st.markdown("### Important Charts 📈")
            chart1, chart2 = st.columns(2)
            chart1.plotly_chart(commit_frequency_chart(commits))
            chart2.plotly_chart(pr_merge_rate_chart(pull_requests))

            chart3, chart4 = st.columns(2)
            chart3.plotly_chart(issue_resolution_time_chart(issues))
            chart4.plotly_chart(open_vs_closed_issues_chart({'open_issues_ratio': metrics['open_issues_ratio']}))

            chart5, chart6 = st.columns(2)
            chart5.plotly_chart(contributors_chart({'contributor_activity': metrics['contributor_activity']}))
            chart6.plotly_chart(commit_per_contributor_chart({'avg_commits_per_contributor': metrics['avg_commits_per_contributor']}))

        except Exception as e:
            st.error(f"Error fetching or calculating data: {str(e)}")
