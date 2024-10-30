
# GitHub Repository Metrics App



This project is a Streamlit-based app that collects, calculates, and visualizes GitHub repository metrics. Users can input a GitHub organization and repository to see various KPIs and charts related to the repository's metrics.

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone <your-repository-url>
    ```

2. Navigate to the project folder:
    ```bash
    cd <project-folder>
    ```

3. Install the required dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

## Python Version

Ensure you are using Python **version < 3.9** for compatibility with the libraries used in this project.

## Environment Setup

1. Inside the project folder, locate the `.env.example` file.
2. Rename the `.env.example` file to `.env`.
3. Open the `.env` file and replace `<your-github-api-key>` with your GitHub API key:
    ```bash
    GIT_TOKEN=<your-github-api-key>
    ```

## Running the App

1. Open the project folder in your terminal.
2. Run the Streamlit app with one of the following commands:
    ```bash
    streamlit run app.py
    ```
    or
    ```bash
    streamlit run main.py
    ```

The app will launch in your default web browser. Follow the on-screen instructions to input a GitHub organization and repository name to view metrics and charts.
