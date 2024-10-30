
import streamlit as st
from datacollection.git_api import Collector
from metrics.calculator import MetricsCalculator
from visualization.dashboard import display_dashboard
from query_interface.nlp_processor import NLPProcessor
nlp_processor = NLPProcessor()

from query_interface.response_generator import ResponseGenerator
import os
from datacollection.data_storage import DataStorage


token = os.environ.get("GIT_TOKEN")
credentials = [token]
collector = Collector(credentials)
data_storage = DataStorage()  
metrics_calculator = MetricsCalculator(data_storage)  
response_generator = ResponseGenerator(metrics_calculator, collector)

st.title("AI-Powered Developer Performance Analytics Dashboard")

org_name = st.text_input("Enter GitHub Organization Name", "surveysparrow")

query = st.text_input("Ask a question about the repository metrics:")

if org_name:
    with st.spinner("Fetching repositories..."):
        try:
            repos = collector.get_org_repos(org_name)
            st.session_state['repos'] = repos
            st.success(f"Fetched {len(repos)} repositories!")
        except Exception as e:
            st.error(f"Error fetching repositories: {str(e)}")

if 'repos' in st.session_state:
    repo_url = st.selectbox(
        "Select a repository",
        options=st.session_state['repos'],
        help="Scroll and search to find a repository"
    )

    if repo_url:
        display_dashboard(org_name, repo_url)

if query:
    metrics_list = nlp_processor.process_query(query)
    if metrics_list:
        with st.spinner("Fetching data based on your query..."):
            try:
                responses = response_generator.generate_response(repo_url, metrics_list)
                for response in responses:
                    if isinstance(response, str):
                        st.write(response)
                    else:
                        st.plotly_chart(response)
            except Exception as e:
                st.error(f"Error generating response: {str(e)}")
