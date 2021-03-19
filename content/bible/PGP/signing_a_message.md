---
title: Signing a message
weight: 60
---

# Signing a message with PGP

{{< hint danger >}}
**This is not for [encrypting]({{< relref "encrypt_a_message.md" >}}) your address or other private messages.**
{{< /hint >}}

You can sign a message to prove that you created it. Anyone that has your public key can verify that you signed it. It is usually not necessary to sign messages as a normal DNM buyer but if you need to do it, here is how.

{{< tabs "signing">}}
{{< tab "Tails" >}}
Type the message in the text editor. Then press CTRL + A and CTRL + C to copy it. After that click on the clipboard icon and select "Sign/Encrypt Clipboard with Public Keys".

{{< figure src="/images/tails_pgp_sign_encrypt_with_pubkey.png" class="borderimage">}}

On the new window do not check any keys in the recipient list but select your key on the drop down list on the right of "Sign message as:". Also make sure that the "Hide recipients" option is unchecked.

{{< figure src="/images/tails_pgp_sign_message.png" class="borderimage">}}

When that is done, click on "OK" and enter your password for your private key. To confirm that it signed your message properly go back to your text editor and press CTRL + V. If you see something that looks like this, it is signed properly.


    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA512

    This is my signed message.

    Anyone with my public key can verify that I signed it.
    -----BEGIN PGP SIGNATURE-----

    iQIcBAEBAgAGBQJYg5AQAAoJEMPzj/CHV15DTbkP/iweuHOlCH9fxa2CqBoxUn2D
    BZiW94/PMitNAG1hP/Nucc+rAbRgvmtrQ/GfPkcgtUmsLJy0+duMk7PBg1Q3imkz
    icqHhI6eN7F4aHSlM1kVKIXhNSwE0AVaf5n45Yrqtkt+O3BQ7aH/v5vcFbTTzIcf
    XJGfhh/OAig8+w6LQvJL
    =QsWE
    -----END PGP SIGNATURE-----


The gibberish in the middle will be a little bit longer for you. Now all you have to do is going to the market or email website, paste the clipboard content into the relevant text field and send the message or email.

After you did this please close the text editor and if it asks you if the changes should be saved, select "Close without saving".


{{< /tab >}}
{{< tab "Whonix" >}}
Open the KGpg window and select File -> Open Editor. Then type in the message that you want to sign in the new editor window and click on the button "Sign/Verify". Select your PGP key from the newly appeared list and click on "OK". It will then prompt you for the password of your PGP key, enter it and confirm again by clicking on "OK".

Now the content of the editor should look like this:

    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA512

    This is my signed message.

    Anyone with my public key can verify that I signed it.
    -----BEGIN PGP SIGNATURE-----

    iQIcBAEBAgAGBQJYg5AQAAoJEMPzj/CHV15DTbkP/iweuHOlCH9fxa2CqBoxUn2D
    BZiW94/PMitNAG1hP/Nucc+rAbRgvmtrQ/GfPkcgtUmsLJy0+duMk7PBg1Q3imkz
    icqHhI6eN7F4aHSlM1kVKIXhNSwE0AVaf5n45Yrqtkt+O3BQ7aH/v5vcFbTTzIcf
    XJGfhh/OAig8+w6LQvJL
    =QsWE
    -----END PGP SIGNATURE-----

if it is signed properly. The gibberish in the middle will be a little bit longer for you. Now all you have to do is going to the market or email website, paste the copied content of the editor into the relevant text field and send the message or email.

After you did this please close the editor window and click the "Discard" button when it asks you if you want to save the document.
{{< /tab >}}
{{< /tabs >}}
