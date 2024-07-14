import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('Akashat.png','akashat'),
      ('Devang.png','Devang'),
      ('Jibran_Sir.png','Jibran Sir'),
      ('Pragya.png','Pragaya'),
      ('Vimal_Sir.jpeg','VImal Sir'),
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('chehrabucket','index/'+ image[0])      // here you have to write bucket name and file name .
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})
