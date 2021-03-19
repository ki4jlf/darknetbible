---
title: Tails
bookCollapseSection: true
weight: 10
---

# Tails

{{< figure src="/images/logo.svg" class="tailsbanner">}}

[Tails](https://tails.boum.org/) is a live operating system that you can start on almost any computer from a DVD, USB stick, or SD card. It aims at preserving your privacy and anonymity, and helps you to:

- use the Internet anonymously and circumvent censorship (because all connections to the Internet are forced to go through the Tor network)

- leave no trace on the computer you are using unless you ask it explicitly and

- use state-of-the-art cryptographic tools to encrypt your files, emails and instant messaging

As you can see it is a pretty useful operating system for doing things that you do not want others to find out. An it gets even better: you do not need to install any additional tools for using darknetmarkets! Everything you need as a buyer is already installed.

Here is the [default desktop of Tails](https://tails.boum.org/install/inc/screenshots/desktop.png). Pretty neat isn't it?


## Is Tails necessary?


**YES**. Even if you think you are just a small fish and nobody will go after you. Let me give you an example: you use the Tor browser on Windows to make your order and everything seems to go fine. However unfortunately your package gets caught by customs because the vendor did not package it correctly. Now law enforcement starts to investigate because someone tried to send illegal drugs to you. One possible consequence is that they will deliver the package to you but raid your house shortly afterwards because you are in possession of illegal drugs (called a [controlled delivery]({{< relref "controlled_delivery.md" >}}).)

Since Windows is not secure, they will find all the evidence they need to prove in court that you made the order. You would not have these issues with Tails because nobody can say what you did on there or say what files you stored on your [persistence volume]({{< relref "setting_up_persistence" >}}). Tails does not even leave a trace that it was booted on your computer!

So as you can see, Tails is not only to prevent you from getting caught but also for greatly minimizing the damage done if you get caught.

## Do I need a VPN?


Normally, no.

Here an excerpt form the Tails website about VPNs:

>    Some users have requested support for VPNs in Tails to "improve" Tor's anonymity. You know, more hops must be better, right?. That's just incorrect -- if anything VPNs make the situation worse since they basically introduce either a permanent entry guard (if the VPN is set up before Tor) or a permanent exit node (if the VPN is accessed through Tor).

>    Similarly, we don't want to support VPNs as a replacement for Tor since that provides terrible anonymity and hence isn't compatible with Tails' goal.



[Quoted from the official tails website](https://tails.boum.org/blueprint/vpn_support/)

The main goals of a VPN would be to a) hide your tor usage from your ISP and b) add another security layer.

a) If you want to hide the fact that you are using Tor from your ISP, then you can select the "More Options" button on the Tails greeting screen and then select the Option "This computer's Internet connection is censored, filter or proxied". However if you are not living under an oppressive regime in which it is illegal or not possible to use Tor normally, it is not recommended to use that options since it only takes away resources from people who really need it.

b) Assuming that law enforcement would break the Tor network and get the IP address that you used to connect to the Tor network, they would know your real identity (or at least the one of the owner of the WiFi that you used). If you would use a VPN they would only get the IP address of the VPN server that you used (assuming that you set up Tails and the VPN correctly). However it is extremely unlikely that LE would try to attempt this just to bust a buyer that bought a few grams. There is no known case where a buyer got busted by a Tor de-anonymization attack and there will probably never be one.

There are **many** other OpSec factors which are more important and have a greater impact on your well-being, so please take care of them first before dealing with the Tails with a VPN topic.

