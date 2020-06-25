# ONOS-SVM-Tutorial
Using ONOS and an SVM to detect anomalous behavior in IoT devices
(Ubuntu 18.04 Tested)

This repo will be to provide general knowledge on how to install and use the ONOS platform.<br>
I will also provide multiple useful commands for the CLI, GUI, and Docker that will speed up 
the process of development.

## Mininet-Installation
*Make sure you have Mininet Installed* <br>
  For installing mininet on Ubuntu 18.04 its pretty simple. <br>
  *<ins>Run:</ins>* sudo apt install mininet <br>

---

## ONOS-Installation (via Docker)
  If you don't have docker already installed Digital Ocean has a great tutorial
  that you can follow.

**Digital Ocean Docker install tutorial:**<br>
  https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04 <br>
  Once you have docker installed you need to setup your environment with the required tools needed to run   ONOS.<br>

**Required tools / Commands**<br>
*MAKE SURE TO RUN THESE COMMANDS IN THE ORDER THEY APPEAR*<br>
*MAKE SURE YOURE ON A FRESH NEW VM OR INSTALLATION OF UBUNTU*<br>

  1. sudo apt install python
  2. sudo apt install python3
  3. sudo apt install python-pip python-dev python-setuptools
  4. sudo apt install python3-pip python3-dev python3-setuptools
  5. pip3 install --upgrade pip
  6. pip3 install selenium
  7. sudo apt-get install git
  8. sudo apt-get install git-review

**ONOS Docker**<br>
*<ins>Clone ONOS github:</ins>* git clone https://gerrit.onosproject.org/onos <br>
*<ins>Pull the ONOS image:</ins>* sudo docker pull onosproject/onos <br>

---

## Running-ONOS and Accessing-GUI/CLI

**Running ONOS docker image:** <br>
sudo docker run -t -d -p 8181:8181 -p 8101:8101 -p 5005:5005 -p 830:830 --name onos onosproject/onos

*Inorder to access the CLI and GUI you need to run a few docker commands.* <br>

**Find Docker Container ID:** <br>
sudo docker ps *(This command is used to find all of the currently running docker containers)* <br>
Once you find the ID make sure to copy it.

**Finding Docker IP addr:** <br>
sudo docker inspect 'container-id' *(This command inspects the listed docker container and all of its details)* <br>
Once you find the IP addr make sure to copy it.<br>

*In the next few commands were going to use our Docker IP '172.17.0.2'* <br>

**Accessing GUI:** <br>
Open up a web browser and copy this URL http://172.17.0.2:8181/onos/ui/index.html <br>
When you access the GUI you will not see a topology that comes later.

*Note: The web browser may prompt you to enter in a username and password in order to login <br>
use <ins>Username:</ins>onos <ins>Password:</ins>rocks this should allow you to log in. Also if you just started the <br>
container it may show an error once you copy the URL just wait a minute for the GUI to start up.* <br>

**Accessing CLI:** <br>
Make sure to run this command in the host machine terminal. <br>
ssh onos@172.17.0.2 -p 8101

*Note: For the password same as the GUI use ->* rocks <br>

**Activating ONOS Applications:** <br>
When inside of the GUI go to the applications windows and search for openflow and look for the <ins>"openflow provider suite"</ins> app. Click on it and the press the play button at the top right of the screen to activate the app. Do the same steps and look for the <ins>"Reactive Forwarding"</ins> app and activate that as well. <br>
Now were ready to start to run Mininet and a default simulated topology.<br>

*Note: If you dont activate these apps the mininet topology won't connect to the ONOS remote controller*<br>

**Running Mininet with ONOS:** <br>
By now everything should be setup in order to run the Mininet command below to connect the controller to the simulated topology. <br>

sudo mn --controller remote,ip=172.17.0.2,port=6633 --topo tree,2,2 <br>

After running this command the mininet prompt should start up. Next you want to type the "pingall" command in mininet so that the OvS switches discover all of the connected hosts. <br>

Next you want to access the GUI and while in the GUI you should only be able to see the three switches. If you press **H** the hosts along with their individual ip address should be visible. <br>

---

## Useful-Commands 

**Mininet:**<br>
* xterm h1 h2 s1 *(This command pulls up all of the terminals for the simulated topology components)* <br>
* sudo mn *(This command generally runs mininet with no controller)* <br>

**Openflow virtual switch:**<br>
* sudo ovs-ofctl dump-flows s1 *(This command prints out the flow tables for the openflow switch)*<br>
* <ins>Here is a resource for OvS switch docs:</ins> http://www.openvswitch.org/support/dist-docs/ovs-fields.7.txt <br>

**Docker Commands:**<br>
* sudo docker ps *(lists currently running docker containers)* <br>
* sudo docker ps -a *(lists recently exited containers)* <br>
* sudo docker rm 'docker id' *(rm instance and frees up resources)* <br>
* sudo docker exec -it onos /bin/bash *(accessing terminal in container)* <br>
* sudo docker inspect "docker id" *(Inspecting docker container details)* <br>

**ONOS CLI Commands:**<br>
* flows -s *(lists the flows for all of the connected openflow switches)* <br>
* devices *(lists the openflow devices connected to the controller)* <br>
* <ins>For more CLI commands:</ins> https://wiki.onosproject.org/display/ONOS/Appendix+A+%3A+CLI+commands <br>
* <ins>Great YouTube video for ONOS intents:</ins> https://www.youtube.com/watch?v=glkJaBvtqpA <br>

**Netcat Commands to start a TCP connection:**<br>
* Server: nc -l 2399 <br>
* Client: nc "server_ip" 2399 <br>

---

## Contributors 
- Kyle Everett -- **Linkedin:** https://www.linkedin.com/in/kyle-everett-829b50113/
---
