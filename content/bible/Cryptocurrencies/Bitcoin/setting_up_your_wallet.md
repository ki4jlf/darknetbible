---
title: Setting up your wallet (BTC)
weight: 40
---

# Setting up your wallet (BTC)


**Note**: Do not use Electrum wallets with two-factor authentication (2FA). You may think that 2FA for markets is good (which it is) so it must be good for Electrum on Tails too. No. It requires you to bring your smartphone into DNM activities as well as installing google apps on it which is the last thing you want for an anonymous DNM wallet.
Plus your wallet will be secure enough if you keep your seed secure (e.g. written down on a piece of paper in a secret location and stored in a .txt file in your persistence directory, more on that later) and use KeePassX for your wallet password.
Please just create a normal wallet as described in the following steps.


## Using Whonix?

Electrum is now built into Whonix for use! You can follow the same setup below for using electrum in Whonix.

## Setting up Electrum

Fortunately Tails already comes with a wallet installed. So everything you have to do is to set it up. To do this click on "Applications" on the top task bar and select the category "Internet". Then click on the "Electrum Bitcoin Wallet" entry in the list on the right.
{{< figure src="/images/elecopen.png" class="borderimage" >}}

If you get the warning that "Persistence is disabled for Electrum" you either need to [set it up first]({{< relref "setting_up_persistence" >}}). so you do not lose your bitcoins.
It should now start an installation wizard 

First type the name you would like to give this wallet. 
{{< figure src="/images/elecname.png" class="borderimage" >}}

What kind of wallet do you want to create?
 "Standard Wallet"
{{< figure src="/images/electype.png" class="borderimage" >}}

Do you want to create a new seed, or restore a wallet using an existing seed?
Choose "Create a new seed"
{{< figure src="/images/elecnewseed.png" class="borderimage" >}}

Choose a seed type
 "Segwit" 
{{< figure src="/images/elecseedtype.png" class="borderimage" >}}


You now get that new seed. As long as you remember that seed, you can always recover your bitcoins (even if you loose your password or when your USB stick with Tails gets lost). So make damn sure that you either remember it or write it down somewhere where nobody else can find it.
{{< figure src="/images/elecseedgen.png" class="borderimage" >}}

Confirm Seed Now type in the seed you have remembered or written down.
{{< figure src="/images/elecseedconfirm.png" class="borderimage" >}}

Choose a password to encrypt your wallet keys Do not skip this step. Instead choose a strong password using [KeePass]({{< relref "adding_entries" >}}). In case you loose it, you can always restore your wallet with the seed and set a new password.
{{< figure src="/images/elecpass.png" class="borderimage" >}}


Almost done!

Now you just have to make a few change in the settings. Go to "Tools" -> "Preferences" 

Under General 
Change "Base unit" to BTC
"Zeros after decimal point" to something like 5. 
{{< figure src="/images/elecgeneral.png" class="borderimage" >}}


Under Transactions
Check the checkbox for and the one for "Enable Replace-By-Fee". 
"Use multiple change addresses" 
"Online Block Explorer" to blockchainbdgpzk.onion (You may need to scroll down to find it)
{{< figure src="/images/electrans.png" class="borderimage" >}}

Now close the dialog by clicking on "Close".


**Important note**  
Electrum has a list of several servers which it will ask in order to get the balance of the addresses that belong to your wallet. Law enforcement could easily set up such a server to collect information about when what IP address asks for the balance of what Bitcoin addresses. So Electrum is not anonymous.
However if you use Electrum on Tails, law enforcement only knows which addresses belong to that wallet (because the IP address of a Tor exit node suddenly request the balance of for example 20 specific addresses) but not the true IP address of the owner because Tails routes it's entire internet traffic through the Tor network.
Because of this issue it is very important that you exactly follow the steps in the sending bitcoins chapter.

## Electrum questions?

Check their FAQ, their documentation and google your question. If that does not help, you can post your question on /d/darknetmarketsnoobs
Electrum not starting any more?
First make sure you still have your seed for that wallet and that you can still access it even if your Tails USB stick would break completely.
Then right click on desktop, open terminal, and type in
electrum
and press ENTER. See if it loads. If it does not load do the following steps:
Make sure that "Bitcoin client" is checked in the list of data that will be preserved between reboots (go Applications -> System Tools -> Configure persistent volume to see the list).
Several users also reported that the following helped: go Applications -> System Tools -> Configure persistent volume and uncheck the Electrum option. Then reboot and check the option again. To finish it, reboot again and test if electrum opens.
Reboot Tails and try deleting the "electrum" folder in the directory /live/persistence/TailsData_unlocked/ because it can happen that the Electrum files are corrupted. Then restart Tails and see if you can open Electrum again, if yes you will have to restore your old wallet from your seed.
If that does not work go into your /home/amnesia/ directory and press CTRL + h. then rename the folder .electrum to .electrum.bak. After that restart and see if you can start Electum now.
