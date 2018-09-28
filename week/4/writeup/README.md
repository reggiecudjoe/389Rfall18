Writeup 3 - Pentesting I
======

Name: Reginald Cudjoe
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Reginald Cudjoe

## Assignment 4 Writeup

### Part 1 (45 pts)
To investigate the vulnerability, I first observed the output of the "nc cornerstoneairlines.co" command with its own IP address. I noticed that following the IP, the script runs the ping command. In a past security course (CMSC414), I knew that SQL code injections are traditionally done by first ending the input command and appending another command. After a small amount of research, I decided to try to insert a semicolon after the inserted IP and attempt to run a shell command. My belief was that the input being taken into the program would be executed no matter what was provided. That also means that any registered linux commands will just be evaluated and run. This led me to try "000000000; ls" to see if any information would print. I saw that after the statistics the current directory information was printed. I then realized that the length of the initial IP did not matter as long as it did not contain letters. I first tried "0; cd root && ls" and that yielded no results. After this I decided to check the home directory with "0; cd home && ls" and saw flag.txt. The last command to run was "0; cd home && cat flag.txt" and that revealed "CMSC389R-{p1ng_as_a_$erv1c3}". 

To determine where Krueger's vulnerability was, I searched several directories including run, lib, lib64, and others until I located "container_startup.sh" in the opt directory. After running cat, I noticed this section of the script:

echo -n "Enter IP address: " read input >&2 echo "[$(date)] INPUT: $input" cmd="ping -w 5 -c 2 $input" output=$(eval $cmd) echo $output

The issue here is that Kreuger runs the eval command on whatever input he receives. In "output=$(val $cmd)" the program will evaluate whatever is placed in "$input" and that allows attackers to run any real command. To fix this, I would recommend that he sanitize his input by putting quotes around the entire text. He must also make sure that instances of words that contain a quote be replaced with "\'" to avoid the possibility that attackers will close the leading quotation mark, inject their command, and then close the ending quotation.


### Part 2 (55 pts)

In order to craft the shell wrapper for part two, I had to capitalize on the command injection vulnerability. The first step was to create the base interface. This was done by creating a main method with a "while True" loop to wait for user input. The next step was to create the quit function which exits the program and then the shell and pull functionality. If those three inputs are not provided, the program simply prints the help menu which will account for malformed input and the call to help. For the shell, it was first necessary to establish a connection to the cornerstone port using sockets. The next step was to ensure that the input provided by the user is sent to the server. This operation had two cases. Case one was a call to "cd" and in this scenario, it is necessary to keep track of the current working directory between command calls; the server simply disconnects and this information is not stored. After storing the pwd, each subsequent call requires that the code travels to the pwd before executing the command. At the end of a call to "cd" the "pwd" command is called and received in order to store any directory changes. After this case was completed, the other case was all other commands. With calls to things like "ls" and "cat", all that is necessary is it head to the current directory and the server will execute the command. This was all that was required of the shell. When finished, a call to "exit" will leave the shell and go back to the base program. The last part to implement was the pull command. This was simple as it was only necessary to call "cat" on the remote directory and then save the output in a string to be written to a file. It was necessary to check if three elements were provided to the command line or else the call would count as malformed input.    
