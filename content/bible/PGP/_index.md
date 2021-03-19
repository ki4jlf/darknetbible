---
title: PGP
bookCollapseSection: true
weight: 50
---

# PGP


## General information


Pretty Good Privacy (PGP) is an encryption program that provides cryptographic privacy and authentication for data communication. PGP is often used for signing, encrypting, and decrypting texts, e-mails and files and to increase the security of email communications.

A typical darknet user will use PGP to:

#### Encrypt messages
- To encrypt the shipping address and other sensitive information so only the vendor can read it.

#### Decrypt messages
- Vendors will encrypt sensitive shipping information for you (e.g. tracking codes).
- Decrypting a message is sometimes required to login to a market.

#### Verify messages
- To verify that a market link is legit and not a phishing site.

Learning how to use PGP is very important. You don't ever want your personal details to fall into the hands of law enforcement. Please carefully read through all sections in this chapter. If you want to make sure that you can properly encrypt and decrypt messages with PGP please go to {{< subdread "/d/PGPPractice" >}}.

## FAQ

### What if I sent a message without PGP?

Did you sent a message that contained sensitive data (e.g. your address) without encrypting it with PGP by yourself?

Then it is best to delete your market account and start a new one. And no, this is not overkill. When the Silk Road servers were seized, a lot of messages were not PGP encrypted and contained addresses in plaintext. In the following years the FBI gave those data to other law enforcement agencies around the world and they busted buyers that sent their addresses unencrypted. So if you would continue to order with that account, the evidence against you would just stack up even more.

{{< hint danger >}}
**Please** make the cut now and create a new market account with which you will always PGP encrypt your address by yourself.
{{< /hint >}}

### Can I use the market's built in encryption?

**No**. The server processes the message in plain text, if the market is compromised attackers will be able to see the contents. Always encrypt sensitive information yourself.

### Do I need to encrypt all messages?

You only need to encrypt messages containing sensitive information such as packaging details (which should only ever be discussed between a vendor and a buyer) or addresses. Saying "Thanks!" doesn't need encryption.

### Can I decrypt a PGP message I sent?

No, only the user whose public key you used to encrypt the message can decrypt it. However if you select the public keys of the users you want to send the message to and your own public key, then you will be able to decrypt the encrypted message. You will learn later how to do that.

### What is the difference between PGP and GPG?

It is explained [here](https://askubuntu.com/questions/186805/difference-between-pgp-and-gpg).
