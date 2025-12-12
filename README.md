# airflow

Apache Airflow 3.1.3 の学習用プロジェクト

## 公式ドキュメント
https://airflow.apache.org/docs/apache-airflow/stable/start.html

## 立ち上げ方法

### Docker Compose で起動（推奨）

最小構成でAirflowを起動できます。

```bash
# 必要なディレクトリを作成
mkdir -p ./logs ./plugins

# ビルド・起動
docker-compose up -d

# ログを確認
docker-compose logs -f airflow

# 停止
docker-compose down

# 完全削除（ボリュームも含む）
docker-compose down -v
```

起動後、以下のURLでWebUIにアクセスできます:
- URL: http://localhost:8080
- ユーザー名: `airflow`
- パスワード: `airflow`

### ローカル環境で起動

以下実行すると8080のポートでwebuiを確認できる

```bash
airflow standalone
```

## 構成

- **Executor**: LocalExecutor（学習用の最小構成）
- **Database**: PostgreSQL 15
- **DAGs**: `./dags` ディレクトリ配下
- **Logs**: `./logs` ディレクトリ配下
- **Plugins**: `./plugins` ディレクトリ配下

## その他の便利なコマンド

```bash
# コンテナ内でAirflow CLIを実行
docker-compose exec airflow airflow dags list

# DAGをテスト実行
docker-compose exec airflow airflow dags test <dag_id> <execution_date>

# コンテナに入る
docker-compose exec airflow bash
```


# airflow
