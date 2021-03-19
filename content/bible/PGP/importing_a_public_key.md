---
title: Importing a public key
weight: 10
---

# Importing a public key

To be able to send someone an encrypted message (e.g. your address to a vendor), you need their public key. In order to get a vendor's public key you have to visit his profile and look out for a link that is named like "PGP key" or "Vendor public key". Sometimes it is also featured directly on the vendor's profile page.

A public key looks like this:

    -----BEGIN PGP PUBLIC KEY BLOCK-----
    Version: GnuPG v1

    mQINBFhNDOsBEACzwJJVsMo7sIiLhvCsLx2n+DVHzw1trM/C8Yao8EmWdDYe3ei9
    mXRqSudbD6S4KvJfm+ZeOlEQ6gGoG2q3aFYASRgcK7WDhs+jwG42EA+j2oIpU/EO
    8EQXTmTn8T+LQT84JZ5KkiZZp2CqLU8RVszfkKEj1oX/sO5watxNQur4fbk9FiCA
    1MjHMYir1g==
    =TV04
    -----END PGP PUBLIC KEY BLOCK-----

The gibberish part in the middle will be a bit longer though. The "Version" line may also be different or not exist at all.

{{< tabs >}}
{{< tab "Tails" >}}
{{< hint warning >}}
Due to a bug in the PGP software on Tails the easy way of importing a public key by pasting it in the program is currently broken. A workaround is described below.
{{< /hint >}}

Find the public key that you want to import and copy it to your clipboard. Then open the text editor and paste it in there.

{{< figure src="/images/tails_pgp_pubkey_text_editor.png" class="borderimage" >}}

Click save and name the file `key.asc`. 

{{< figure src="/images/tails_pgp_pubkey_text_editor_name.png" class="borderimage" >}}

Now open the file browser and right click on the `key.asc` file, then click Import Key. 

If this option is missing there was a formatting problem with the key you copied. Make sure that you copied all of the key including the lines with the BEGIN and END statements and all the dashes. PGP is very picky about formatting errors.

{{< figure src="/images/tails_pgp_pubkey_open_with_import_key.png" class="borderimage" >}}

If everything went successfully, a notification should pop up telling you that the key is imported.

{{< figure src="/images/tails_pgp_pubkey_key_imported.png" class="borderimage" >}}

If you get a pop up telling you that the import failed, there is something wrong with the public key.

{{< figure src="/images/tails_pgp_pubkey_import_failed.png" class="borderimage" >}}

Double check that you copied the entire key.
{{< /tab >}}
{{< tab "Whonix" >}}
Find the public key that you want to import and copy it to your clipboard. Now copy that public key and open the KGpg window. At the top you see a few buttons, one of which is named "Import Key". Click it and select "Clipboard" on the window that appeared. Confirm by clicking "OK".

If all went well, you should get a message like "1 key processed. One key imported: One RSA key imported.". Close the window by clicking on "OK" and check the list of PGP keys to see if it contains the PGP key you just imported. When you find it, right-click on it and select "Key Properties". Then select "Ultimately" from the drop-down menu for the field "Owner trust" and confirm by clicking "OK". This will make it easier for you to quickly encrypt messages with that PGP key (i.e. send encrypted messages to that vendor).

If you get an error like "Key importing failed. Please see the detailed log for more information.", there was probably a formatting problem with the key you copied into the clipboard. Make sure that you are copying all of the key including the five dashes at the beginning and end of the key and the BEGIN and END statements. PGP is very picky about formatting errors.
{{< /tab >}}
{{< /tabs >}}
