# Use Python 3.8 as a parent image
FROM python:3.8.2

# Set the timezone
ENV TZ=Europe/Malta
# Add a command to print memory usage
RUN echo "Memory usage before installation:" && free -m && echo ""



# Set the working directory in the container
WORKDIR /app


# Create and activate a virtual environment
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"



# Copy the requirements file into the container at /app
COPY requirements.txt .

# let's updgrade pip with proper protobuf
RUN pip install --upgrade pip
RUN pip install --upgrade protobuf==3.20.0

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Debug cat the current package ...
RUN echo "Current package , check check:" && pip freeze

# Add another command to print memory usage after installation
RUN echo "Memory usage after installation:" && free -m

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python3", "my_app.py"]

