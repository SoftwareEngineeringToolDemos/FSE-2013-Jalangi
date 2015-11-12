###Instructions:
1. Download and install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).
2. Download this folder ("build-vm").
3. In a terminal, navigate to this folder and run the command "vagrant up".

The console should then print out the script's progress. It will take about 15
minutes for completion. In this version, the script only creates an instance
of Ubuntu 14.04 and installs Java 7.

###VM Credentials:
Username: vagrant
Password: vagrant


###Notes:
The base box used for the Vagrant script is [box-cutter/ubuntu1404-desktop](https://vagrantcloud.com/box-cutter/boxes/ubuntu1404-desktop).
You may need SSH for Vagrant to work. For windows, you can use OpenSSH as part of [Cygwin](https://www.cygwin.com/).
