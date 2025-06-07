# Use an official Python runtime as a parent image
FROM python:3.12-slim-bookworm

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run the application using Uvicorn
# The --host 0.0.0.0 makes the application accessible from outside the container
# The --workers 1 is a good starting point; adjust based on your needs.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
