---
title: Backing up
weight: 60
---

# Backing up

It is **crucial** that you back up your data. Not just the data you have on Tails but all your other documents too. However this chapter will only deal with how to back up your persistence data which is stored on Tails. You probably do not want to loose access to your market account and wallet with all your money in it, so you **need** to do the following steps.

Yes, nobody likes to make backups but you will be _really_ annoyed if you loose your Tails USB stick and your market account and coins with it.

Backing up will only take a few minutes over your time be sure you do it regularly!

To start you will need another USB that you wish to back your system up onto. 

## Cloning Tails

**Note:** First thing we need to do is clone your current tails drive. If you already have Tails cloned you can jump down to the backing up Persistent Storage section below

**Note 2:** This part will NOT backup your persistent! You must clone tails before you can backup 

* First login to the tails USB you want to backup. Once you are logged in to Tails plug in your USB stick that will serve as your backup.

* Now go to Applications-> Tails -> Tails Installer (or you can find it on the sidebar)

* A window like this will open
{{< figure src="/images/tails_cloner.png" class="borderimage" >}}

* Select Clone the current Tails, and select the USB that will be your backup on the Target USB stick Drop down menu.

* Click Install

* Read the warning message in the confirmation dialog. Click Yes to confirm.
Depending on your computer will vary how long the installation will take. The progress bar usually freezes for some time while synchronizing.

* Finally it should say Installation Complete!

You now have cloned tails!


## Backing up your Persistent Storage

**Note:** If this is your first time backing up to this USB you need boot into your backup USB first [enable persistent volume]({{< relref "setting_up_persistence" >}}) and everything else you want enabled. (Electrum, GNUPG, DOT files) 

* Once everything is enabled on your backup drive, boot back into your main Tails drive that you will be backing up. On the Welcome Screen, enable the Administration Password. You can make it whatever you want it will reset after you shutdown tails. (Click the + in the bottom left)
#Insert welcome screen image

* Once you have booted up tails with the Administration Password enabled go to, Applications-> Accessories-> Files to open the Files browser

* Plug in your backup USB stick.

* You should see a encrypted volume in the sidebar of the Files browser. Click on it and enter the Persistent storage password for your BACKUP tails.

* It should now appear as TailsData volume on the sidebar.

* Open up root terminal. You can either go up top and type terminal and click root terminal or go Applications-> System Tools -> Root Terminal enter the Administration Password that you made.

* In Terminal run the following command:
{{< highlight bash >}}
rsync -PaSHAXv --del /live/persistence/TailsData_unlocked/ /media/amnesia/TailsData/ 
{{< /highlight >}}

When the command finishes running you should see something like this displayed: 
{{< highlight bash >}}
sent 32.32M bytes received 1.69K bytes 21.55M bytes/sec
total size is 32.30M speedup is 1.00
{{< /highlight >}}

**Congrats you have successfully backed up your entire tails drive!**
Going forward you do not need to clone your drive again. You can just boot up with administrator password enabled, unlock your backup, and run that command. It will update the backup for you.

This only takes 5 minutes to do! Remember to take regular backups so you don’t lose your shit!!