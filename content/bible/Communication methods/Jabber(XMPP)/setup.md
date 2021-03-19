---
title: Jabber(XMPP) Setup
weight: 20
---

# Jabber(XMPP) Setup        
For this example setup we will be using The Calyx Institute. You can read about their public jabber servers, Data retention policy, and other information [here](https://calyxinstitute.org/projects/digital-services/xmpp)

You do not have to use Calyx Institute if you do not want to. Check this [list]({{< relref "services" >}}) for some other options. (Their settings will be different from this guide)


## How to configure Pidgin and OTR Plugin

First open Pidgin by going to Applications (at the top left of your screen) -> Internet -> Pidgin Internet Messenger. Then two separate windows should open. One should look like this:

{{< figure src="/images/pidgin_welcome.png" class="borderimage" >}}

 On the one called "Buddy List" go Tools -> Plugins and scroll down the alphabetically sorted list till you see an entry called "Off-the-Record Messaging". Make sure the checkbox on the left of it is checked, then select the entry and click on "Configure Plugin".

{{< figure src="/images/pidgin_plugin.png" class="borderimage" >}}

Ensure that the following options are selected:

- "Enable private messaging"
- "Don't log OTR conversations"
- "Automatically initiate private messaging"

Now close the configuration window and the plugin overview window.

## Getting an XMPP account

To be able to chat with someone you still need to register an account.Some XMPP servers do not log connecting IPs or greatly limit what they log. Policies are decided entirely by each individual XMPP server administrator. The ones listed on services however are rather privacy friendly and you are using Tor (by using Tails or Whonix) any way. Some may require registering your account through their website and cannot be registered through Pidgin. The registration is usually quick and easy in any event.

In the "Buddy List" window go Accounts -> Manage Accounts which should switch you to your second window (the "Accounts" window). Click on the "Add" button and select the following options:

- Protocol: XMPP
- Username: YourDesiredName
- Domain: jabber.calyxinstitute.org (or whatever jabber server you want to use, see the linked list above)
- Resource: Leave blank. It indicates which device you are using, not important.
- Password: (make your password strong and unique)
- Check the checkbox called "Create this new account on the server" at the bottom
{{< figure src="/images/pidgin_account.png" class="borderimage" >}}

Next Click the tab that says "Advanced" in Advanced your settings should be:
- Connection Security: Require Encryption
- Connect Port 5222
- Connect server: ijeeynrc6x2uy5ob.onion
- File transfer proxies: Leave blank
- BOSH URL: Leave blank     
**NOTE:** You should always try to use a hidden service server.   
{{< figure src="/images/pidgin_connection.png" class="borderimage" >}}


To finish click on the "Add" button and wait a short time. Then you should get automatically presented a window to enter your username and password which you previously set in the configuration. Enter them and click "OK". Then you should get the message that the registration of your account was successful.

**Note:** You will probably get a notification to accept a certificate.

After that go to the account window and check the checkbox on the left of your new account to enable it. This should ask you again for your password and after a short time the status at the bottom of the "Buddy List" window will change to "Available" with a green circle on the left of it.

For the XMPP server used in this example you also get a welcome message telling you their twitter account and that you should donate if you find the service useful (which you should do if you have some leftover money or donate them.