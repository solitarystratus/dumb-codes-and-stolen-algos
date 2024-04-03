# dumb-codes-and-stolen-algos
My project supervisor keeps asking me to solve the same problem using different approaches. So I ended up choosing the easiest problem from junior school because my brain can't comprehend complicated things. 
Here's what I came up with. 
I used the formula to calculate distance between any two given points in the XY-plane because that's the only formula I remember correctly and know where to apply. 
As of now, I used two algorithmic paradigms to solve the problem in two different ways. 
The brute-force approach takes random pair of points from the given set/file (I used .txt file), creates random pairs and calculates the distance, repeats this process until all the pairs have been evaluated. 
Meanwhile, divide-and-conquer does something more complicated that took me more than an hour to understand and then TWO MORE DAYS to actually write a code that follows this approach. So what this approach does is, it divides the given set into equal halves and then calculates the minimum distance separately for both halves. Then it takes the minimum of the two former minimum distances. The process repeats until all the pairs have been evaluated.
