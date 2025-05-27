from aiobotocore.session import get_session
from contextlib import asynccontextmanager

class S3Client:
    def __init__(self, secretKey: str, accesskKey: str, serverUrl: str, bucketName: str):
        self.config = {
            "aws_access_key_id": accesskKey,
            "aws_secret_access_key": secretKey,
            "endpoint_url": serverUrl
        }
        self.bucketName = bucketName
        self.session = get_session()
    
    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config) as client:
            yield client

    async def upload(self, content: bytes, filename:str):
        async with self.get_client() as client:
            client.put_object(
                Bucket = self.bucketName,
                Key = filename,
                Body = content)