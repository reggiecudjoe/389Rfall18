Writeup 5 - Binaries I
======

Name: Reginald 
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Reginald Cudjoe

## Assignment 5 Writeup

Before starting, I reviewed the slides to understand the basics of taking in parameters and using them for loops. Initially, I had three calls to mov to take the three parameters but I realized that the rdi, rsi, each store the values. For the loop construction, I used the cmp function from the slides and looked up the command for greater than or equal too which was jge. Using rcx as my index, I attempted to move the character using the rsi to [rdi+rcx], increment rcx and restart the loop. When running the main, I noticed that there were issues with my output. My initial thinking was that there was an issue using a higher bit register on lower bit data. I was unsure about the issue so I referenced the slide's Memory Instructions section, I saw that the size of memory is either explicit in instruction or implicit by register size; using a larger register without specifying one byte was messing up my output. Referencing the chart in the beginning, I saw that sil was a lower bit version fo rsi. I changed by command to "mov byte [rdi+rcx], sil" and the memset output was correct. Keeping this in mind, the 2nd function was executed much smoothly.

For strncpy, a similiar methodology was used. After creating my loop index and setting my greater than or equal to condition, I copied the data using the technique I discovered in the first function. To take the character from the source, I moved it into the low bit version of the rbx register bl. I then moved the char from bl into the memory location [rdi+rcx]. This operation gave me the correct output on the first try.  
