---
title: Important tips for using markets
weight: 5
---

# Important tips for using markets


* **NEVER** let the market encrypt sensitive data (such as your address) for you. **Always** encrypt it yourself. The market can always store the plaintext version of your message, and send an encrypted one to the vendor. That way you both think it was encrypted while the market still has the original and unencrypted message. Also if the market gets taken over by law enforcement, they will store the plaintext versions of the messages that the users sent using the 'PGP encrypt' checkbox to harvest addresses. But they will still send the encrypted ones to the vendor to not make anyone suspicious.

* Use 2 Factor Authentication **(2FA)**. It means you will have to decrypt a PGP message that was encrypted with your public key every time you log in, in addition to your username and password. Using 2 FA will greatly improve your chances of success when contacting the support of the market because you lost some funds for example (since 2FA makes it much harder for unauthorized persons to break into your account they will not just say that you got phished and close your ticket). To set up 2FA, go to your DNM account settings and look for an option to enable 2FA. Upload your public PGP key first in the settings first if you have not done it already. [Here]({{< relref "creating_a_pgp_key_pair" >}}) is how to create a secure PGP key.

* Found a link on the hidden wiki or similar sites? It is very likely that they are a scam.

* **Never** use a market that requires javascript. Read about why [here](/bible/miscellaneous-information/javascript/)

* **Never** leave more bitcoins on a market than necessary. Ideally you should only transfer the necessary amount to the market if you also ready to make the purchase right after they have arrived in your market wallet. Leaving funds in your market wallet is too risky since the market can steal them at any given time.

* **Make sure to never tell anybody about your DNM activities.** This can not be emphasized enough.

* **Never** use the same username, password, PIN or PGP key-pair on more than one market. If an attacker or even rogue market staff gains access to your account on one market, he could easily break into the other ones as well and do even more damage (like stealing your coins or deleting your account).

* Do **not** use identifying usernames or passwords. That means your username should give no clue about who you really are, e.g. do not include your birth year in your username.

* **Never** use privnote or similar services that claim to offer self-destructing messages. Absolutely nothing prevents such services from storing your message even after it was 'officially' destroyed. On top of that they also require JavaScript, which is a huge no-go. Just encrypt your messages with PGP like every other market user and send them using the internal market messaging system. Also avoid vendors that use privnote or similar services.

* Do not check tracking at all, unless a substantial or abnormal amount of time has passed without delivery. You will only leave traces when doing so but will not make it arrive faster. For more details visit the [non arriving packages]({{< relref "non_arriving_packages" >}}) chapter. If you absolutely have to check it (which should never be the case), do not use Tor to do it. It will be a huge red flag and law enforcement already knows about DNM users checking their packages over Tor. Instead use a third party website if possible, so not the one of your mail carrier but a website which checks the tracking for you.Examples are TrackingEx and PackageMapping. Also do not use your own WiFi for checking the tracking number. Use one that is not tied to your identity (e.g. a cafe) or use a VPN and choose a server that is in the same country as you (to not raise any red flags).

* Do not just order from the biggest vendor(s) on the market simply because of the size of their operation or because they pay for ads on a DNM or other site. Often there are smaller vendors with who offer a better product with a better customer service.

* Do you not know if it is a lower case L or upper case i in a captcha? It is almost always a lower case L.

* If a vendor suddenly changes his PGP key without signing it with his old one, stay away from him until he does so!

* When sending messages (no matter if on Reddit or a DNM) try to write all you have to say in **one** message. Nobody likes getting hit with a high notification counter when logging in just to realize that you wrote half of the new messages. It is also easier to answer for your chat partner if you sent only one message.

* When you make an order, the status of it will be unaccepted (or similarly called) at first. When the vendor confirms/accepts your order it will be market as accepted or processing. Again the exact words vary from each DNM. The next step would be market as shipped or in transit. The last step of the order is finalized or completed.

