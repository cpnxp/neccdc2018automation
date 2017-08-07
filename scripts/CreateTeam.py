# Create a new blue team
import os
import boto3

# Predetermined values specific to 2018
PARENT_ID = 'ou-ej2m-9e1lj6fx'

# Default input values
TEAM_NAME = 'team0.3'
TEAM_EMAIL = teamName + '@neccdc2018.org'
TEAM_CIDR = "132.177.0.0/16"

def main():
# Read command line args
opts, args = getopt.getopt(sys.argv[1:],"n:c:e:",["name=","cidr=","email="])

for o, a in opts:
    if o in ( '-n','--name'):
        TEAM_NAME = a
    elif o in ( '-e','--email'):
        TEAM_EMAIL = a
    elif o in ( '-c','--cidr'):
        TEAM_CIDR = a
    else:
        print("Usage: %s -n name -e email -c cidr" % sys.argv[0])
        
    session = boto3.Session(profile_name='neccdc', region_name='us-east-1')
    client = session.client('organizations')
    
    response = client.create_organizational_unit(ParentId=PARENT_ID, Name=TEAM_NAME)
    
    response = client.create_account(Email='',
                                     AccountName='',
                                     RoleName='OrganizationAccountAccessRole',
                                     IamUserAccessToBilling='DENY')
        

if __name__ == '__main__':
    main()
    
