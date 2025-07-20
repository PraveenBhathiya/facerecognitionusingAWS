import boto3

s3 = boto3.resource('s3')
bucket_name = 'facebucketapp'

# List of images and their associated cricketer names
images = [
    ('image_01.jpg', 'Virat Kohli'),
    ('image_02.jpg', 'Virat Kohli'),
    ('image_03.jpg', 'Virat Kohli'),
    ('image_04.jpg', 'Virat Kohli'),
    ('image_05.jpg', 'Mahendra singh dhoni'),
    ('image_06.jpg', 'Mahendra singh dhoni'),
    ('image_07.jpg', 'Mahendra singh dhoni'),
    ('image_08.jpg', 'Mahendra singh dhoni'),
    ('image_09.jpg', 'Rohit sharma'),
    ('image_10.jpg', 'Rohit sharma'),
    ('image_11.jpg', 'Rohit sharma'),
    ('image_12.jpg', 'Rohit sharma'),
    ('image_13.jpg', 'Ben stokes'),
    ('image_14.jpg', 'Ben stokes'),
    ('image_15.jpg', 'Ben stokes'),
    ('image_16.jpg', 'Kane Williamson'),
    ('image_17.jpg', 'Jos Buttler'),
    ('image_18.jpg', 'DevOpsMaster'),
    ('image_19.jpg', 'DevOpsMaster')
]

# Upload each image to the S3 bucket with metadata
for image in images:
    try:
        with open(image[0], 'rb') as file:
            object = s3.Object(bucket_name, 'images/' + image[0])
            object.put(Body=file, Metadata={'FullName': image[1]})
            print(f"✅ Uploaded {image[0]} as {image[1]}")
    except Exception as e:
        print(f"❌ Failed to upload {image[0]}: {str(e)}")
