---
title: Transactions not getting confirmed
weight: 60
---

# Transactions not getting confirmed

Bitcoin transactions become "confirmed" when miners accept to write them in the Bitcoin blockchain. In general, the speed of confirmation depends on the fee you attach to your transaction; miners prioritize transaction that pay the highest fees.
Another reason could be that the Bitcoin network is overloaded at the moment. Sometimes a lot of unconfirmed transaction rack up (tens of thousands) these have to get processed, which will take a while.
However for now you have to be patient and wait. It can take several hours or sometimes over a day for a transaction to get confirmed. Making posts about it on {{< subdread "/d/DarknetMarketsNoobs" >}} is not confirming your transaction faster.
In the meantime you can check if the destination address of the transaction is correct, because if not you can wait forever for the coins to arrive.
Make sure that you use the transaction fee that is dynamically created by Electrum next time (by default it will get confirmed within 5 blocks). That means just let the slider under the amount field be in the middle in the "Send" tab.
There are however two ways which can speed up your transaction:

- Increase the transaction fee in Electrum. This is only possible for "replaceable" transactions. To create this type of transaction, you must have enabled "Replace by Fee" in your preferences, before sending the transaction. If it takes too long till this transaction gets confirmed you can right click on the transaction and then upgrade the fee to make it get confirmed faster (only works if you did not spend the full amount of bitcoins in your wallet).
- If you sent the bitcoins to an address you do not control (e.g. a market), the best you can do is try the ViaBTC Transaction Accelerator. It may or may not work.

## FAQ

#### Can I cancel a transaction I made?
No, you will have to wait till it get confirmed eventually or rejected by the Bitcoin network.

#### Will I lose my bitcoins?
No, you will just have to wait some time till it gets confirmed or rejected.
