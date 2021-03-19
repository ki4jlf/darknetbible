---
title: Removing Exif Data
bookCollapseSection: true
weight: 60
---

# Removing exif data from images

One day you might find yourself needing to take a picture of the product you ordered. Perhaps it's for a review, or you've found yourself in a dispute. 

**What is exif data?**

EXIF stands for Exchangeable Image File Format. When you take a picture with your phone, camera, whatever it writes information in the file. This data ranges from information about your camera (or phone) to exact GPS coordinates. Before you upload an image make sure **you** remove the exif data yourself. 

{{< hint danger >}}
**Note:** Never use a service or website to remove the exif data for you! You never know when this service is saving a copy of the original image on their end!
{{< /hint >}}

Luckily Tails provides a very handy tool to remove this data! 

* To remove this data simply right click on the image file you wish to remove it from. 
{{< figure src="/images/Metadata.png" class="borderimage" >}}
* On the context menu click remove meta data. 
* You will see a new file created that is cleaned of exit data.