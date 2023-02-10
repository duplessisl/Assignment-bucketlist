# s3blist.py
# Author: Leon Du Plessis
# StudentID:
# Description: lists s3 buckets and saves to file
# Date: 13/10/23

import boto3


# get yes or no response yes=true no=false
def yesNoResponse():
    response = ''
    while(response != 0 and response != 1 ):
        response = input("Yes or No? ")
        response = response.lower()
        if response == "yes" or response == "y":
            return 1
        if response == "no" or  response == "n":
            return 0
        print("Please enter ", end='')
    

def main():
    FILENAME = "bucketList.txt" # File name to save the bucket list
    
    # Instantiate the connection to S3
    client = boto3.client('s3')
    
    print("Welcome, this program lists S3 buckets")
    print("\nYour default region is {}".format(client.meta.region_name))
    
    # see if default region is correct
    print("Is this region correct?")
    if(yesNoResponse()):
        print('\nList of Buckets:')
        #retrieve buckets
        response = client.list_buckets()
        bucketlist = '' # variable for saving bucket list
        bucketCount = 0 # number of buckets
        # print buckets
        for bucket in response ['Buckets']:
            print('\t' + bucket['Name'])
            # add bucket to string for saving
            bucketlist = bucketlist + bucket['Name'] + '\n'
            bucketCount = bucketCount + 1 # add one to bucket count
        # Remove useless new line
        if bucketCount > 0:
            bucketlist = bucketlist[:-1:]
        
        print('\nWould you like to save ' + str(bucketCount) + ' buckets ' + FILENAME)
        if(yesNoResponse()):
            print("\nSaving bucket list to " + FILENAME)
            # saving bucket name to file
            file1 = open(FILENAME, "w")
            file1.write(bucketlist)
            file1.close()
            
    print('Exiting')
    
main()
