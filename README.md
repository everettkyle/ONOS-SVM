# ONOS-SVM
Using ONOS and an SVM to detect anomalous behavior in IoT devices
(Ubuntu 18.04 Tested)

This repo will be to provide general knowledge on how to install and use the ONOS platform.<br>
I will also provide multiple useful commands for the CLI, GUI, and Docker that will speed up 
the process of development.
## Mininet-Installation
*Make sure you have Mininet Installed* <br>
For installing mininet on Ubuntu 18.04 its pretty simple. <br>
*Run:* sudo apt install mininet <br>

---

## ONOS-Installation (via Docker)
If you don't have docker already installed Digital Ocean has a great tutorial
that you can follow.

**Digital Ocean Docker install tutorial:**<br>
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04 <br>
Once you have docker installed you need to setup your environment with the required tools needed to run ONOS.<br>

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
*Clone ONOS github:* git clone https://gerrit.onosproject.org/onos <br>
*Pull the ONOS image:* sudo docker pull onosproject/onos <br>



---
## Contributors 
- Kyle Everett -- **Linkedin:** https://www.linkedin.com/in/kyle-everett-829b50113/
---
