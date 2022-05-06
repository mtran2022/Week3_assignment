This application is design to assess the sentiment of a given comment.

#### Install packages in WSL2 Ubuntu Root
```
sudo apt update
sudo apt install python3-pip python3-dev
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv

#### Install Docker
````
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

#### Add Docker user and start service
````
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
sudo service docker start
docker run hello-world

#### Install git and clone this repo
```
sudo apt install git
git clone https://github.com/mtran2022/Week3_assignment.git


cd Week3_assignment
docker build -t sentiment .
docker run -p 127.0.0.1:8000:8000 sentiment