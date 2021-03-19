---
title: Creating a database
weight: 10
---

# Creating a KeePassXC database

{{< tabs "creating" >}}
{{< tab "Tails" >}}
{{< hint info >}}
Before creating a new database make sure that you have set up and unlocked the [persistent volume]({{< relref "setting_up_persistence" >}}).
{{< /hint >}}

On the welcome screen, click on 'Create new database'. Alternatively, click on "Database" in the menu bar -> "New database".

{{< hint danger >}}
**Make sure you save the database on the persistent volume**. If you fail to do this your database will be gone when you restart Tails.

{{< figure src="/images/tails_keepassxc_persistent.png" class="borderimage" >}}
{{< /hint >}}

You will now enter your master password. This is the only password you will need to remember since it will be used to keep all your stored secrets safe. It must not be easy to bruteforce or guessable by an attacker, anyone that can guess your master password has access to ALL secrets in the database. 

The best way to create a password that is both strong and memorable is to create a [mnemonic](/images/password_strength.png). A mnemonic of at least 5  words or more is recommended.

You can use the built-in passphrase generator for inspiration. Click on the {{< icon "/images/password_generator.png" "dice" >}} button in the toolbar. Under the password field select "Passphrase". Adjust the word count to the desired length. Then keep pressing "Generate" until you come across one you like. Press "Copy" to copy the passphrase to the clipboard and close the password generation window by pressing the {{< icon "/images/password_generator.png" "dice" >}} button once more.

Think of a story that incorporates all the words in the phrase, this will help you to remember your mnemonic. If you fear you might forget your password you can write it down on a piece of paper and store it in an inconspicous location until you know it by heart. 

After entering your password, click "OK".

{{< hint danger >}}
**You should now restart Tails to make sure that your database is on the persistent volume and that you can still open it.**
{{< /hint >}}
{{< /tab >}}
{{< tab "Whonix" >}}
{{< /tab >}}
{{< /tabs >}}
