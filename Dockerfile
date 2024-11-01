# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install SQLite and necessary dependencies
RUN apt-get update && \
    apt-get install -y sqlite3 libsqlite3-dev
    
# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (replace 8501 if using a different one for Streamlit)
EXPOSE 8501

# Initialize the database
RUN python3 config/init_db.py

# Expose port (replace 8501 if using a different one for Streamlit)
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "main.py"]
