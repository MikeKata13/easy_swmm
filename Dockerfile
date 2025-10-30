# Use Python 3.14 slim image
FROM python:3.14-slim

# Set working directory
WORKDIR /app

# Copy source and examples
COPY src/ src/
COPY examples/ examples/
COPY tests/ tests/

# Install dev dependencies
RUN pip install --upgrade pip uvicorn fastapi pytest

# Default command: interactive shell
CMD ["bash"]
