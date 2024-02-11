FROM python:3.9-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME

# Copy function code
COPY . ./

# Install the specified packages
RUN pip install -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD  ["streamlit", "run", "Home.py"]