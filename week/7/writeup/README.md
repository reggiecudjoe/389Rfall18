Writeup 7 - Forensics I
======

Name: Reginald Cudjoe
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Reginald Cudjoe

## Assignment 7 writeup

### Part 1 (40 pts)

1. A JPG file.

2. The photo was taken at the John Hancock Center in Chicago, Illinois.

3. The time was 11:33am EST (16:33:24Z).

4. An iphone 8 back camera.

5. The photo was taken 539.5 meters above sea level.

6. CMSC389R-{look_I_f0und_a_str1ng}


### Part 2 (55 pts)

I first decided to run the binary and after seeing its output I was somewhat confused. I then ran the strings command with a length minimum of 5 and noticed that at the top there were three recognizable commands: fopen, fclose, and fwrite. I then decided to run gdb to step through the program in hopes that I would see what was being written. I set a breakpoint using "break main" and began stepping through the program. When I stepped it took me to a line that used fopen on "/tmp/.stego" and I realized that the .stego file must be where the flag is being written. After going to the directory and displaying hidden files I found the file and attempted to open it. That failed and I was unsure why. I decided to run the exiftool to see if I can determine the file type and any other key information. In the type section, I noticed that it mentioned an unknown format header byte but information that appeared to look like a JPEG format. I opened the binary in sublime and decided to google JPEG format headers to try and repair the file. I saw that the null byte was the issue and attempted to change it to e1, e0, and fe. All of those attempts failed and I decided to try and delete the entire byte. That fixed the file and it revealed a picture of a stegosaurus. I was confused by this but then I remembered steghide and its ability to reveal hidden messages (stegosaurus, steghide, coincidence? I think not). I ran the command on the slides and I first tried "stego" as the password and that failed. I then tried stegosaurus and got the flag: CMSC389R-{dropping_files_is_fun}.

	Format header source: https://digital-forensics.sans.org/media/hex_file_and_regex_cheat_sheet.pdf
