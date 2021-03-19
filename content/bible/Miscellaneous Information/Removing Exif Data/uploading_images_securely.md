---
title: Uploading images securely
weight: 110
---

# Uploading images securely

Images can tell the world a lot of information and can even reveal your true identity although you have followed all other steps in the DNM bible. So it is important to read and follow this chapter too because it can literally mean the difference between freedom and jail.

Just do give you an [example](https://ampedsoftware.com/) of what basic forensic video/photo software is capable of doing. Now imagine what forensic software on steroids law enforcement can buy with all their money.

## Making a photo

Even if you follow all the tips in this chapter it is still possible to identify the camera that you used because of other camera specific data that is much harder to obfuscate. Therefore it is highly recommended to either use a throwaway camera or one that you never used to make pictures that you uploaded online somewhere.

To get the image for your camera or mobile phone onto Tails, simply stick the SD card into your computer or connect your mobile phone with a USB cord to your computer when you booted Tails.

## Removing traces

To remove at least some of the traces of the images that you want to upload, do the following steps. Keep in mind that this is not 100% protection against all the forensic methods out there.

Right click on the image, hover over "Open With" and select "GNU Image Manipulation Program" from the context menu.

**Note**: you can enable the Single-Window Mode by clicking on "Window" (at the top of the middle window which shows your image) and then selecting "Single-Window Mode". This may make GIMP a bit easier to work with.

Then crop the image to remove any background details that could identify you using the "Crop Tool" in the toolbox (on the left side, click on the icon knife icon which says "Crop Tool: Remove edge areas from image or layers"). After you selected the area that you want to keep in the image, press Enter.

Now apply some noise to the image using "Filters" (at the top of the middle window) > "Noise" > "HSV Noise". The default values should be enough to remove any unique differences in the sensor in the camera that may be used to identify you. However if you are paranoid, play around with the settings to find something that is still relatively clear but applies more noise.

Save the image by going "File" > "Export As..." and store them in your Persistence folder. Uncheck all the options that you get (the list that contains entries like "Save resolution").

**Note**: this process also remove the EXIF data. It is short for Exchangeable Image File, a format that is a standard for storing interchange information in digital photography image files using JPEG compression. Almost all new digital cameras use the EXIF annotation, storing information on the image. That information can be used to de-anonymize you, e.g. because your smartphone put the GPS coordinates where the photo was made automatically in the EXIF data. But you do not need to worry about that any more as that data is already removed.
