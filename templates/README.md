## NECCDC 2018 Blue Team Quick Start

The CloudFormation templates have been derived from AWS' Goldbase templates.

There are three (3) template tiers: 1) infrastructure 2) scoring 3) service

The infrastructure templates have the following design goals:
* Same deployment for team practice, qualifying, and regional event.
* Allow teams to deploy independantly into a Blue team managed account.
* Deploy all access, network, and resources required to deploy the application an scoring tiers.

Scoring templates
* This public repo will only know how to score the sample web service.
* The template will be parameterized to faciliate the services used in qualifying and regional.
* Allow testing of Black team infrastructure.

Service templates design goals
* This public repo will contain only a sample web service.
* The template will be parameterized to faciliate the services used in qualifying and regional.
* Allow testing of Black team infrastructure.

During qualifying and regional AWS organizations will used to control access.
* Only the Black with have the access rights needed to successfully deploy the infrastructure and scoring template tiers.
* Each team will be issued an account controlled by the Black team.
* AWS root credentials will be held by the Blakc team.
* One or more users/roles will be created to allow Blue teams to manage their services.

Prereqs:

* [AWS Account](https://aws.amazon.com/)
* [Git installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CLI installed and configured](http://docs.aws.amazon.com/cli/latest/userguide/installing.html)
* [Ansible installed and configured](http://docs.ansible.com/ansible/latest/intro_installation.html)


To get yourself going:

* clone this repo
* change the variable values below
* run the cloudformation command

```keyname="your-ec2-keypair-name"
az1="choose-an-availabilty-zone"
az2="choose-a-different-availabilty-zone-in-same-region"
dbpass="a-secure-password"
keyname="your-keypair"
# if you already have cloudtrail set up, leave this as false
newaccount=false

aws cloudformation create-stack --stack-name goldbase-$(date +%Y%m%d%H%M%S) \
  --template-body file://main-webapp-linux.json \
  --disable-rollback \
  --capabilities="CAPABILITY_IAM" \
  --parameters \
    ParameterKey=pKeyName,ParameterValue=$keyname \
    ParameterKey=pRegionAZ2Name,ParameterValue=$az1 \
    ParameterKey=pRegionAZ1Name,ParameterValue=$az2 \
    ParameterKey=pCreateCloudTrail,ParameterValue=$newaccount \
    ParameterKey=pDBPassword,ParameterValue=$password
```

It'll take about 30m for everything to get up and running (and probably like 25 of those are RDS.) 
