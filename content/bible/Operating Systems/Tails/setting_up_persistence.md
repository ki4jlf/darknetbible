---
title: Setting up the persistence volume
weight: 40
---

# Creating and configuring the Persistent Storage 

Normally Tails forgets every change you made on it when you reboot (that is why it is called amnesiac). However when you want to order from DNMs you need to save some files. This is possible by setting up the persistence volume which encrypt, and store your data after restarting. Tails uses LUKS or, Linux Unified Key Setup to encrypt your data, if you want to know more about LUKS you can read about it [here](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup)

**Make sure the persistence volume is actually working before you use it.** That means for example set up a wallet like it is described later in the bible and then reboot to see if you can still access and read all the data you created.

**Note:** you absolutely have to make sure that you do not forget or lose your persistence password. If you lose it, you also lose access to your whole Tails installation which includes PGP keys, market accounts, Electrum wallet if you have not written down your seed (which you should do)

Some of the things you can enable tails to save are

* Personal Data
* Browser Bookmarks
* Network Connections
* Additional Software
* Printers
* Thunderbird
* GnuPG
* Bitcoin Client
* Pidgin
* SSH Client
* Dotfiles

A detailed explanation of each setting can be found when enabling.


## Creating Persistence

* To create or configure the Persistent Storage, simply go to: Application->Tails->Configure persistent volume
{{< figure src="/images/tails_applications_system_tools.png" class="borderimage" >}}

* Specify a passphrase of your choice in both the Passphrase and Verify Passphrase text boxes. The best way to create a password that is both strong and memorable is to create a [mnemonic](/images/password_strength.png). A mnemonic of at least 5  words or more is recommended.
{{< figure src="/images/tails_configure_persistent_volume_cropped.png" class="borderimage" >}}

* Click on the Create button.

* The list of features of the Persistent Storage appears. Each feature corresponds to a set of files or settings that can be saved in the Persistent Storage. Click which options you need, click Save at the bottom.

**NOTE:** If you are new and unsure which options you will need, chances are you will want to enable Personal data, GnuPG, Bitcoin client, and Dotfiles. Others can be added later if you want them.

* Restart your machine

* Your welcome should now look like this
{{< figure src="/images/welcome_screen_with_persistence.png" class="borderimage" >}}

Once you login You can now save your personal files, and working documents in the Persistent folder. To open the Persistent folder choose Places -> Persistent. Your other tools you enabled will save automatically.

**Note:** Unticking a tool in the persistent configuration will NOT delete the files of your persistent in the future. If you need to delete see below.

## How to delete persistence

On occasions you might come across a need to delete your persistent storage.
This technique is fast but might not prevent a strong attacker from recovering files from an old Persistent Storage using advanced data recovery techniques.

To securely delete the Persistent Storage, you have to securely delete the entire USB stick, which is a much slower operation.

* Start Tails from the USB stick on which you want to delete the Persistent Storage.

In the Welcome Screen, keep the Persistent Storage locked.

* Choose Applications -> Tails -> Delete persistent volume.

*  Click Delete.

Alternatively if you want to delete the files for specific tool, without losing everything follow this:

*  Start Tails and set an administration password, you can make it anything tails will erase it when you reset. (Click the plus on the welcome screen)
{{< figure src="/images/additional.png" class="borderimage" >}}

* Choose Applications -> System Tools -> Root Terminal to open a terminal with administration rights. 

* Type nautilus to open the file browser with administration rights. 

* In the file browser, navigate to /live/persistence/TailsData_unlocked. 

* Delete the folder corresponding to the feature