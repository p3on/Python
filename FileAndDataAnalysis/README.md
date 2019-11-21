# File Analysis snippets

Snippets that deal with analysis of filecontent, counting bits and generating images with the data supplied. 

I used this for checking the randomness of a RNG (claimed to be a True-RNG), this is a rudimentary analysis and does not determine if or if not there is true randomness within the generated data.

## Index

- [bitcounter](#bitcounter)
- [bw_plot_img](#bw_plot_img)

## bitcounter

processes a file on binary level and counts the 1s and 0s => used it as a sanitycheck while testing the output of a crng.

## bw_plot_image

Takes either a binary or 'nomral' input and prints an image from the values - interesting when processing output from rng to visualize the numbers.
