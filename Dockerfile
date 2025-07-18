FROM ubuntu:22.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    build-essential cmake libfmt-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy C++ and build
COPY CMakeLists.txt .
COPY cpp/ ./cpp/
RUN cmake -S . -B build && cmake --build build

# Copy binary to /app/
RUN cp build/my_cpp_app /app/ && chmod +x /app/my_cpp_app

# Copy Python code directly to /app
COPY app/ .

# Run Python API
CMD ["python3", "main.py"]
