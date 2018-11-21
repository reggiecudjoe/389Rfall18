Writeup 10 - Crypto II
=====

Name: Reginald Cudjoe
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Reginald Cudjoe

## Assignment 10 Writeup

### Part 1 (70 Pts)

Part 1 was somewhat difficult because I ran into a few issues. Step was easy: after implementing the sockets I able to recieve the initial data containing the hash of secret and the message. The only thing really required at this point was to extract the last 32 characters for the md5py to decode into hex. With step two, I first had to figure out an effective way to append the endian to the padding. I had difficulty trying to do it manually but after google python endians I was pointed to the struct.pack() function and the 'Q' option for little-endian. After this I was able to construct the payload and send it to the server but I ran into an issue with the for loop to construct secrets. During the time between sending the payload and recieving the data, the server would not send anything back. I realized that it must take the server some time to process the payload so I added a sleep within the function before the recieve and I got the following flag: CMSC389R-{i_still_put_the_M_between_the_DV}.


### Part 2 (30 Pts)
This part was not very difficult. I intially ran "gpg --gen -key", inputed a name, email, and then a password to create a public key. After this, I imported the pgpassigment.key using "gpg --import pgpassignment.key" and after a delay it outputted the recipient email "president@csec.umiac.umd.edu". Lastly, i used "gpg --output message.secret --encrypt --recipient president@csec.umiac.umd.edu "hello" to encrypt the file "hello" as message.secret. 
