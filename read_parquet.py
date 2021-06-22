from azure.storage.blob import BlobServiceClient
import pyarrow as pa
import pyarrow.parquet as pq
from io import BytesIO
import pandas as pd

# azure-storage-blob
G_INTERVAL = 'Major'
G_INTERVAL = 'Minor'


def load_blob(file):
    stream_downloader = blob_container_client.download_blob(file)
    stream = BytesIO()
    stream_downloader.readinto(stream)
    df = pd.read_parquet(stream, engine='pyarrow')
    return df

major_am_data = pd.DataFrame()

conn_str = "DefaultEndpointsProtocol=https;AccountName=stdnrsdevelopmentvar;AccountKey=tiLgzC+Sg5pHWhJmEpJBkR3DFTe8UI5JemDc4k3HZPCzJBjSASr5kE832Ym6RTI6Jx9FmTxfnpuLMFVg/MK/gQ==;EndpointSuffix=core.windows.net" 

blob_service_client = BlobServiceClient.from_connection_string(conn_str)
if G_INTERVAL == 'Major':
    blob_container_client = blob_service_client.get_container_client('noise-data-processed')
elif G_INTERVAL == 'Minor':
    blob_container_client = blob_service_client.get_container_client('noise-data-processed-ten-secondly')
else:
    print('G_INTERVAL not understood: ',G_INTERVAL)

all_blobs = list(blob_container_client.list_blobs())
processed_files = [f['name'] for f in all_blobs]

for file in processed_files:
    df = load_blob(file)
    major_am_data = major_am_data.append(df)

# print(major_am_data)
major_am_data.to_csv("E:\Vardafjellet\Misc\Matthew_AM_10sec.csv")