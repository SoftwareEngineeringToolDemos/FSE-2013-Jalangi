#Building the Jalangi VM:
###Instructions:
1. Download and install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).
2. Download this folder ("build-vm").
3. In a terminal, navigate to this folder and run the command "vagrant up".

The console then prints out the script's progress, which will take several minutes before completion. Midway through the process, a window for the new VM should open on your desktop, but you shouldn't try to use the VM until your initial terminal is finished running scripts.

In this version, the script only creates an instance of Ubuntu 14.04 and installs Java 7. This script was modified slightly from the command line installation that the official Jalangi Readme provides.

###VM Credentials:

Username: vagrant

Password: vagrant


###Notes:

The base box used for the Vagrant script is [box-cutter/ubuntu1404-desktop](https://vagrantcloud.com/box-cutter/boxes/ubuntu1404-desktop).

You may need SSH for Vagrant to work. For Windows, you can use OpenSSH as part of [Cygwin](https://www.cygwin.com/).

The commands for silenty installing Java were found [here](http://askubuntu.com/questions/190582/installing-java-automatically-with-silent-option).
