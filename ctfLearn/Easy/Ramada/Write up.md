1. open ida to disassemble 
2. have a look on here
![[Pasted image 20250416004731.png]]

is look like we need to pass in an argument and it must equal CTFlearn{

then ltr we found that v8 will strong the length if our argument 

for the next if condition it check whether the last of our argument is } 
 and the next if condition check whether v8 is euqal 31 while v8 is our length
3. thus in summarise must have flag of 31 length and start with CTFlearn{ , end with } .
4. after that i also found a check flag condition 
![[Pasted image 20250417004104.png]]

5. lets have a look on it 
![[Pasted image 20250417004125.png]]
the a1 is our input is looks like input * input * input = input ^ 3 
this input ^ 3 is equal to smtg mainly is our flag value

6. lets start with gdb
```gdb
b * main
b * CheckFlag
r CTFlearn{111111111111111111111}
c
si
```
rmb to step inside the checkflag  function
7. now we reach here 
![[Pasted image 20250417004541.png]]
8. continue step until the cmp 
![[Pasted image 20250417004612.png]]
based on the previous assembly we know that edx is input ^ 3 then we need to check the value stored in [rsi+rax* 4] u can print it in hex or decimal 
```gdb
x/x ($rsi+$rax*4)  -- hex
x/d ($rsi+$rax*4) -- decimal

```

9. u will get a value and this the flag characters 
![[Pasted image 20250417004830.png]]

but since it is input ^ 3 rmb to cube root the value and print it in ascii . just repeat the steps .

10 . CTFlearn{CLip1zzaner_Stalli0ns}