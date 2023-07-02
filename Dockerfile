# Pythonイメージをベースにする
FROM python:3.10
LABEL org.opencontainers.image.source=https://github.com/geekcamp2023-vol5-team31/backend

# 環境変数を設定する。これによりPythonがバッファリングを無効にし、メッセージが即時にコンソールに出力されます
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ワーキングディレクトリを設定
WORKDIR /code

# 依存関係をインストール
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# プロジェクトコードをコンテナにコピー
COPY . /code/