---
title: Encrypting a message
weight: 20
---

# Encrypting a message with PGP

{{< hint warning >}}
You must always encrypt sensitive information yourself. Never trust a market to do it for you.
{{< /hint >}}

{{< tabs >}}
{{< tab "Tails" >}}
{{< hint info >}}
You first need to [import]({{< relref "importing_a_public_key.md" >}}) the public key of the user (e.g. a vendor) that you want to message, so you can encrypt messages that you want to send to him.
{{< /hint >}}

To encrypt messages with PGP you first have to type that message in the text editor. Then press CTRL + A and CTRL + C to copy it. After that click on the clipboard icon and select "Sign/Encrypt Clipboard with Public Keys".

{{< figure src="/images/tails_pgp_sign_encrypt_with_pubkey.png" class="borderimage" >}}

On the new window select the public key of the user you want to encrypt the message for (e.g. your vendor) by checking the checkbox in front of the list entry. Then select your key on the drop down list on the right of "Sign message as:" and make sure that the "Hide recipients" option is unchecked.

{{< figure src="/images/tails_pgp_select_recipients.png" class="borderimage" >}}

When that is done, click on "OK" and you should get asked if you trust these keys. Click on "Yes" and enter your password for your private key. To confirm that it encrypted your message properly go back to your text editor and press CTRL + V. If you see something that looks like this, it is encrypted properly.

    -----BEGIN PGP MESSAGE-----

    hQIMA8Pzj/CHV15DAQ/+JOWXCC6vDIxNge3xRqHsKCSEToFkx02qXd9PwWRFESgc
    QZGwh6yz0DVlB7yKJZvzRK1O0tS2wLpKKMBNv8dPv/u6B609yXzP6ns3066C7ymO
    PAFA1MgvKvu7mUg5wxFRPKgFfYxBNbCleS5MzPp8bPJq6xQaVeOOogPtFWerN/vM
    iIcCod+JyWoBgy3iBw==
    =alkJ
    -----END PGP MESSAGE-----

The gibberish in the middle (the actual encrypted message) will be a little bit longer for you.

{{< hint info >}}
**Note**: After your message is encrypted you will not be able to decrypt it. Only the selected recipient will be able to do it. It is possible to select multiple recipients, so if you want to be able to decrypt your message you must also select your own key.
{{< /hint >}}

Now all you have to do is going to the market or email website, paste the clipboard content into the relevant text field and send the message or email.

After you did this please close the text editor and if it asks you if the changes should be saved, select "Close without saving".
{{< /tab >}}
{{< tab "Whonix" >}}
{{< hint info >}}
You first need to [import]({{< relref "importing_a_public_key.md" >}}) the public key of the user (e.g. a vendor) that you want to message, so you can encrypt messages that you want to send to him.
{{< /hint >}}

Open the KGpg window and select File -> Open Editor. Then type in the message that you want to encrypt in the new editor window. To encrypt it, click on the "Encrypt" button at the bottom and then select the according PGP key from the list that appeared in the new window (i.e. the PGP key of the vendor that you want to send the encrypted message to).

Then the text in the editor will change to something like this, if it is encrypted properly.


    -----BEGIN PGP MESSAGE-----

    hQIMA8Pzj/CHV15DAQ/+JOWXCC6vDIxNge3xRqHsKCSEToFkx02qXd9PwWRFESgc
    QZGwh6yz0DVlB7yKJZvzRK1O0tS2wLpKKMBNv8dPv/u6B609yXzP6ns3066C7ymO
    PAFA1MgvKvu7mUg5wxFRPKgFfYxBNbCleS5MzPp8bPJq6xQaVeOOogPtFWerN/vM
    iIcCod+JyWoBgy3iBw==
    =alkJ
    -----END PGP MESSAGE-----

The gibberish in the middle (the actual encrypted message) will be a little bit longer for you.

{{< hint info >}}
**Note**: After your message is encrypted you will not be able to decrypt it. Only the selected recipient will be able to do it. It is possible to select multiple recipients, so if you want to be able to decrypt your message you must also select your own key.
{{< /hint >}}

Now all you have to do is going to the market or email website, paste the clipboard content into the relevant text field and send the message or email.

After you did this please close the editor window and click the "Discard" button when it asks you if you want to save the document.
{{< /tab >}}
{{< /tabs >}}
