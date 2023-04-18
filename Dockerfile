FROM python:3.9
WORKDIR /app
RUN pip install flask
COPY MainScores.py .
COPY Utils.py .
COPY Scores.txt .
# Expose the port the app runs on
EXPOSE 5000
# Start the Flask app
CMD ["python", "MainScores.py"]