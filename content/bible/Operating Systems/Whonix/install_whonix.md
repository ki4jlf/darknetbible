---
title: Installing Whonix
weight: 20
---

# Installing Whonix

## Installing

Before you install Whonix, a small note that it consists of two different OS: the Gateway and the Workstation. When you set everything up you do all your work (like using the Tor browser, decrypting PGP messages, . . .) on the Workstation. The Workstation contacts the Gateway in the background (i.e. you do not have to do anything) and sends the entire internet traffic that you produce on the Workstation to it.

The Gateway then connects to the Tor network and sends your traffic through it. That gives you an additional security advantage. So you basically run three operating systems (OS) at a time: your host OS (e.g. Ubuntu), Whonix Gateway and Whonix Workstation. Normally you can only boot one OS at a time on your computer, but with a special software (called VirtualBox) you can run more. Do not worry it is not that complicated, just follow the steps below.

To install Whonix just follow the instructions on [this page](https://www.whonix.org/wiki/VirtualBox). For the step 2 (called "Install Whonix") of the linked guide you need to open the Konsole. Do that by simply pressing CTRL + ALT + T and then enter the command from the guide.

Do not forget to verify the downloaded Whonix files as explained in the guide. Also change the default password ("changeme") on the Whonix Workstation and Gateway.
