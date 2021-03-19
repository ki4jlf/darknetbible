---
title: Using jabber (XMPP)
weight: 30
---

## Chatting with someone

After setting up your jabber account to chat with someone you will need to add them by going to: Buddies > Add Buddy (close and re-open all the Pidgin windows if the "Add Buddy" selection is disabled).

Now enter the username the the other person gave you. I could for example be username99@jabber.calyxinstitute.org. Optionally you can also set an alias for him in the line below which gets shown in the chat window when you chat with that person (instead of the long username which you previously entered). To confirm click the button "Add".

The user you want to add will receive a notification when he comes online again where he gets asked to authorize you (he sees your username). He has to click the "Authorize" button and confirm the new dialog window where he can also set a local alias for your username.

When he did that and he is currently online, you will see him in your "Buddies" list. You will also see the small authorization notification at the bottom of your "Buddy List" window where the other user wants to add you to their buddy list. Click on authorize.
{{< figure src="/images/pidgin_authorize.png" class="borderimage" >}}

That's it! Now double-click on his name in the buddy list, click on the red "Not private" at the bottom right and select "Start private conversation". 
{{< figure src="/images/pidgin_private.png" class="borderimage" >}}
Then the chat window will print some messages like "Attempting to start a private conversation with other user's username here"
{{< figure src="/images/pidgin_unverified.png" class="borderimage" >}}

Now you both can chat securely!

## Authenticating your buddy

You should see at the bottom right it says "unverified" while you have established a secure chat with some other user, it may be the wrong user. That means you could chat the whole time with a wrong person who might be malicious. In most cases the other person (your are now chatting on XMPP with) gave you his XMPP username through an encrypted message or a similar channel.

So if you are sure that the message (where he told you his XMPP username) that the other user sent you could not be manipulated, then you can skip the authentication / verification. If however you received the username through for example a clear text message on a DNM, this message may have been tampered with by LE who might have taken over the market. So to be sure that you are chatting with the right user, do the following.

Click on the "Unverified" at the bottom right and select "Authenticate Buddy".
 Now you can enter a question and a secret answer.
 {{< figure src="/images/pidgin_authenticate.png" class="borderimage" >}}
  It is sufficient if you choose for example "check your email account" as a question and a random string like "Af!J}m" as the secret answer. Before you click on the "Authenticate" button, send the other user that secret answer through a secure channel first. For example using his PGP key you have saved and sending an encrypted email to his email address that he usually uses. The content can be like "The answer to my authentication question is secret answer here".

Now click the "Authentication" button and you should get a window waiting for the authentication to be completed. The other user now gets prompted to enter the answer for your authentication question and if he does it successfully then you will see the content of your authentication progress window change to "Authentication successful". You can close it by clicking "OK".

Now you have confirmed that you not only established a secure chat with some user, but also with the correct user. The other user can also decide to ask you such a authentication question so you are marked as authenticated on his side too.

It should now say in Green "Private" 
{{< figure src="/images/pidgin_verified.png" class="borderimage" >}}