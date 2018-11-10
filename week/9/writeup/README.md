Name: Reginald Cudjoe 
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Reginald Cudjoe

1. Brute forcing the script was not a very challenging process. After opening the hash and password file, It was simply a series of for loops that prepend a-z on to a specific password and then using the sha512 format of the hashlib python library to do the comparison. One issue that I encountered was figuring out that the salted password needed to be encoded in order to hash. For this case, I used utf-8 and ensured that it still printed a valid hash. Another issue I encountered was not resetting the readlines() position after going through the hash and wordlist file. After fixing these two things I was able to get the output displayed below. 
![Part1](images/wp1.png)

2. The 2nd part was not difficult because of the prior experience with sockets. After observing the question format, I split the lines and parsed the question for the hash type and string. This was easy because all the question lines have the same format. To figure out how to use the hash, I looked up the documentation on the library and saw that the hashlib.new() and hashlib.updata() can be used to manually enter a hash format and hash it. After that I ran into an issue with sending a new line along with the hash. After searching I was that b should be appended to make the new line character into a byte literal and I was able to answer all the hash requests to claim the flag CMSC389R-{H4sh-5l!ngInG-h@sH3r}. The output is displayed below:

![Part2](images/wp2.png)