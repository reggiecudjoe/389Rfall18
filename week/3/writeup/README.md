Writeup 3 - OSINT II, OpSec and RE
======

Name: Reginald Cudjoe
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Reginald Cudjoe

## Assignment 3 Writeup

### Part 1 (100 pts)

1. Weak Password
    Krueger's password to his admin account was very weak and vulnerable to dictionary attacks. He used "pokemon" which is a simple 7 letter word without any special characters. Attackers using a list of common words (as we did in class) would be capable of brute forcing their way into his systems and other accounts that use the same password. According to research done by Red Data Security, modern password crackers can calculate all 7 ASCII character combinations in 2 hours and much less time for anything lower. Attackers may even able to narrow down the possible passwords by applying OSINT techniques and discovering the things that he is interested in on his social media accounts. To fix this, Kreuger should make his password at least 10 characters long and incorporate a mixture of uppercase, lowercase, and special characters. He should also avoid using common words or things related to him and change the password every 60-90 days in case the password is leaked. These methods increase his password's complexity and make a brute force attack very difficult to accomplish. Red Data estimates that the time to calculate all 10 digit ASCII combinations is 4 years and the time continues to increase as they get larger. Another way to assure that his password is safe would be to conduct a Brute Force Search Space Analysis. this can be done using online programs that compute the relative time it would take to guess the password during a brute force attempt.

    Sources: 
    https://www.perspectiverisk.com/top-5-common-network-vulnerabilities-weak-password-policies/
    http://web.cs.du.edu/~mitchell/forensics/information/pass_crack.html

2. Open Network Port
    Krueger left an open port on his admin server that allowed us to access his website and information not meant for the public. Using this port, attackers can also inject, corrupt, and delete private information. This vulnerability is especially dangerous when combined with his weak password mentioned above. The first thing that Krueger should do is to use a Secure Socket Shell (SSH) when accessing his website. This would provide him with authenticated and encrypted data communication while he accesses his network. Attackers would have difficulty eavesdropping and gaining access to his user information. Another important thing to implement would be two-factor identification. If attackers do gain access to his username and password, they would also need another means to verify their identity before gaining access to his data.

    Sources: 
    https://searchsecurity.techtarget.com/definition/Secure-Shell
    https://www.inmotionhosting.com/support/website/linux/ssh-advantages



3. robots.txt Information
    On the robots.txt, Krueger left information on a directory called secret that was not meant to be accessed by the public. After going to such a directory, attackers may discover private information on the page or the source code. The allow and disallow parameters listed on the file may contain useful information for attackers to exploit. Directories that are not secure may not be accessed by search engines bots but may be pulled by attackers. Kreuger should make sure that all of his sensitive areas are secured (using passwords, authentication, etc.). Disallowing a directory but not protecting it is security through obscurity and Krueger should avoid that by locking down the private parts of his platform.

    Source:
    https://www.synopsys.com/blogs/software-security/robots-txt/