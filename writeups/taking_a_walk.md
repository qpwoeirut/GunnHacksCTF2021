## GunnHacks 7.0 Taking a Walk Challenge Writeup

We're given 7 images, and we need to find where they were taken.
The first is a photo of a sign at Henry M. Gunn High School, so we get the first letter for free.
Since the description says to use the short school name, the first letter is `g`.

For the rest of the images, it'll be a bit more difficult since all we see is a bunch of concrete.
We'll need to use image metadata to locate where these images were taken.
Many phones have a setting which will save the location by geotagging them.
(On a related note, you should probably figure out if your phone has that setting enabled or not.
This can be rather dangerous for privacy reasons.)
This geotag information can be viewed with a metadata viewer, both online and locally.

Once that was figured out, the remainder of the challenge consists of finding the coordinates for each image, looking up the street on some map, and adding that to the flag.
I tried to make the street that the image was on unambiguous, but it looks like participants still had a bit of an issue, which is unfortunate.
