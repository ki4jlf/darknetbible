---
title: Installing on Whonix
weight: 10
---

# Installing on Whonix


To use OB on Whonix, do the following steps on the Whonix Workstation. Open the Konsole by double-clicking on the icon called "Konsole" on your Workstation desktop. Then enter the following command (you can copy it and paste it into the terminal / konsole by doing right-click -> "Paste"):

{{< highlight bash >}}
sudo apt-get update && sudo apt-get dist-upgrade -y
{{< /highlight >}}

This makes sure that all your software is up to date. It should also ask you for your password that you should have changed when you set up Whonix. Then open the Tor Browser which is also linked on your desktop and visit the [OB download page](https://www.openbazaar.org/download/). Look out for the Linux category and click on the link that should be called "32-bit (deb)".

Click on it and select "Save File" in the upcoming dialog, Then you get to choose where to save it, click on the "<" which is located between the "Save in folder:" text and the "Browser > Downloads" text. Then click on "user" which will be shown in the changed file path between "> home >" and "> .tb > tor-browser > Browser > Downloads". Then simply double click on the folder called "Desktop" to enter it and press the "Save" button.

This description may be a bit confusing but it is to make sure you save the file in your normal user-directory and not the Tor browser directory (which has a similar structure and you may search forever when saving it there and later looking in the normal user-directory).


When the download is finished (which you can see at the download icon in your Tor browser that should be on the right of the address bar), switch to your desktop.

Once on your desktop make sure you only see one file with the OB name. If you see two, one of it should be called something like "openbazaar2_2.0.18_i386.deb.part" which means that the download is still running. Wait for the second file to automatically disappear which means that the download finished. Once that happened, right click on the remaining downloaded file -> select "Properties" -> switch to the permissions tab -> check the checkbox called "Is executable" and click the "OK" button.

**Note**: at the time of writing OB apparently did not offer any way to verify the downloaded file (like a signature file or hash) which is not ideal. The transmission of the file is still encrypted but if an attacker would have access to the download server it is stored on, he could replace it with a malicious version. If the developers should release signatures for the downloads in the future and it is not featured in this guide, please message the mods of {{< subdread "/d/DarkNetMarketsNoobs" >}}.

You just started but you are already almost done! Now open the Konsole by double clicking on the icon called "Konsole". Then enter the following command (you can copy it and then right-click and "Paste"):

{{< highlight bash >}}
cd ~/Desktop && sudo dpkg --install openbazaar2_2.0.18_i386.deb 
{{< /highlight >}}

Now this should ask you for your password first and then you should see lines containing an error due to software that is missing on your system but required to run OB (called dependencies). Do not worry about it, the next command automatically installs that required software and makes sure that your installation attempt of OB (that you did with your previous command) completes successfully.

{{< highlight bash >}}
sudo apt-get -f install
{{< /highlight >}}

Press ENTER when you get asked "Do you want to continue? [Y/n]" and wait for the command to finish executing.

-----

Done! You now have OpenBazaar installed. To open it simply open the Application Launcher which is the small "K" icon at the very bottom left (like the Start-Menu on windows) of your screen and type in "open" in the search bar. This should show you an entry called "OpenBazaar", click on it.

Now the OB window will open and prompt you with a question dialog after some loading. Do not check the checkbox called "Use Tor". Whonix already routes your entire internet traffic through Tor so you already got that covered. Click on the "Save" button and wait a bit till you get to a screen with the "Get started >" button. Click it and now you will be prompted to enter some information about yourself.

Obviously do not use your real name but choose an un-identifying username like "MichaelTheMan" (assuming that you are not named Michael) and leave out anything like your birth year or similar information. Now you can also set the currency to your preferred one. Leave out all the other options, they only harm your OpSec when setting them. The vendors you will be buying from will know your country you are from when you send them your PGP encrypted address and an avatar is just more data that could include digital traces leading to your true identity.

After clicking "Next", skim the Terms of Service and agree with them.
