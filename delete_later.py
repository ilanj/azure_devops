from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

def upload_image_to_blob(storage_account_name, storage_account_key, container_name, local_image_path, blob_name):
    # Construct the connection string
    connection_string = f"DefaultEndpointsProtocol=https;AccountName=myblobstorageaccount;AccountKey=abcdefghijklmno1234567890pqrstuvwxyza1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5zA==;EndpointSuffix=core.windows.net"

    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Create a ContainerClient
    container_client = blob_service_client.get_container_client(container_name)

    # Create a blob client
    blob_client = container_client.get_blob_client(blob_name)

    # Upload the image
    with open(local_image_path, "rb") as data:
        blob_client.upload_blob(data)
    # print()

if __name__ == "__main__":
    # Replace these values with
    upload_image_to_blob()
