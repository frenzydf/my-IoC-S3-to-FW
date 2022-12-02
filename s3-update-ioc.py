# Updating Indicator of Compromise to a s3 txt file 
# files should be 'src/ioc.txt' for a local file with new IoCs 
# and 'cloud/actual.txt' to download actual IoCs in S3
# anyway you can edit folder and names as you wish


import boto3
#Function for write new lines 
def WriteFile(valor):
    f = open('cloud/actual.txt', "a")
    f.write('\n')
    f.write(valor)
    print(valor ,"Added to a IoC")
    f.close()

# 1. Download the IoC file from AWS S3
bucketname = input("Enter bucket name:")
print('Downloading AWS S3 File...')
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucketname)
s3.meta.client.download_file(bucketname,'ioc-fw.txt','cloud/actual.txt')
print('ioc-fw.txt File Downloaded')

# 2. Find duplicated items between local and s3 File 
print('\nProccesing Ioc in Local File:')
with open('src/ioc.txt', 'r') as f_ioc:
    for l_ioc, line_ioc in enumerate(f_ioc):
        my_ioc = line_ioc.strip()
        exist = False
        with open('cloud/actual.txt', 'r') as f_actual:
            for l_actual, line_actual in enumerate(f_actual):
                my_actual = line_actual.strip()
                if my_ioc == my_actual:
                    print(my_ioc ,"already exist")
                    exist = True
                    break
            if exist == False: 
                WriteFile(my_ioc)
    f_actual.close()
f_ioc.close()

# 3. Delete a old s3 ioc file
print('\nDeleting old ioc-fw.txt from s3 bucket...')
s3.Object(bucketname,'ioc-fw.txt').delete()
print('ioc-fw.txt file has been deleted')

# 4. Uploading the new s3 ioc file
print('\nUploading a new ioc-txt to s3 bucket...')
s3.meta.client.upload_file('src/ioc.txt',bucketname,'ioc-fw.txt')
print('ioc-fw.txt file has been updated')
