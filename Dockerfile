FROM python:3.12-slim-bookworm

# Install uv using pip (recommended)
RUN pip install uv

# Set the working directory inside the container
WORKDIR /app

# Copy pyproject.toml and src/ first for caching
COPY pyproject.toml .
COPY uv.lock .

# Sync the project using the frozen lockfile (if you have one)
RUN uv sync --frozen

# Get the rest of the source code
COPY src/ ./src/

# CMD instruction to run when the container starts
CMD ["uv", "run", "src/main.py"]