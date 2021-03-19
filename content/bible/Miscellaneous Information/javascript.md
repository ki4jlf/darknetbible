---
title: Javascript
bookCollapseSection: false
weight: 10
---

# Javascript warnings

If you have javascript on you have probably gotten a warning on a few different sites by now. Javascript is not naturally dangerous, but it can be used in different situations to deanonymize who you are. 

Again this is why we say keep your darknet activities, and clearnet completely separate. Certain websites can use javascript to see what your real IP address is behind tor.

## Disabling javascript

**Note:** You will need to do this everytime you restart tails! 

* When you first open tor click the {{< icon "/images/security-level.png" "dice" >}} icon in your upper right hand corner.

* Next click Advanced security settings. You should see a window like this open:
{{< figure src="/images/security-levels.png" class="borderimage" >}}

* Now click safest

Please note: You may still get an occasional message from a site saying you have javascript enabled. Due to it being blocked only by NoScript. NoScript will block javascript, but it ***could*** fail. For better results after you have set the security slider to safest, **and** do the following. 

* In your address bar type About:config

* Click accept the risk and continue

* In the search bar type java

* Towards the top of the list you should see a value that says javascript.enabled double click that to set it to false.

and you're done!

