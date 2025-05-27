from aiobotocore.session import get_session
from contextlib import asynccontextmanager
from store.store_config import ACCESS_KEY, SECRET_KEY, URL, BUCKET
class S3Client:
    def __init__(self, secretKey: str, accesskKey: str, serverUrl: str, bucketName: str):
        self.aws_access_key_id=accesskKey,
        self.aws_secret_access_key=secretKey,
        self.endpoint_url=serverUrl
        self.bucketName = bucketName
        self.session = get_session()
    
    async def upload(self,  content:bytes, filename:str):
        try:
            async with self.session.create_client("s3",    
                        endpoint_url= URL,     
                        aws_access_key_id= ACCESS_KEY,
                        aws_secret_access_key= SECRET_KEY,
                        verify=False ) as client:
                    resp = await client.put_object(
                        Bucket= BUCKET,
                        Key= f"images//{filename}",
                        Body= content)
                    print(resp)
        except Exception as e:
            print(e)