section .text         ;declare this section to include executable instructions




global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame      
        mov rcx, 0 ;  General purpose counter register. 
  		call my_memloop ; Calls loop 

my_memloop:
	cmp rcx, rdx ; rdx holds the string lenDo the index comparison
	jge mem_done ; Quit if we have reached the end of string
	mov[rid+rcx], rsi ; Move the char into the memory address.Rcx for increment
	inc rcx ; rcx ++
	jmp my_memloop ; restarted loop

mem_done:
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!



global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        mov rcx, 0 ; Create index 
        call my_strloop ; Call loop 

my_strloop:
	cmp rcx, rdx ; Do the length comparison
	jge str_done ; Quit if end is reached
	mov r10, [rsi+rcx] ; Move char from source to a temp register
	mov [rdi+rcx],r10 ; Move char from temp to new destination
	inc rcx ; rcx++
	jmp my_strloop ; restart  



str_done:
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
