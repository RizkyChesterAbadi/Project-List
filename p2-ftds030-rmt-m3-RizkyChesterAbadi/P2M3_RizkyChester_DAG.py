from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime
from sqlalchemy import create_engine  # Koneksi ke PostgreSQL
import pandas as pd
from elasticsearch import Elasticsearch

# Define load csv
def load_csv_to_postgres():
    database = "postgres"
    username = "postgres"
    password = "postgres"
    host = "postgres"

    # Membuat URL koneksi PostgreSQL
    postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"

    # Gunakan URL ini saat membuat koneksi SQLAlchemy
    engine = create_engine(postgres_url)
    conn = engine.connect()

    df = pd.read_csv(r'D:\DATA Science FTDS\DATA\DEBlitz\MLPipeline2\P2M3_RizkyChester_data_raw.csv')
    df.to_sql('table_m3', conn, index=False, if_exists='replace')  # Mengganti nama tabel menjadi 'table_m3'

def ambil_data():
    # Fetch data
    database = "postgres"
    username = "postgres"
    password = "postgres"
    host = "postgres"

    # Membuat URL koneksi PostgreSQL
    postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"

    # Gunakan URL ini saat membuat koneksi SQLAlchemy
    engine = create_engine(postgres_url)
    conn = engine.connect()

    df = pd.read_sql_query("SELECT * FROM table_m3", conn)  # Menggunakan nama tabel 'table_m3'
    df.to_csv(r'D:\DATA Science FTDS\DATA\DEBlitz\MLPipeline2\P2M3_RizkyChester_data_new.csv', sep=',', index=False)

def preprocess_column_names(df):
    new_columns = []
    for col in df.columns:
        # Ubah semua huruf menjadi kecil
        col = col.lower()
        # Ganti spasi dengan underscore
        col = col.replace(' ', '_')
        # Hapus karakter yang tidak diperlukan
        col = ''.join(e for e in col if e.isalnum() or e == '_')
        new_columns.append(col)
    df.columns = new_columns
    return df

def preprocessing():
    ''' Fungsi untuk membersihkan data '''
    data = pd.read_csv(r'D:\DATA Science FTDS\DATA\DEBlitz\MLPipeline2\P2M3_RizkyChester_data_new.csv')

    # Bersihkan nama kolom
    data = preprocess_column_names(data)

    # Bersihkan data
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)

    # Menangani missing values (contoh: mengganti NaN pada kolom numerik dengan rata-rata, pada kolom string dengan 'Unknown')
    for col in data.select_dtypes(include=['float64', 'int64']).columns:
        data[col].fillna(data[col].mean(), inplace=True)

    for col in data.select_dtypes(include=['object']).columns:
        data[col].fillna('Unknown', inplace=True)

    data.to_csv('/opt/airflow/dags/P2M3_RizkyChester_data_clean.csv', index=False)

def upload_to_elasticsearch():
    es = Elasticsearch("http://elasticsearch:9200")
    df = pd.read_csv(r'D:\DATA Science FTDS\DATA\DEBlitz\MLPipeline2\P2M3_RizkyChester_data_clean.csv')
    
    for i, r in df.iterrows():
        doc = r.to_dict()  # Convert the row to a dictionary
        res = es.index(index="table_m3", id=i+1, body=doc)
        print(f"Response from Elasticsearch: {res}")

default_args = {
    'owner': 'Irfan',
    'start_date': datetime(2023, 12, 24, 12, 00)
}

with DAG(
    "P2M3_RizkyChester_DAG",  # Atur sesuai nama project kalian
    description='Milestone_3',
    schedule_interval='10 5 10 * *',  # Atur schedule untuk menjalankan Airflow
    default_args=default_args,
    catchup=False
) as dag:
    # Task : 1
    load_csv_task = PythonOperator(
        task_id='load_csv_to_postgres',
        python_callable=load_csv_to_postgres
    )
    
    # Task : 2
    ambil_data_pg = PythonOperator(
        task_id='ambil_data_postgres',
        python_callable=ambil_data
    )
    
    # Task : 3
    edit_data = PythonOperator(
        task_id='edit_data',
        python_callable=preprocessing
    )

    # Task : 4
    upload_data = PythonOperator(
        task_id='upload_data_elastic',
        python_callable=upload_to_elasticsearch
    )

    # Proses untuk menjalankan di Airflow
    load_csv_task >> ambil_data_pg >> edit_data >> upload_data
