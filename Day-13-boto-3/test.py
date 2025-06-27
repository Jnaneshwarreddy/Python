import boto3


client = boto3.client('s3')

# response = client.create_bucket(
#     Bucket='aws-s3-jnani1',

# )

response = client.get_bucket_acl(
    Bucket='aws-s3-jnani1',
    )

print(response)
