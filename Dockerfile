FROM ubuntu:latest

# Update package lists and install necessary packages
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev build-essential

# Copy requirements.txt separately to leverage Docker caching
COPY requirements.txt /app/requirements.txt

# Set the working directory
WORKDIR /app

# Install pip dependencies with retries and timeouts
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port
EXPOSE 5000

# Set the entry point for the container
ENTRYPOINT ["python3"]

# Specify the default command to run when the container starts
CMD ["app.py"]