* It is not necessary to encrypt every message you send on a DNM. You **absolutely** have to encrypt all sensitive data such as addresses or tracking numbers. However mundane questions about the product for example do not need to be encrypted, since the vendor would need much more time to decrypt all messages.

* Do not use SWIM or a variation of it. It stands for "Somebody who is not me" and is absolutely useless. No law enforcement agent will stop his work when he sees that you used SWIM. It only makes you look like a complete noob. Instead step up your OpSec which is far more helpful.

* Remove the version string from your PGP public key (which is the line that begins with "Version:" and is directly under the "-----BEGIN PGP PUBLIC KEY BLOCK-----" line). It is not necessary and just gives away information about the software that you are using.

* Are you not getting past the captcha although you always entered it correctly? Restart your Tor browser and visit the market address again to register (try another onion address if the market provides more than one). If that still does not work please go to your privacy preferences by entering about:preferences#privacy in your address bar or by going to Edit -> Preferences and selecting "Privacy" on the sidebar. Then click on the button 'Exceptions...' next to the checkbox labeled "Accept cookies from sites' (which should be unchecked). Then paste the site address (the onion link of the market that you are using) into the input field. Click on "Allow for Session" and then on "Save Changes". If you do not want to do it every time, check the checkbox "Accept cookies from sites" (it is the default setting anyway).

* **NEVER** use Tor gateways. By using them you send your login credentials and all other data in plaintext through the whole internet till it reaches the Tor gateway. So not only your ISP knows that you are buying drugs online but also the gateway can simply steal your bitcoins. Just follow the steps in the DNM bible as every other sane user.

* Get a scale. Seriously.

* **NO** market staff will message you on Reddit. If you get a PM from someone claiming to be market staff, please report it to the mods of {{< subdread "/d/DarkNetMarkets" >}} or {{< subdread "/d/Dread" >}} immediately.

* Use KeePassXC to generate and store your market, Electrum and PGP passwords.

* Unsure when to use "Bitcoin" and "bitcoin"? Bitcoin - with capitalization, is used when describing the concept of Bitcoin, or the entire network itself. e.g. "I was learning about the Bitcoin protocol today." bitcoin - without capitalization, is used to describe bitcoins as a unit of account. e.g. "I sent ten bitcoins today."; it is also often abbreviated BTC or XBT. (From bitcoin.org)

## About other goods you might find on DNMs

**Credit Cards**: Nobody is going to sell you a physical cloned CC that you can use at a store or stick in an ATM and get money out. If they are selling them for less than the balance of the card they are basically giving you money as they could cash the cards out just as easily as you could.

**PayPal accounts/transfers**: People sell PayPal accounts/transfers because they can't figure out how to beat PayPal's anti-fraud systems to cash it out. If you think you can do that better than career fraudsters go ahead. Even on the highest rated vendors for them on Evolution there were still plenty of bad reviews about accounts being locked down minutes after receiving them.

**Electronics**: All onion electronics stores are scams. There is already a market where you can sell electronics you have carded or stolen from stores, it's called Ebay. The reason thieves target electronics is because they can be flipped for close to face value. Why would they setup a hidden service to sell stuff as stolen for half price when they could get 75% of it's value on Ebay with much less hassle?

**Darknet non-escrow "stores" in general**: Unless it is being run by a vendor that started on a DNM (there should be a matching PGP key, don't trust any other proof) they are all scams. They are primarily advertised on various "hidden wiki" sites where there is no place to leave feedback. Without escrow or feedback opportunities they have **zero** incentive to ever deliver a product to you.

**Counterfeit Money**: It is never a good idea to order and use it. Not only is law enforcement really going hard after such people (e.g. in the US the secret service is investigating counterfeit money cases), but it is also very hard to actually use the fake money. For example the quality has to be very good, it takes very long to get rid of the fake notes and get real money back because you can not use them all at once but have to go to different places and can only carry one fake note at a time, . . . So counterfeit money is definitely not worth the risk.
