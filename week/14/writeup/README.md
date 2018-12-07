Writeup 10 - Crypto II
=====
5'or'1'='1
Name: Reginald Cudjoe
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Reginald Cudjoe

## Assignment 10 Writeup

### Part 1 (70 Pts)
I realized that a sql injection was necessary based on the hint in the instructions. I was already familiar with the inputs involving a sql injection from CMSC414 so this task was not too difficult. After clicking through some of the links, I realized the query used the "id" field to access the data table so I would have to form input to be executed. I knew I needed to use an id that was not valid to reach the 'OR' condition so I started with 5' OR '1'='1. This failed initially and I attempted to try a different arrangement of quotes. After this, I googled the standard format for sql injection attacks and noticed that some sources used lowercase in order to achieve the goal. I then tried 5' or '1'='1 and got the flag CMSC38R-{y0U-are_the_5ql_n1nja}.

### Part 2 (30 Pts)
1. For the first part, I used a hint and saw that it mentioned trying html tags. I entered <h1> "hi" </h1> and saw that it printed it in bold. At that point I realized that the search will directly interpret and execute any code so I simply used  <script> alert("hi") </script> to complete the first challenge.

2. I tried to use the same script command that I used for the first part but a hint indicated that the script tag would not work. I realized that I needed to find an html element that executes javascript, so upon searching the internet I found that the img tag could be used in with the "onerror" condition. I initially wrote "Hey <img src="i.jpg" onerror="alert("hey")"/>" into the box but that did not work. I realized that I needed to use single quotes in the alert box and "Hey <img src="i.jpg" onerror="alert('hey')"/> was able to complete the challenge.

3. This one was not difficult. To inject the code I inserted a ";" after the the frame number and tried https://xss-game.appspot.com/level3/frame#2;"<img src="i.jpg" onerror="alert('hey')"/>" which initially failed. I noticed that in the image box the words ".jpg" were printed but the quotes on each side were not equal so I changed the quotes surrounding my command to single and https://xss-game.appspot.com/level3/frame#2;'<img src="i.jpg" onerror="alert('hey')"/>' completed the challenge.

4. This one took a some time to figure out how to properly format the input. I saw after looking at the hint I saw that the time field was passed into "startTimer('{{ timer }}');" and I knew that it could be exploited. I first tried "3; alert('hey')" but that failed. I realized that I needed to close the quotes and parenthesis of the timer command in order to allow the alert command to execute. After playing around, I tried 3'); alert('hey and passed the level.

5. Exploiting the email field di did not work because the source code does not collect the field. I noticed that an href takes whatever is passed to the {{next}} parameter and executes it. Looking at the url, I see that confirm is always passed and I would need to change the request. After entering "https://xss-game.appspot.com/level5/frame/signup?next=alert('hey')" and clicking next, the challenge was completed.

6. This challenge was the hardest of the 6. I inspected the source code and saw that a regex style matching was used to block "https" but the entrance was case sensitive and could be avoided by just changing the case of one of the letters. After examining the hints I saw that a could get a javascript file from google's jsapi. After examining the api, I got the call back and I changed the tense of the "https". The input "https://xss-game.appspot.com/level6/frame#Https://www.google.com/jsapi?callback=alert" completed the challenge. 