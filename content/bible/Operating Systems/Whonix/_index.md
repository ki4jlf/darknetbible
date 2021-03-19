---
title: Whonix
bookCollapseSection: true
weight: 20
---

# Whonix


## When you should use this guide

This guide shows an alternative, but still secure setup. Usually Tails is the easier and faster solution, so try it out if you have not already.
However sometimes users have issues with it that can no be resolved by reading through the DNM bible, googling the issues and asking on dedicated forums (like {{< subdread "/d/DarkNetMarketsNoobs" >}} or {{< subdread "/d/Tails" >}}).
In these cases it is better to follow this guide since it is less hassle for you and still gives you a reasonable secure setup instead of a horrible one which for example involves windows (the get-in-jail-free card).

## General


This guide is for installing Whonix on a Linux distribution such as Ubuntu, Debian or Linux Mint. It is important to choose a distribution that offers **Full Disk Encryption** such as the named ones. Otherwise, your whole setup would be useless. If you are not really keen with Linux, it is recommended that you use Ubuntu or Linux Mint in the following as they are easy to use and there are many resources available if you run into issues.

**DO NOT USE WHONIX ON WINDOWS OR OS X**. They are insecure and cancerous to your OpSec. If you want to play the game, do it right.

**Note**: more security can be achieved by using Qubes with Whonix. However this is more for technically advanced people and higher profile users and therefore a smaller target group. This guide is for using Whonix without Qubes, guides for Qubes will follow at some point in the future though.
Related subs for additional resources:

- /d/Whonix
- /d/VirtualBox

## What is Whonix?


It's basically like a sandboxed and torrify'd Linux operating system (OS) which you can run while running your usual operating system (called host OS). That means you boot for example Ubuntu from a USB stick and then run Whonix (the guest OS) within your booted Ubuntu (an OS in an OS). In Whonix's words:

>Whonix is a desktop operating system designed for advanced security and privacy. It realistically addresses attacks while maintaining usability. It makes online anonymity possible via fail-safe, automatic, and desktop-wide use of the Tor network. A heavily reconfigured Debian base is run inside multiple virtual machines, providing a substantial layer of protection from malware and IP leaks. Pre-installed applications, pre-configured with safe defaults are ready for use. Additionally, installing custom applications or personalizing the desktop will in no way jeopardize the user. Whonix is the only actively developed OS designed to be run inside a VM and paired with Tor.


For more information please visit their [website](https://www.whonix.org/).

**Note**: you could also easily use Tor in combination with a VPN when using this guide. To do that simply run the VPN software on your host OS (e.g. Ubuntu or Linux Mint). **However** this is often unnecessary, especially as a buyer, since DNM users get frequently busted because they made other, more simple mistakes. So it is far more important that you take care of these other factors first by reading and following every page of the DNM bible, instead of jumping on a rather unnecessary OpSec measure (using a VPN).  
Here a [quick comparison](https://www.whonix.org/wiki/Comparison_with_Others) of Whonix with other OS.
