# Use the Python 3.13-rc-bookworm base image
FROM python:3.13-rc-bookworm

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Clone the GitHub repository
#RUN git clone git@github.com:ericmelz/synutil.git
#RUN git clone https://github.com/ericmelz/synutil.git
RUN --mount=type=cache,target=/var/cache/apt \
    rm -rf synutil && \
    git clone https://github.com/ericmelz/synutil.git


# Change directory to the cloned repository
WORKDIR /app/synutil


# Install the dependencies if requirements.txt is present
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; else echo "requirements.txt not found"; fi

# Run the unit tests
CMD ["python", "-m", "unittest", "discover", "-s", "tests", "-p", "test_dup_detector.py"]
