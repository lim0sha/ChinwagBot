# Use official Python image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Copy dependencies first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Set environment variables
ENV PORT=8080
EXPOSE 8080

# Run the bot
CMD ["python", "bot.py"]
