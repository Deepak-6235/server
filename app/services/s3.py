import boto3
from botocore.exceptions import ClientError
from app.core.config import S3_ACCESS_KEY, S3_SECRET_KEY, S3_BUCKET, S3_REGION


def get_s3_client():
    """Create and return an S3 client"""
    return boto3.client(
        's3',
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_KEY,
        region_name=S3_REGION
    )


def upload_file_to_s3(file_path: str, s3_key: str) -> str:
    """
    Upload a file to S3 and return the public URL

    Args:
        file_path: Local path to the file
        s3_key: The key (path) to use in S3

    Returns:
        Public URL of the uploaded file
    """
    try:
        s3_client = get_s3_client()

        # Upload the file with public-read ACL
        s3_client.upload_file(
            file_path,
            S3_BUCKET,
            s3_key,
            ExtraArgs={'ContentType': 'video/mp4', 'ACL': 'public-read'}
        )

        # Generate the public URL
        url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{s3_key}"

        return url

    except ClientError as e:
        print(f"Error uploading to S3: {e}")
        raise


def upload_video_bytes_to_s3(video_bytes: bytes, s3_key: str, content_type: str = 'video/mp4') -> str:
    """
    Upload bytes directly to S3 and return the public URL

    Args:
        video_bytes: Content as bytes
        s3_key: The key (path) to use in S3
        content_type: MIME type of the content (default: video/mp4)

    Returns:
        Public URL of the uploaded file
    """
    try:
        s3_client = get_s3_client()

        # Upload the bytes with public-read ACL
        # Using put_object for direct upload (faster than upload_file)
        s3_client.put_object(
            Bucket=S3_BUCKET,
            Key=s3_key,
            Body=video_bytes,
            ContentType=content_type,
            ACL='public-read',
            # Add metadata to cache for faster delivery
            CacheControl='max-age=31536000',  # Cache for 1 year
        )

        # Generate the public URL
        url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{s3_key}"

        return url

    except ClientError as e:
        print(f"Error uploading to S3: {e}")
        raise


def upload_stream_to_s3(file_stream, s3_key: str, content_length: int = None) -> str:
    """
    Upload a file stream directly to S3 without saving to disk

    Args:
        file_stream: File-like object or stream
        s3_key: The key (path) to use in S3
        content_length: Optional content length for optimization

    Returns:
        Public URL of the uploaded file
    """
    try:
        s3_client = get_s3_client()

        extra_args = {
            'ContentType': 'video/mp4',
            'ACL': 'public-read',
            'CacheControl': 'max-age=31536000',
        }

        # Direct stream upload - no temp file needed
        s3_client.upload_fileobj(
            file_stream,
            S3_BUCKET,
            s3_key,
            ExtraArgs=extra_args
        )

        # Generate the public URL
        url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{s3_key}"

        return url

    except ClientError as e:
        print(f"Error uploading stream to S3: {e}")
        raise
