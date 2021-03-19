---
title: Monero FAQ
bookCollapseSection: true
weight: 5
---

# Monero FAQ

## How do I safely route my coins?
Exchange -> Monero wallet (on Tails or Whonix) -> Destination

More details in the following posts: [1](http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion/post/745cd3237a0eeff70ed5), [2](http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion/post/272e1b2a9317a973c99d)

## My vendor only accepts Bitcoin, what do I do?
Monero wallet -> Exchange service -> Destination
or
Monero wallet -> Exchange service -> Bitcoin wallet -> Destination

Use an instant exchange service over Tor to anonymously convert your Monero into Bitcoin.

Avoid sending directly from an exchange service to the destination if your order has a short timeout. The order may expire before payment arrives if the exchange is delayed for whatever reason. By first sending the Bitcoin to your personal wallet you have more control over when the payment is made. Make sure you convert enough to cover the extra transaction fees you will be paying.

## Is it safe to buy Monero directly on a KYC exchange?
For most threat models, [yes.](https://old.reddit.com/r/Monero/comments/g6end3/how_to_buy_xmr_anonymously_wo_getting_ripped_off/fo9dcub/)

## Is it safer to buy Monero directly or to buy Bitcoin and convert it?
If possible for you, buying Monero directly should always be preferred.

As a rule of thumb: try to minimize your interactions with transparent blockchains (such as Bitcoin, Litecoin, etc) as much as possible.

## How do I buy Monero anonymously?
Cash by mail on [LocalMonero.co](http://localmonerogt7be.onion/)


## Why is my transaction not showing up?

- Is your wallet software on the latest version?
Some Monero updates are backwards incompatible, old versions stop working eventually.

- Is your wallet synchronized?
The wallet needs to scan the blockchain to find your transactions. Wait for this process to complete.

GUI: Check the status in the lower left hand corner.
Feather: The status bar should say "Synchronized"

- Does your transaction exist on a block explorer?
Go to xmrchain.net and enter the txid of your transaction. If it doesn't show up something went wrong on the sending side, contact them to sort it out.

If your transaction shows up on a block explorer and your wallet is synchronized, try the following:

Feather:
Tools -> Import transaction. Enter the txid of the transaction. Click "Load", then "Import". If the transaction belongs to the primary wallet account it should now show up in the history.

GUI:
Go to Settings -> Info. Next to "Wallet restore height" click "Change", press Ok twice.
Wait for the wallet to resync. After it is done syncing your transaction should show up.

## My outgoing transactions keep failing
Feather: Before closing the wallet, right click on the "Failed" transaction and select "Resend transaction". Wait for a few minutes until the transaction has 1 confirmation or try again.

GUI: Switch to a different node, go to Settings -> Wallet -> Rescan wallet balance, then try resending your transaction.

Failed transaction are caused by malfunctioning nodes. Whenever this happens please check which remote node you're connected to and message the mods so it can be removed.

## Is it safe to connect to a remote node over Tor?
For most threat models, [yes.](http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion/post/769995e72d1e18bae2e4/#c-32f11a9295d8513c3d)

It is recommended to change your remote node between each session. Feather wallet does this automatically.

## How do I run a full node on Tails?
Check the guide [here.](https://old.reddit.com/r/Monero/comments/h8pbc2/guide_setting_up_a_monero_full_node_on_tails/)

## How do I set up a public/private remote node?
Check the guide [here.](http://6idyd6chquyis57aavk3nhqyu3x2xfrqelj4ay5atwrorfcpdqeuifid.onion/guides/run-a-monero-node/)

## Is there any way to speed up synchronization?
Switching to a different remote node will often help.

GUI: Follow the instructions [here.](xmrguide42y34onq.onion/tails/gui/troubleshoot/change_remote_node)
Feather: File -> Settings -> Node -> Double click on a different node.

## How do I copy my address from Tails/Whonix to a different machine?

* Save your address to a .txt file and use a second USB drive to transfer it over
* Send a PGP encrypted e-mail to yourself using a throwaway e-mail service
* Scan the QR code with a secondary device

## My wallet keeps freezing / crashing
PM the mods on {{< subdread "/d/monero" >}}. with details, so we can work on a fix. Feather users please provide a copy of Help -> Debug info.

## What happened to Morphscript / MorphToken?
MorphToken started blocking all Tor exit nodes. Morphscript no longer works on Tails/Whonix.

Consider using an alternative service from the list of exchanges.

## Resources

**Block explorers**

https://xmrchain.net/ (no JS)
http://theblock755bysooet2texualb4detjjcvkxs2nxuiumln4bacjh3rqd.onion (no JS)


**Remote nodes**
Check the list [here.](http://xmrguide42y34onq.onion/remote_nodes) 