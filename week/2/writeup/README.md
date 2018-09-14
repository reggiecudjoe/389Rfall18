Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Reginald Cudjoe
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Reginald Cudojoe

## Assignment 2 writeup

### Part 1 (45 pts)

1. His real name is Fred Krueger.

2.1. He is located in Silver Spring, MD: A google search of the provided username yielded his STWITY profile with this information.
  2. His website is cornerstonearilines.co: This was also yielded by the google search that bought up his STWITY profile.
  3. His twitter handle is @kruegster1990: This was also located on his STWITY profile.
  4. His reddit username is also kruegster1990: This was found during the google search of the username.
  5. He has a zara larsson account with the username krueger190: Also found during a google search of the username.
  6. His email is kruegster@tutanota.com: This was found on his website's about section. 
  7. His instagram is also @kruegerster1990: This was found by searching his username on instagram. After discovering the twitter, I searched facebook and instagram for possible profiles. 

3. The IP address of his current host is 142.93.118.186. This was found using the Domain Dossier on centralops.net.

4. After looking at robots.txt I found the secret directory. On the page source I found the flag "CMSC389R-{fly_th3_sk1es_w1th_u5}""  

5. Yes, 216.87.155.33 links to dsn1.registrar-servers.com and 216.87.152.33 links to dsn2.registrar-servers.com. Both of these were found on dnsdumpster.com

6. There was an IP address on the admin page address bar. After using mxtoolbox, I saw that it led to an Apache server.

7. Mxtoolbox showed that the server was running on Ubuntu.

8. On dnsdumpster.com there was a flag: "CMSC389R-{dns-txt-rec0rd-ftw}"
On the secret source code: CMSC389R-{fly_th3_sk1es_w1th_u5}
On the homepage source code: CMSC389R-{h1dden_fl4g_in_s0urce}

### Part 2 (55 pts)

First, to detect the port I used the nmap command. The first 1000 ports failed to have a but a search from 1001 to 2000 yielded vulnerability at port 1337.
After this, I created a brute force function using stub.py. I created a for loop that constantly connects to the server and tries mutliple passwords from the rockyou.txt file in hopes that it can access the file. If a message containing success is printed, the code prints the current password and exits the loop. This condition was added after noticing that "Success!" is printed after successfully finding the password. Before this, it was necessary to review the output as the program printed. In an attempt to guess the user name I first used his email Kruegster@tutanota.com along with the password list. After failing to yield an answer after 45 minutes, I decided to try his common username; kruegster1990 along with the list of passwords. This failed as well so I attempted to use just his last name Krueger. After that failed I tried to use simply kruegster as this was still a part of the name he commonly used. After waiting roughly 15 minutes the loop was broken and the password "pokemon" was printed on the console. Using this password, I used the nc command to ssh into the server. After entering, I used the ls linux command to look at the directories. I immediately chose "home" as it was likely that user would store personal information in non-system folder. After discovering the flight records I saw that there were several files. At this point I remembered that there was a ticket listed on the instagram along with several pictures of pokemon. After inspecting the instagram I saw that AAC27670 corresponded to one of the files in the directory. Performing a cat linux command led me to the flag CMSC389R-{c0rn3rstone-air-27670}.
