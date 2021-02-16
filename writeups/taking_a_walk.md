## GunnHacks 7.0 Taking a Walk Challenge Writeup
Points: 300
> I took a walk around my neighborhood last week, and I took some photos. Unfortunately, most of them are of the sidewalk (I'm a really terrible photographer), so now I don't know where I went! For each photo, can you find me the first letter of the street it was taken on? (The first photo was at a school, so use the first letter of the short school name.) If you can find the streets, the letters should spell out a word, which you can submit as gunnHacks{the_word}. Make sure to submit the word in lowercase. Here are the photos I took: [img.zip](/taking_a_walk/img.zip)

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