If you still want to use Tor and a VPN, please [read this](https://thetinhat.com/tutorials/darknets/tor-vpn-using-both.html).

## Ordered without Tails before?


If you did not use Tails for previous orders you made a mistake. The problem is not that much that law enforcement will catch you now because of it, but rather that if you get in trouble later they can still find proof for your past orders and then prosecute you. Therefore it is important to remove the evidence immediately and step up your OpSec for future purchases.

The first step is to uninstall all the tools you used to order on your insecure OS. That includes the Tor browser, PGP tools, Bitcoin wallets, . . .

After that you have to overwrite the free disk space on your hard drive. That is to make it harder to recover the deleted tools (and therefore evidence that can get you in trouble) but it will not delete any other files you have on your hard drive. That means the uninstalled tools will get overwritten but your personal documents (e.g. your pictures in your home folder) will not be affected by it.

Here is how to do it on [windows](http://www.howtogeek.com/137108/how-securely-overwrite-free-space-in-windows/), [mac](http://osxdaily.com/2016/04/28/erase-free-space-mac-command-line/) and [linux](https://ssd.eff.org/en/module/how-delete-your-data-securely-linux).

**Note**: this is not 100% secure. There are always log files that you OS might have created which still show that you used tools that are common for DNM buyers (e.g. PGP tools). Therefore it is important that you follow the steps mentioned above and keep **everything** related to DNM purchases on Tails in the future.

## Using Tails on a personal/work computer


Using Tails on a computer doesn't alter or depend on the operating system installed on it. So you can use it in the same way on your computer, a friend's computer, or one at your local library. After shutting down Tails, the computer will start again with its usual operating system.

Tails is configured with special care to not use the computer's hard-disks, even if there is some swap space on them. The only storage space used by Tails is in RAM, which is automatically erased when the computer shuts down. So you won't leave any trace on the computer either of the Tails system itself or what you used it for. That's why we call Tails "amnesic".

This allows you to work with sensitive documents on any computer and protects you from data recovery after shutdown. Of course, you can still explicitly save specific documents to another USB stick or external hard-disk and take them away for future use.

[Quoted from here.](https://tails.boum.org/about/index.en.html#index2h1)

tl;dr you can use Tails on your normal computer and do not have to buy a burner laptop.

## Using Tails on your own WiFi


If you use Tails (or Tor in general) on your own WiFi, your ISP will only know that you are using Tor but not what you are doing exactly. If you do not want your ISP to know that you are using tor you can tell Tor to use bridges on the Tails greeting screen (select "Yes" for the more options question and after pressing forward select the "My computer's Internet connection is censored, filtered or proxied" option). That will obfuscate the fact that you are using Tor from your ISP although it is not necessary as long as you are not living under an oppressive regime which blocks Tor and/or makes the use of it illegal. If that is not the case, please do not use bridges as it would take away resources from people who actually need them.

So only reason for using another WiFi than your own is that an attacker would not get your real IP address in case of a de-anonymization attack but the one from the network you are using (e.g. the starbucks WiFi). However these attacks are unrealistic for buyers and the risks that this method brings along (e.g. someone shoulder-surfing or a camera recording your face and/or screen) make it not worth it for buyers. Therefore using your own WiFi along with following all the other tips in the DNM bible is a much better solution.

## Is it okay to use a WiFi with login?


Sometimes you will have to log into WiFis with credentials that in some cases are also tied to your real identity (e.g. a college WiFi). Tails [spoofs all MAC addresses](https://tails.boum.org/doc/first_steps/startup_options/mac_spoofing/index.en.html) by default, that means that a system administrator would only see that a seemingly other device than your default one logged in with your credentials. That adds some plausible deniability, because you can claim that someone stole your login credentials and logged in with them on another computer. Furthermore nobody knows what exactly you are doing since the whole internet traffic that Tails produces is routed through the Tor network and is therefore encrypted and nobody knows where it goes. So to make it short: yes you can use Tails in a WiFi that requires you to log in.

## Are DNS leaks an issue?

When using Tor your computer does not make the DNS requests for the sites you visit but the exit node (the last node in the chain of relays that route your Tor traffic) makes the DNS requests for you. That is done because Tor does only support TCP but not UDP traffic. So just use Tails, which routes all your traffic through the Tor network, and you will not have to worry about it.

## I want to buy a new computer anyway, which works best with Tails?


Many computers are able to run Tails, but if you have the choice you should keep the following tips in mind when picking a computer:

- Do not use a mac, macbook or any other apple device because they can not always run Tails.

- Make sure that no hardware parts in the computer are on the [list of known issues](https://tails.boum.org/support/known_issues/index.en.html).

- If possible choose one that has not windows 8 or 10 installed because they are more likely to cause issues than the ones with older windows versions or no OS at all.

Some users also report that [alienware computers](https://www.dell.com/en-us/gaming/alienware-laptops?cs=19) are working good with Tails. And here is [a list](http://picknotebook.com/blog/best-tails-laptops/) of laptops that work good with Tails too.

## Is running the latest version of Tails necessary?


**Yes**. It is absolutely crucial that you always use the latest version of Tails since the updates usually fix security vulnerabilities to which you are vulnerable by not upgrading. So take the few minutes and [upgrade Tails]({{< relref "upgrading.md" >}}) **as soon** as you get the notification that an update is available.

## Compatible hardware


If you run into problems with Tails and your hardware, you might want to buy one of these if you can try using Tails on another computer:

**USB sticks**

The following listed USB sticks will work with Tails (tested with Tails 3.0).

- Kingston Data Traveler SE9 G2 16GB

- Lexar Twist/Turn Jump Drive 16GB

- Mushkin Atom 16GB

- Onn 32GB (Walmart brand)

- Transcend Jetflash 700 16GB

All of the drives above can be found online easily. They range from $6-15 each. The Onn is a Walmart brand and can be found in most stores. The Lexar can be found in most Target stores.

The Onn is manufactured by Sandisk as a private label for Walmart(just found this out but since passed testing left it in there)

**USB WiFi adapters**

**Note**: before you buy extra hardware, try using an Ethernet cable that you plug in your router and your computer. It is usually the easiest solution and recommended over buying a new WiFi adapter.

These USB WiFi adapters are known to work with Tails:

- https://www.amazon.com/CanaKit-Raspberry-Wireless-Adapter-Dongle/dp/B00GFAN498/

- https://www.amazon.com/Edimax-EW-7811Un-150Mbps-Raspberry-Supports/dp/B003MTTJOY/

- Belkin N300 high-performance WiFi USB adapter

**USB Ethernet adapters**

These USB Ethernet adapters are known to work with Tails:

- http://plugable.com/products/usb3-e1000

- http://plugable.com/products/usb3-hub3me

## Can I buy USB sticks that already have Tails installed on it?


No. Nothings prevents the seller from modifying the Tails installation which is on the USB stick so that it for example sends all the passwords you use to them. Always download, verify and install tails by yourself.

## Why is JavaScript enabled globally by default and the security slider set to low?


There are a lot not so tech savvy Tails users who would have a hard time dealing with all the different settings if they were all set to high and they would have to make adjustments. Therefore the developers decided to set the default settings to not so strict values to make the Tails experience better for these users.

You however, have to make sure that you set the [security slider to high](https://tails.boum.org/doc/anonymous_internet/Tor_Browser/#index3h2) every time you start the Tor browser (because it is not possible to save the security slider settings between the reboots, even with persistence enabled).
