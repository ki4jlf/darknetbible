---
title: Verifying a message
weight: 30
---

# Verifying a message with PGP

Verifying messages is commonly used to check the authenticity of market links. Markets publish signed messages containing links to their market. If you have the market's public key you can use it to verify that the message was created by the market and that the links are legitimate.

Markets, vendors and moderators will sometimes sign announcements or warnings. You can also use this to verify those.

{{< tabs "verifying">}}
{{< tab "Tails" >}}
{{< hint "info" >}}
Before you can verify the PGP signed message, you need to [import]({{< relref "signing_a_message.md" >}}) the public key of the user that signed the message. So see where it is listed (e.g. on the vendor's profile on the market, or on the market's subdread) and then import it.
{{< /hint >}}

Copy the PGP signed message, it looks something like this:


    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA512

    Here are our onion links:
    
    ar3a3uxsmdjvlv3o.onion
    effma5umlll2bxmd.onion
    xw7w4apecxzw4t7h.onion
    
    - SomeDarknetMarket

    -----BEGIN PGP SIGNATURE-----

    iQIcBAEBAgAGBQJYsU1SAAoJEMPzj/CHV15DkfgP/RcJw9EtFiv/+4LIV5rrgqcF
    +FHEZiYb5jQhsqHrR7jS69rAwxzMD/rttQxMMw4cXBDh/dQaelwOVWbcy4DUwHaj
    c3gFOzt/42VK40LcQlEs
    =ON6z
    -----END PGP SIGNATURE-----

After you have copied it, click on the clipboard icon at the top taskbar and select "Decrypt/Verify Clipboard". 

{{< figure src="/images/tails_pgp_decrypt_verify_clipboard.png" class="borderimage" >}}

A new window should pop up which contains "Good signature from <name of the key pair that signed the text>" at the bottom, if the signature was correct.
{{< /tab >}}
{{< tab "Whonix" >}}
{{< hint "info" >}}
Before you can verify the PGP signed message, you need to [import]({{< relref "signing_a_message.md" >}}) the public key of the user that signed the message. So see where it is listed (e.g. on the vendor's profile on the market, or on the market's subdread) and then import it.
{{< /hint >}}

Copy the PGP signed message, it looks something like this:

    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA512

    Text of the PGP signed message.
    -----BEGIN PGP SIGNATURE-----

    iQIcBAEBAgAGBQJYsU1SAAoJEMPzj/CHV15DkfgP/RcJw9EtFiv/+4LIV5rrgqcF
    +FHEZiYb5jQhsqHrR7jS69rAwxzMD/rttQxMMw4cXBDh/dQaelwOVWbcy4DUwHaj
    c3gFOzt/42VK40LcQlEs
    =ON6z
    -----END PGP SIGNATURE-----

After you have copied it, open a new editor window, paste the signed message into it and click on the "Sign/Verify" button. A new window should pop up which contains "Good signature from <name of the key pair that signed the text>", if the signature was correct.
{{< /tab >}}
{{< /tabs >}}
