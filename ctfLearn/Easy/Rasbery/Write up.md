1. first i try put it in ida and do some simple analysis i found is it kinda smtg cmp with a string , that string should be the flag 
2. then i started gdb , the first ques i meet is i could not pass the check length string is look like i need to pass in an argument thus i guess it and run with 
```gdb
break * _start
run CTFlearn{
```

3. after move i found the function name like firstletter and secondletter ...
4. then i check again in ida it have until nintheen thus i simple guess it cuz i dun wan stuck on the check length funciton
```gdb
run CTFlearn{111111111}
```

5. have a look here
![[Pasted image 20250416002145.png]]

6. mainly we just look cmp thr and if not equal we will jump to a badchar function which indicates us is wrong . So in here just cmp bl , 0x43 thus 0x43 in ascii is C 
7. so we just repeat the process for some letter it under xor , mul and div so we need to revers eto get back it 
8. the final flag : CTFlearn{+Fruit123}



**what i learn** 

In C it default can pass in argv and it will be stored on stack 

this is the stack after i run with CTFlearn{+Fruit123}
![[Pasted image 20250416002655.png]]

in C its look like
```C
main (2 , /home , CTF..)
```

the first wan 2  means 2 argument is pass in .
while the CTF will be passed in first follow by the others . 

```asm
mul ebx
```
this mean eax = eax * ebx will stored in eax

when div 

```asm
mov ebx , 0x5
div ebx
```

this will take eax divide by ebx 

eax will stored the quotient , edx stored remainder
