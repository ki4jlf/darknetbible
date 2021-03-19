---
title: Got problems?
weight: 100
---

# Got Problems?


## Common issues

As mentioned previously, Tails works on _almost_ any computer. So it is possible that your installation will not go as flawlessly as it usually should. However there are many way to solve issues that might come up. Please go through the following options one after another if you have difficulties getting tails on a USB stick or to boot:

- Did you [disable secure boot](https://msdn.microsoft.com/en-us/windows/hardware/commercialize/manufacture/desktop/disabling-secure-boot)?

- Look at the list of [known issues](https://tails.boum.org/support/known_issues/index.en.html) and check if there is hardware on it that you use too (for example a USB brand or a certain network card). If it is on the list please check if there is also a solution described, if yes try it. Sometimes it is best to try booting Tails on another computer to see if it is working there, so you know if your computer is the problem.

- Tor is not ready or other internet connection issues? Boot Tails, log in and do something else for about 5 to 10 minutes. Then go back and check if Tor is ready now by opening the Tor browser. If you still get the "Tor is not ready" warning, reboot Tails and try again. If that does not work try disabling MAC address spoofing on the Tails greeting screen when rebooting (select "More Options", click on "Forward" and click once on "Spoof all MAC addresses").

- Are some password not getting accepted although they should be correct? Please check that you set the correct keyboard layout on the Tails greeting screen as [described here]({{< relref "installing_tails.md" >}}).

- Having trouble booting Tails although you followed the instructions on the Tails website? Check that your USB stick is not on the list of [problematic USB sticks](https://tails.boum.org/support/known_issues/index.en.html#index1h2) USB sticks and see if they work.

- If Tails freezes after you press enter in the [boot screen](https://tails.boum.org/install/inc/screenshots/tails_boot_menu.png), try not pressing enter to boot but letting Tails count down itself. If Tails worked previously but suddenly has freezing issues, try rebooting a couple of times. Some users report that it worked after about 5 tries.

- Does Tails freeze and only shows you a blue screen? A user reported that the following worked for him: When Tails first boots up (before choosing tails or tails failsafe version), press tab to open up the console. Don't modify anything, just type all of the following commands: nouveau.modeset=0 modeset.blacklist=nouveau noslash One of the commands above should get you past the blue screen. Unfortunately you will have to enter the commands every time you boot but it's better then it not working at all.

- Having issues accessing your persistence data? You may be able to fix your problem by simply re-running the persistence configuration tool: Applications > Tails > configure persistent volume and enable the same options that you had before. Then reboot.

- For OS X: If Tails does not show up when holding the alt key upon restart, try the following. Install rEFInd (if you use a Mac with El Capitan or later, rEFInd may not install properly). Then temporarily disabled SIP: hold command + R when you see the Apple logo after restarting, then go to Utilities -> Terminal, then type "crsutil disable" in the Terminal window then press Enter, then restart as normal and install rEFInd, then repeat the process but this time type "crsutil enable," turning SIP back on.

- Can you not connect to your WiFi because it keeps asking for the password but you know you entering it correctly (e.g. it just asks for password after a few minutes of trying to connect)?. It could be an issue with Tails not recognizing drivers, so a solution would be to use a WiFi adapter or a wired connection (i.e. plug in an ethernet cable that is connected to your router).

- Does the Tails installer does not work when clicking an option? [Try this](https://www.reddit.com/r/tails/comments/3dr8xh/clone_and_install_does_nothing/).

- Do you get asked for a password when you want to install Tails by cloning? If the process is like this: you click on "install by cloning" it shows the USB stick you want to clone Tails to, so you click on "install Tails", then get asked to confirm the device selection, which you do, and are then told that authentication is required to "unmount General UDisk (/dev/sda1)" mounted by another user" (or a similar message) - which is when it asks you for the password. If that is the case, follow the instructions [here](https://technet.microsoft.com/en-us/library/jj200124%28v=ws.11%29.aspx) (for the USB stick that you want to clone Tails on) but use fs=fat32 quick instead of fs=ntfs quick in step 9. If that does not work please try using two different USB sticks and avoid using the ones that are on the [list of known issues](https://tails.boum.org/support/known_issues/index.en.html#index1h2).

- Issues with your screen resolution? [Check out this](https://tor.stackexchange.com/questions/4551/how-to-change-display-resolution-in-tails).

- Are you using a mac and have issues installing/booting Tails? [Try following these steps](https://cryptovillage.org/dc22/tails_osx.pdf).

- [Icons and information located on the top right corner of the screen disappeared?](https://tails.boum.org/support/known_issues/index.en.html#index38h2)

- Boot problems and an error message like this "(initramfs) unable to find a medium containing a live file system on custom Live USB"? A user reported that using rufus and choose a different partition scheme helped. Also try holding the power button down for 10 seconds till the computer turns off and then turn it on again to see if it works with the second boot.


Still not solved?


Research your problem. That means using a [search engine](https://duckduckgo.com/) and the search function of the {{< subdread "/d/DarknetMarketsNoobs" >}} subdread to search for solutions for your problem. If that does not help you can make a post on {{< subdread "/d/DarkNetMarketsNoobs" >}} **but** remember to give it a meaningful title (i.e. "When booting Tails I just get a blank screen" instead of "need help plz").
