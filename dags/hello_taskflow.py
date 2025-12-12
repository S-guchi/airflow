from datetime import datetime
from airflow import DAG
from airflow.decorators import task

with DAG(
    dag_id="hello_taskflow",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["intro"],
) as dag:

    @task
    def extract():
        # ここで外部からデータを取ってくる処理を書く（今回はダミー）
        return "airflow"

    @task
    def transform(text: str):
        # シンプルな変換（大文字化）
        return text.upper()

    @task
    def load(result: str):
        # 本来はDBやS3に書き込む場所（ここではログに出力）
        print(f"結果: {result}")

    load(transform(extract()))
