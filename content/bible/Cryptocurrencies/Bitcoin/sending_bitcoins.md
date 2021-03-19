---
title: Sending Bitcoin
weight: 50
---

# Sending Bitcoin


This chapter deals with sending your bitcoins from the source you got them (e.g. a Bitcoin exchange) to the final destination (a DNM). Unfortunately it is not as easy as sending them straight to your market deposit address because exchanges have banned and flagged accounts in the past that did that.

## The Path

**Note**: as described earlier, if you use Electrum an attacker can see what addresses belong to what wallet and which IP address regularly checks the balance of these addresses.

The general the path you should send your bitcoins is: Bitcoin exchange ->BTC Wallet1-> convert to XMR->XMR Wallet -> DNM IF your vendor does not accept XMR you can convert back to Bitcoin. More on that later in the converting section.

**Note**: That normal wallet and the Electrum wallet on Tails have to be different wallets. So you need to do the setup process described previously twice: once for your normal wallet and once for your Electrum wallet on Tails.

This process is to break the chain of custody to you, and add plausible deniablity. Once converted to XMR it cannot be traced anymore. If you were to be questioned about converting you can just say you sent them for consulting, or simply say you no longer have access to the wallet.
If you would go exchange -> Electrum on Tails -> DNM, it would be pretty obvious that you are the one who sent the bitcoins to the DNM (assuming that the DNM deposit address is known), because nobody would give the DNM deposit address to the Bitcoin seller when buying the bitcoins. That means: if you still claim that you sold the bitcoins to someone else after withdrawing them from the exchange to your Electrum wallet on Tails, that new buyer would have given you his DNM deposit address. This is extremely unlikely because you normally do not give out DNM deposit addresses out when buying bitcoins, but rather one that belongs to one of your wallets. Therefore nobody would believe you that you sold the bitcoins to a stranger. So your plausible deniability would be gone.
With the recommended path (marked in bold above) you can believably claim that someone else sent the bitcoins to a DNM and the exchange will most likely not ban your account because you did not sent them directly to a DNM.

Note: some markets have a minimum amount of bitcoins you have to send for a deposit. Make sure you meet that requirement or you could lose your money!
I did not send my bitcoins that way before, am I fucked?
You will probably be fine, BUT make sure you go the path described above in the future for every DNM deposit. You do not have to delete your DNM account or Bitcoin exchange account, but step up your OpSec in the future.

## Sending bitcoins with Electrum The process

To send bitcoins from your Electrum wallet to an address just go to the "Send" tab and enter the destination Bitcoin address in the "Pay to". When sending the bitcoins make sure you use the transaction fee that is dynamically created by Electrum (by default it will get confirmed within 5 blocks). That means just let the slider under the amount field be in the middle. If you are sending the bitcoins from the normal wallet you have to get a receiving address from your Electrum wallet on Tails first. To do that go to the "Addresses" tab in your Electrum wallet on Tails and write down the value of one of the Bitcoin addresses listed under "Receiving".

**Note**: you can double click on the space on the right of the address to change the label of that address. It is recommended to label it as "used <current date>" for example, so you know that you already used it and do not use it again.
After that boot your normal OS again and start Electrum again. Then you can go to the "Send" tab again and send the bitcoins to the address of your Electrum wallet on Tails. When you received the bitcoins on Electrum wallet on Tails you can repeat the same send-process but this time send them to the deposit address that your market gave you.

## Setting the fee manually

You can also set the fee manually to ensure that your transaction (short: tx) does not take too long to confirm. Using the dynamic fee as described above is usually the best way though. If you do want to set the fee manually though, follow these steps:

1. Go to bitcoinfees.21.co, allow JavaScript for "https://bitcoinfees.21.co" and scroll down to the bottom of the graphs. There you see a sentence like "The fastest and cheapest transaction fee is currently 390 satoshis/byte".
2. Open Electrum and go Tools -> Preferences and uncheck the "Use dynamic fees" option. Then you can set the transaction fee per kilobyte (kb) in BTC/kB. If it shows mBTC/kB, switch to the "Appearance" tab and select "BTC" as the base unit from the dropdown menu.
3. Now change the value of the transaction fee per kb like this: If the recommended fee from the website is 390 satoshis/byte, set the fee to 0.0039 BTC/kB. That means, append three zeros to the satoshis/byte value as well as a point after the zero on the far left. If the website would have recommended 280 satoshis/byte instead, you should set the fee to 0.0028 BTC/kB instead in Electrum.
4. Done! Now click on the close button.
