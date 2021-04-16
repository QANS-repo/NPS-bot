# Extend the official Rasa SDK image
# https://hub.docker.com/r/rasa/rasa-sdk

FROM rasa/rasa-sdk:1.10.3

WORKDIR /app
# Change back to root user to install dependencies
USER root

# To install packages from PyPI
RUN pip install --no-cache-dir gspread
# https://pypi.org/project/gspread/  to access Google sheet

COPY ./actions /app/actions

# Switch back to non-root to run code
USER 1001