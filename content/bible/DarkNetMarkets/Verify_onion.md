---
title: How to verify an onion
weight: 30
---


# How to verify an onion address

Verifying onions. It's such an important thing yet so many people don't know how to do it properly. **Always,** regardless of where you get the onion from take the time to verify it. You never know when you have a typo, or a simple error. Taking the 10 seconds to verify can save your coins from falling to a phisher.

Darkfail has a great tool to help you do it, but no one resource should be blindly trusted. You should always **manually** verify the onion address yourself!

**Note:** Before you can verify you are on the correct Onion make sure you understand how to [verify a PGP signature. ]({{< relref "verifying_a_message" >}})

---

Now that you know how to verify a signature we can verify an onion address. First we need to get a markets pgp key. Most markets put them on their subdread, but if not you can put /pgp.txt at the end of the mirror you want to verify.
It should look like this: MarketOnionAddress.onion/pgp.txt

You'll probably have to complete a captcha. Then you should see the markets PGP key. Import the key like normal. (See above if you need help)

Once you have it imported put /mirrors.txt at the end of the onion you are on.
It should look something like this MarketOnionAddress.onion/mirrors.txt You should see a page with some information like this on it: 



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



**Note:** Some markets don't use mirrors.txt check their subdread for what you should put at the end to verify.

If you see a message like above you can now verify the message is signed by the market pgp key you imported.  It should come back with good signature at the bottom ,and at the top you will see a list of the current market mirrors. **Make sure the address you are on matches one of the ones in the signed message.** If it does you are on a official market onion!

Once you do this a few times it really only takes about 15 seconds to do. Always take the time to verify an onion regardless of where you get them from