---
title: Decrypting a message
weight: 40
---

# Decrypting a message

{{< tabs >}}
{{< tab "Tails" >}}
First copy the encrypted message. Then click on the clipboard icon and select "Decrypt/Verify Clipboard".

{{< figure src="/images/tails_pgp_decrypt_verify_clipboard.png" class="borderimage" >}}

Enter the password for your key if requested.

A window will show up the decrypted message:

{{< figure src="/images/tails_pgp_gnupg_results.png" class="borderimage" >}}
{{< /tab >}}

{{< tab "Whonix" >}}
Open the KGpg window and select File -> Open Editor. Paste the message that you want to decrypt in the new editor window. To decrypt it, click on the "Decrypt" button at the bottom. It will then prompt you for the password of your PGP key, enter it and confirm again by clicking on "OK".

If all went well, you will see the decrypted message in the editor window. To reply you can open a new editor window and type in the response (and check the first editor window with the decrypted message during that process if you need to re-read parts of the decrypted message again).
{{< /tab >}}
{{< /tabs >}}
