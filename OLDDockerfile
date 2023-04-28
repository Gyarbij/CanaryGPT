FROM python:3.11.3-slim-bullseye

RUN python3 -m venv /opt/venv

# Install dependencies:
COPY requirements.txt .
RUN . /opt/venv/bin/activate && pip install -r requirements.txt

# Run the application:
COPY canarygpt /app
CMD . /opt/venv/bin/activate && exec python /app/canarygpt.py