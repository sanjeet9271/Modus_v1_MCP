FROM python:3.11-slim

WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and knowledge base
COPY src/ ./src/
COPY Knowledge\ Base/ ./Knowledge\ Base/
COPY trimble-logo-rev.svg ./

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Expose the port the MCP server runs on
EXPOSE 3001

# Command to run the MCP server
CMD ["python", "src/ModusFromMCP.py"]
