import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def commit_frequency_chart(commit_data):
    """Creates a line chart for commit frequency with enhanced styling."""
    df = pd.DataFrame(commit_data)
    df['date'] = pd.to_datetime(df['date'])
    df['date'] = df['date'].dt.date
    
    daily_commits = df.groupby('date').size().reset_index(name='commits')
    
    fig = px.line(
        daily_commits,
        x='date',
        y='commits',
        labels={'date': 'Date', 'commits': 'Number of Commits'},
        title='Commit Frequency Over Time',
        line_shape='linear',  # Adds a smooth line
        markers=True,  # Adds markers to each data point
        template='plotly_dark'  # Sets a dark theme
    )
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Number of Commits',
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True
        ),
        yaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True
        )
    )
    return fig

def pr_merge_rate_chart(pr_data):
    """Creates a pie chart for PR merge rate with enhanced styling."""
    df = pd.DataFrame(pr_data)
    merged = df['merged_at'].notnull().sum()
    total = len(df)
    merge_rate = (merged / total) * 100 if total > 0 else 0
    
    fig = px.pie(
        names=['Merged', 'Not Merged'],
        values=[merged, total - merged],
        title=f'PR Merge Rate: {merge_rate:.2f}%',
        color_discrete_sequence=['#4CAF50', '#FFC107'],  # Colors for the pie chart
        hole=0.3  # Creates a donut chart
    )
    fig.update_traces(
        textinfo='percent+label',
        marker=dict(line=dict(color='#000000', width=2))  # Adds border to pie slices
    )
    return fig

def issue_resolution_time_chart(issue_data):
    """Creates a histogram for issue resolution time with enhanced styling."""
    df = pd.DataFrame(issue_data)
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['closed_at'] = pd.to_datetime(df['closed_at'])
    df['resolution_time'] = (df['closed_at'] - df['created_at']).dt.days
    
    fig = px.histogram(
        df,
        x='resolution_time',
        labels={'resolution_time': 'Resolution Time (days)'},
        title='Distribution of Issue Resolution Time',
        nbins=20,  # Sets the number of bins
        color_discrete_sequence=['#2196F3']  # Color for the histogram bars
    )
    fig.update_layout(
        xaxis_title='Resolution Time (days)',
        yaxis_title='Count',
        xaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True
        ),
        yaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True
        )
    )
    return fig

def contributors_chart(contributor_data):
    """Creates a bar chart for contributor activity with enhanced styling."""
    fig = px.bar(
        x=list(contributor_data.keys()),
        y=list(contributor_data.values()),
        labels={'x': 'Contributor', 'y': 'Activity'},
        title='Contributor Activity',
        color_discrete_sequence=['#FF5722'],  # Color for the bars
        text_auto=True  # Adds value labels to bars
    )
    fig.update_layout(
        xaxis_title='Contributor',
        yaxis_title='Activity',
        xaxis=dict(
            tickangle=-45,  # Rotates x-axis labels
            showline=True,
            showgrid=False,
            showticklabels=True
        ),
        yaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True
        )
    )
    return fig

def commit_per_contributor_chart(data):
    """Creates a gauge chart for commits per contributor."""
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=data['avg_commits_per_contributor'],
            title={'text': 'Average Commits Per Contributor'},
            gauge={
                'axis': {'range': [None, max(10, data['avg_commits_per_contributor'] + 10)]},
                'bar': {'color': '#8BC34A'},
                'steps': [
                    {'range': [0, data['avg_commits_per_contributor']], 'color': '#D3E5D5'},
                ]
            }
        )
    )
    fig.update_layout(
        template='plotly_dark'
    )
    return fig

def pr_response_time_chart(data):
    """Creates a gauge chart for PR acceptance rate."""
    acceptance_rate = data['pr_acceptance_rate'] * 100
    
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=acceptance_rate,
            title={'text': 'PR Acceptance Rate'},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': '#FFC107'},
                'steps': [
                    {'range': [0, acceptance_rate], 'color': '#FFE0B2'},
                ]
            }
        )
    )
    fig.update_layout(
        template='plotly_dark'
    )
    return fig

def open_vs_closed_issues_chart(data):
    """Creates a pie chart for open vs closed issues with enhanced styling."""
    open_issues = data['open_issues_ratio'] * 100
    closed_issues = 100 - open_issues
    
    fig = px.pie(
        names=['Open Issues', 'Closed Issues'],
        values=[open_issues, closed_issues],
        title=f'Open vs Closed Issues: {open_issues:.2f}% Open',
        color_discrete_sequence=['#FF5722', '#9E9E9E'],  # Colors for the pie chart
        hole=0.3  # Creates a donut chart
    )
    fig.update_traces(
        textinfo='percent+label',
        marker=dict(line=dict(color='#000000', width=2))  # Adds border to pie slices
    )
    return fig
