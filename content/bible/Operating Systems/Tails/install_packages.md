---
title: "Optional: Install Debian Packages on Boot"
weight: 70
---

# Optional: Install Debian Packages on Boot

This is an **optional** part if the DNM bible. Please only follow the instructions here when you actually need to install further packages. It is not necessary to install additional software because Tails already has everything you need installed. Any additional software is a security risk. Tails has a facility for automatically installing Debian packages on boot up.

Boot Tails.  
[Enable persistence]({{< relref "setting_up_persistence" >}}) and assign an administration password.
To use this system, you should enable the following two persistence items by clicking on them so that they have a green check mark in the Tails persistence wizard. (Applications -> Tails -> Configure persistent volume):

APT Packages  
APT Lists

If those items were not checked, then reboot so that the settings can take effect.
If you needed to reboot, enable persistence and assign an administration password again.
Start a root terminal (Applications -> System Tools -> Root Terminal)
Type the following commands:

{{< highlight bash >}}
apt-get update
{{< /highlight >}}


(this will take awhile, probably 5 to 10 minutes)
In this example, we are going to install the following package:
gpa (The GNU Privacy Assistant - a familiar PGP client)
Type the following commands:

{{< highlight bash >}}
apt-get install gpa
{{< /highlight >}}


(enter y to confirm installation of the package)

{{< highlight bash >}}
cd /live/persistence/TailsData_unlocked

gedit live-additional-software.conf 
{{< /highlight >}}


Add the following line to the empty file:  
> gpa

Save the file and exit gedit.  
(You will get some warnings from gedit. They are safe to ignore.)
Normally when you install software on Tails using apt-get, it is erased when you shutdown and you have to re-install it next time you boot. Using the above apt persistence settings, the downloaded software is saved locally. By listing items in the "live-additional-software.conf" file, the system will automatically unpack and install them on boot.
The packages are unpacked by a separate process, so that the boot up time is not extended too much.
A status message will pop-up when the system is done installing the software reading "Your additional software / The upgrade was successful".  
To start the PGP client GPA, Select Applications -> Accessories -> GNU Privacy Assistant.
