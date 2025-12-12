FROM apache/airflow:3.1.3-python3.10

USER root

# タイムゾーン設定
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

USER airflow

# 依存関係のインストール
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# DAGsディレクトリのコピー
COPY --chown=airflow:root ./dags /opt/airflow/dags
