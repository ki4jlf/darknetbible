---
title: Bitmessage
weight: 30
---

# Bitmessage

{{< hint danger >}}
**Note:** It is important to note that most of Bitmessage is written in Python2. Python2 was End of Life in January 2020. This means that the core python team is no longer actively developing it, bugs or holes *could* eventually be found in python2 that might put risk on Bitmessage, make sure anything sensitive you still use PGP.
{{< /hint >}}

**What is Bitmessage?**

Bitmessage is a decentralized, encrypted, peer-to-peer, trustless communications protocol that can be used by one person to send encrypted messages to another person, or to multiple subscribers.

## Getting started

For Bitmessage to work we need to install Pythonqt4.

First thing you will want to do is make sure you have your persistence enabled, AND additional software. Check the setting up [persistent volume]({{< relref "setting_up_persistence" >}}) chapter if you are unsure how to do that.

Next thing we need to do is boot tails with the Administration password enabled.
* On the Welcome Screen, enable the Administration Password. You can make it whatever you want it will reset after you shutdown tails. (Click the + in the bottom left) 

Once you are booted into tails open root terminal
* Applications-system tools-Root Terminal.

You will be prompted for your password that you made at login. 

In root terminal type the following two lines

{{< highlight bash >}}
apt-get update

apt-get upgrade

apt-get install -y python-qt4
{{< /highlight >}}

* When the window pops up click install every time.
* Restart your system 
* Once you restart you should see a notification that additional software is being installed.

## Getting PyBitmessage

Now we can actually get Bitmessage onto your system. To do this you need to download their source code.
* Go to Bitmessage.org it should automatically direct you to their onion address. or [click here](http://bitmsgdyvsmwgsimkxplisxbzpewvkhfm3fmomzd63apaymaxiznz6ad.onion/Main_Page)
* On their main page click [Source code on github](https://github.com/Bitmessage/PyBitmessage)
* On github click Code->Download Zip.
* Once the download finishes extract the content to your persistence folder.
* Now navigate to the folder you just extracted. Places-> Persistent-> PyBitmessage 
* Right click in the folder -> Open in terminal
* Type the following:

{{< highlight bash >}}
./bitmessagemain.py
{{< /highlight >}}

Bitmessage should open up. 

## Configuring Bitmessage


When Bitmessage first launches you should be prompted with 3 options.

Connect now
Let me configure special network settings first
Work offline. 

Check Let me configure special network settings first then ok.

* Change listening port to 9050
* Under Server/Tor change it to SOCKS5
* Server hostname should be localhost and port should be 9050
* Check the box that says Only connect to onion services (*.onion)

Now click the tab that says User interface
* Check the box that says run in portable mode.

This will save your keys and settings in the folder in your persistence storage. Make a backup of this folder so you don’t lose your keys!

Click ok. After a few minutes the light on the bottom right should change to yellow this is fine, and Bitmessage will still be operating properly.

## Creating a Bitmessage address


To chat with people you will need to create an identity. On the main screen click new identity.
A window will open read the different options

Since we are running in portable mode, and you made a backup of this folder with your keys in it (RIGHT!?) we can just make one with random number generator.

Click ok and you will see your new Bitmessage number on the main screen.

Now you can also go to the send tab, where the options are pretty straight forward for sending a message. You can check the status of the message you sent on the main screen by going to your sent message.



And you’re done! You’ve successfully installed Bitmessage!