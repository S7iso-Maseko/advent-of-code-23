#!/usr/bin/env bash

export aws_region="eu-west-1"


# Update the system

yum update -y

#Install jq, git and aws-cli
yum install jq git aws-cli -y


export secret_id=$(aws ec2 describe-instances --instance-id $(curl -s http://169.254.169.254/latest/meta-data/instance-id) --query "Reservations[*].Instances[*].Tags[?Key=='BitBucketSMKey'].Value" --region $aws_region --output text)


amazon-linux-extras install docker
service docker start

echo "Starting SSH Agent"
eval $(ssh-agent -s)


mkdir -p ~/.ssh

echo "Reading keypair from SM"
echo "$(echo $(aws secretsmanager get-secret-value --secret-id $secret_id --query SecretString --output text --region $aws_region) | jq -r '.public_key')"  > ~/.ssh/id_rsa.pub
echo "$(echo $(aws secretsmanager get-secret-value --secret-id $secret_id --query SecretString --output text --region $aws_region) | jq -r '.private_key')"  > ~/.ssh/id_rsa

echo "Setting permissions"
chmod 600 ~/.ssh/id_rsa
chmod 600 ~/.ssh/id_rsa.pub

echo "Adding key"
ssh-add ~/.ssh/id_rsa

echo "Trusting BitBucket"
ssh-keyscan bitbucket.org >> ~/.ssh/known_hosts

# TODO: Run stack as ec2-user
#usermod -a -G docker ec2-user

# su - ec2-user <<EOF

# echo "Starting SSH Agent"
# eval $(ssh-agent -s)
# printenv

# mkdir -p ~/.ssh

# echo "Reading keypair from SM"
# echo "$(echo $(aws secretsmanager get-secret-value --secret-id $secret_id --query SecretString --output text --region $aws_region) | jq -r '.public_key')"  > ~/.ssh/id_rsa.pub
# echo "$(echo $(aws secretsmanager get-secret-value --secret-id $secret_id --query SecretString --output text --region $aws_region) | jq -r '.private_key')"  > ~/.ssh/id_rsa

# echo "Setting permissions"
# chmod 600 ~/.ssh/id_rsa
# chmod 600 ~/.ssh/id_rsa.pub

# echo "Adding key"
# ssh-add ~/.ssh/id_rsa

# echo "Trusting BitBucket"
# ssh-keyscan bitbucket.org >> ~/.ssh/known_hosts

# EOF

sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/bin/docker-compose
sudo chmod +x /usr/bin/docker-compose
docker-compose version

mkdir ~/sustainable-timesheets
cd ~/sustainable-timesheets
git clone git@bitbucket.org:synthesis_admin/sustainable-timesheets-app.git
cd ~/sustainable-timesheets/sustainable-timesheets-app
docker-compose up -d


# TODO: Run stack as ec2-user
# su - ec2-user <<EOF

# mkdir -p /home/ec2-user/sustainable-timesheets
# cd /home/ec2-user/sustainable-timesheets

# cd /home/ec2-user/sustainable-timesheets
# git clone git@bitbucket.org:synthesis_admin/sustainable-timesheets-app.git
# cd sustainable-timesheets-app
# docker-compose up -d
# EOF