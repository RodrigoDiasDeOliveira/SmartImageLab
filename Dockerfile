# ---------- build stage ----------
FROM python:3.11-slim AS builder
ENV PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git && rm -rf /var/lib/apt/lists/*
COPY pyproject.toml README.md ./
COPY ImageLab ./ImageLab
RUN pip install --prefix=/install ".[dev]" && \
    pip install --prefix=/install .

# ---------- runtime stage ----------
FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 \
    PATH="/install/bin:$PATH" PYTHONPATH="/app/ImageLab"
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 libglib2.0-0 && rm -rf /var/lib/apt/lists/* && \
    useradd -m app
COPY --from=builder /install /install
COPY ImageLab ./ImageLab
USER app
ENTRYPOINT ["python", "-m", "src"]
CMD ["--help"]
