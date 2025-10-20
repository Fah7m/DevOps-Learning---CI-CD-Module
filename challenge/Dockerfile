# stage 1: build stage
FROM python:3.8-slim AS build

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc python3-dev pkg-config \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip \
 && pip install --prefix=/install -r requirements.txt

COPY . .

# stage 2: production stage
FROM python:3.8-slim AS prod

WORKDIR /app

# Copy installed Python packages from build stage
COPY --from=build /install /usr/local

# Copy only app code
COPY . .

EXPOSE 5002

CMD ["python", "app.py"]