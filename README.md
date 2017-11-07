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
* AWS root credentials will be held by the Black team.
* One or more users/roles will be created to allow Blue teams to manage their services.

Prereqs:

* [AWS Account](https://aws.amazon.com/)
* [Git installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CLI installed and configured](http://docs.aws.amazon.com/cli/latest/userguide/installing.html)
* [Ansible installed and configured](http://docs.ansible.com/ansible/latest/intro_installation.html)


To get yourself going:

* clone this repo
* change the variable values below
* run the Ansible playbook

```ansible-playbook ./playbooks/create-team-stack.yml
```

It'll take less than 5 minutes to create the network infrastructure and IAM 

This playbook will also install a Palo Alto VM100 server.
The server is unlicensed; it will process traffic but most features are not available until a licnese is applied (separate team action).
A simple web server with SSH enabled is also deployed.

This just a practice environment, expect the qualifier and regional events to be different.
