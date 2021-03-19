---
title: Starting and shutting down Whonix
weight: 30
---

# Starting and shutting down Whonix


## Starting

First, start the Whonix-Gateway. Select the Whonix-Gateway in VirtualBox, and hit the big Start button or double click on the entry in the list on the left.

Tip: enlarge the Gateway and Workstation windows after you started them for improved usability.


Once the desktop environment has loaded (i.e. you see the desktop), open the Konsole by double clicking on the Konsole-shortcut on the desktop and change your password by hitting ENTER after typing

{{< highlight bash >}}
passwd user
{{< /highlight >}}


The default username is: user  
The default password is: changeme

Change the password to what you want it to be. It does not has to be that complex but you should not use the default one either.

**Note**: to change the keyboard layout, press the Start button at the bottom left -> Computer -> System Settings -> Input Devices -> switch to the "Layouts" tab on the by default selected keyboard category -> check the "Configure layouts" checkbox -> click "Add" and add your desired laypout. Then remove the default English (US) layout and save the settings by clicking "Apply".

{{< hint info >}}
**Tip**: you can copy the commands and then right-click in the Konsole-window (terminal) and select paste. Alternatively you can also press CTRL + SHIFT + V to paste the command into the Konsole.
{{< /hint >}}

After that update your system by typing the following command into the Konsole

{{< highlight bash >}}
sudo apt-get update && sudo apt-get dist-upgrade
{{< /highlight >}}

{{< hint warning >}}
**Important**: Whonix checks on the Gateway and Workstation every 24 hours if updates for the installed software are available. If yes you get a window that contains something like this:
{{< /hint >}}

{{< highlight plain >}}
WARNING: Debian Package Update Check Result: apt-get reports that packages can be updated.
[some more text how to open the Konsole]
sudo apt-get update && sudo apt-get dist-upgrade
{{< /highlight >}}


Simply copy the command, open the Konsole according to the instructions, paste the command and press ENTER. Then it prints out a few lines in the window and asks you with a message like the following if you want to install the updates:

{{< highlight plain >}}
Do you want to continue? [Y/n] 
{{< /highlight >}}

Type y and press ENTER. Then wait till it finish, i.e. the line at the bottom of the Konsole window begins with user@host:~$. Then you can close the window and reboot Whonix (Gateway and Workstation).

Sometimes you also only get updates on the Gateway and not the Workstation, or the other way around. In that case, do not worry and apply the updates as described above.

If the checking for updates somehow fails, reboot the Gateway and the Workstation and see if the checking works this time. If the update check then does not run automatically (after the reboot), run the update command manually by entering the

{{< highlight bash >}}
sudo apt-get update && sudo apt-get dist-upgrade
{{< /highlight >}}

command from above manually in the Konsole.

If there are no updates available, i.e. your system is up to date, you will still get a window after the check is finished which shows a few lines of text which contain "INFO" in green font at the beginning of some lines.

Now after all that is done, go back to the VirtualBox window on your host OS, select the Whonix-Workstation, and click the big Start button. Then go back to to the beginning of the "Starting Whonix" section of this guide and do all that stuff in your Workstation desktop environment.


Note: you only need to change your password once (once on the Gateway and once on the Workstation), not every time you reboot Whonix.

After you did the whole updating for the Workstation too, you can download the Tor borwser. To do that, double click the Tor Browser icon on your desktop. Follow the prompts, and get the version you want. Make sure that the version does not contain an "a" or "b" which stands for alpha and beta versions that are not yet ready to be released for all users and may contain bugs.

Then launch the Tor Browser by double clicking on the desktop icon called "Tor Browser (AnonDist)". Now you need to configure it a bit to make it more secure. [First set the security slider to high](https://tails.boum.org/doc/anonymous_internet/Tor_Browser/#index3h2/). The link goes to the Tails website but since it is about the Tor browser, it also applies to Whonix. Fortunately, Whonix preserves your settings so you do not need to set the slider to high every time you reboot Whonix.

Now JavaScript (JS) is disabled globally, which is how it should be if you only use DNMs.

{{< hint info >}}
**Tip**: On on the top right corner, click on the icon with the three horizontally stacked bars and choose "Customize". Drag the bookmarks and downloads icons up to your menu bar or your tool bar so you can use them easily. Click "Exit Customize" in the green box on the lower right side.
{{< /hint >}}

{{< hint warning >}}
**Important**: on the Workstation, wait till the small globe icon with the clock is green before starting the Tor browser. That means that the time synchronization was successful. If it is yellow just wait some more time before starting the Tor browser. If it has a small red and white cross, it means that the check failed. In that case restart the Workstation and wait till the symbol goes green.
{{< /hint >}}

## Shutting down


Always close out Whonix in reverse order. That means, shutdown the Workstation first, then shutdown the Gateway. After the VirtualBox windows for both are closed, you can also close VirtualBox. To finish, shut down your host OS after that.

If you are running terminal-based version of the Gateway for performance reasons, just enter the command

{{< highlight bash >}}
sudo poweroff
{{< /highlight >}}

and press ENTER to shut the Gateway down.
