---
title: Performance tips
weight: 40
---

# Performance tips

Running essentially three operating systems (OS) at the same time can take up some resources from your computer. Especially if you are all doing it from a USB stick and not an internal SSD for example. So in the following some tips which you can follow if you want to improve the performance of your Whonix setup. If everything is running smoothly, you do not need to follow them (if it is not broke, do not fix it).

Make sure you have followed the previous Whonix chapters already so you are improving a secure setup and do not have to start all over again (e.g. because you use Whonix on Windows).

Note: most of the tips that involve changing VirtualBox settings for VMs (the Whonix Gateway and Workstation) require the the the VMs to be shut down. So only boot up your Linux distribution that you use for running Whonix (e.g. Ubuntu or Linux Mint) but do not start Whonix too.

## Using more CPUs for the Workstation

Since the Workstation will do the most amount of work, it should also be able to make good use of your CPUs. To ensure that, open the VirtualBox window -> right-click on the "Whonix-Workstation" entry on the left -> select "Settings" -> go to the "System" category -> switch to the "Processor" tab.

Now you should see two sliders: "Processor(s)" and "Execution Cap". If the "Execution Cap" slider is not already set to 100 percent (on the right end), please drag it there. If the "Processor(s)" slider is not disabled, set it to the middle value (i.e. if the maximum is 4 CPUs set it to 2 or if the maximum is 8 CPUs set it to 4).

If you can not move the slider you only need to do one additional step, which is enabling an option called "VT-x technology" in your BIOS or UEFI settings. This may sound complicated but is pretty easy and can give you an enormous performance boost. [Here are the steps](https://askubuntu.com/questions/256792/how-do-i-enable-hardware-virtualization-technology-vt-x-for-use-in-virtualbox/256853#256853), you basically need to get into your BIOS / UEFI settings -> search for an option called something like Virtualization or VT-x -> enable it -> save settings and reboot.

Then when you rebooted with the new settings, the "Processor(s)" slider should not be disabled any more. Now you can change it according to the instructions above.

## Reducing the RAM for the Gateway

You can reduce the amount of RAM that the Gateway is allowed to take up which helps reducing the overall work load for your computer. [Read this first](https://www.whonix.org/wiki/RAM_Adjusted_Desktop_Starter) and then you can adjust the memory in VirtualBox.

Open the VirtualBox window -> right-click on the "Whonix-Gateway" entry on the left -> select "Settings" -> go to the "System" category. Now you should see a slider called "Base Memory" under the "Motherboard" tab. As mentioned in the previous link, the minimum requirement for the Gateway is 256 Megabyte RAM. You should set it to a bit more than that (around 300), apply the other performance tips as well and then see if the Gateway and Workstation are running more smoothly. If you then still have performance issues, you can reduce the memory down to 256 Megabyte.

Now you will only see the terminal-based version of the Gateway even when it is fully booted. This saves the computer some resources but you will still be able to do all the tasks you need to do on it (which is essentially only updating the software if there are updates available).

So in the future start the Gateway -> wait till you get the login prompt -> enter your username (default "user") and password (default "changeme") and press ENTER. After that the Gateway will hijack your command line input when it is checking for software updates, meaning that it will print out some lines without showing you the usual input line where you can enter commands. In such cases just wait till it is finished and gives you a message ending with "Please feel free to press enter to return back to your normal prompt".

So press ENTER and check if the above lines (which show the result of the software update check) contain something like "[WARNING] [whonixcheck] Debian Package Update Check Result: apt-get reports that packages can be updated." If you see such a line, enter the command

{{< highlight bash >}}
sudo apt-get update && sudo apt-get dist-upgrade
{{< /highlight >}}

and press ENTER. That command should also be shown to you in a few lines under the line which contains the note that packages can be updated. Then when you get the line "Do you want to continue? [Y/n]" press either ENTER (which answers the "Update? Yes / No" question with the answer that was capitalized, in this case the "Y" for "Yes") or type y and press ENTER.

Tip: you can also copy that update command by highlighting it -> right-click on it -> select "Copy" -> left click again to un-highlight it and return to your input-line -> right-click -> select "Paste".

This process replaces the usual update process which shows you the notification window where you copy the update command and paste it into the terminal (like you do on the Workstation).

To shut down the Gateway in the future just enter the command

{{< highlight bash >}}
sudo poweroff
{{< /highlight >}}

and press ENTER.

## Using an SSD

If you are not already using an SSD for your Ubuntu or Linux Mint installation, consider switching to one. It offers significant speed boosts over a normal USB stick. You can easily buy a cheap external SSD online or in stores. They do not need to have much capacity either for this use-case, 50 or 75 Gigabyte would easily be sufficient. If that is not an option consider using a USB 3.0 stick on a 3.0 port over a 2.0 one which gets you better results.
