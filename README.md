# FortiGate Indicators of Compromise consumed from AWS S3
Updating Indicators of Compromise (IP address) to a AWS S3 txt file cosumed by FortiGate.
Sometimes we have Indicator of compromise (IP address) to deny in our FortiGates and is very complicated to update them all manualy.
This python script help me to update all IoC IP addres automatically just adding the IoCs to a text file.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
If you have a FortiGate, AWS account and IoCs to update use this script. 
files should be 'src/ioc.txt' for a local file with new IoCs and 'cloud/actual.txt' to download actual IoCs in S3. 
Anyway you can edit folder and names as you wish
	
## Technologies
Project is created with:
* Python 3.10.8
* Boto3 lib
AWS Bucket S3
* AWS CLI. Please check https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
	
## Setup
### Script 
- To run this project, use it locally using python3
- Use folder src/ to put your new IoCs in file named 'ioc.txt'
- Create a txt file and folder named cloud/ to download your S3 text file 

```
$ cd ../lorem
$ npm install
$ npm start
```
## To Do
Validation of the new IP address are correctly.
