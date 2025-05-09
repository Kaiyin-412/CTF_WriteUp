1. first use ida to have static analysis 
2. first info gather is thr is argc mean we can input 
![[Pasted image 20250414003440.png]]
3. is look like we need to pass in CTFlearn{ as the input  
![[Pasted image 20250414003518.png]]
4. next v6 = length of the v5 thr looks like it have a length of 28 so ltr in gdb we need to alter it .
5. actually i have try before that , i found that i must let input at v5[17] = 95 which '_'
and also for v5[22] . i also know the last character must be } so lets start with gdb .
![[Pasted image 20250414003726.png]]

6. start run
```bash 
gdb -q ./Rangoon
```

7. then we run it with input CTFlearn{
```gdb
r CTFlearn{
```

8. we continue ni until here which is checking for the strlength
![[Pasted image 20250414004417.png]]
in ida 
![[Pasted image 20250414004445.png]]

9. from here we know that r14 is storing the string to compare
![[Pasted image 20250414004634.png]]

10. thus we change it to length of 28 with last character of '}' rmb at 17 and 22 put _
```gdb
set $r14 = "CTFlearn{       _    _     }"
```

11. after that we ni until here which compare for _
![[Pasted image 20250414005605.png]]

in ida 
![[Pasted image 20250414005627.png]]


12. at first i try to make the char at input 17 become _ but i found it cannot so i decide to check what is store in [r14+0x11]
13. its look weird is like showing the char after length 15
![[Pasted image 20250414005844.png]]

14. cuz it just want to compare with _ so we change it 
![[Pasted image 20250414010054.png]]
15. now we continue move on to the next compare
16. based on the flags it also show that the zero flag is set means they are equal (it is with bold)
![[Pasted image 20250414010215.png]]

17. now the same thing we doing the samething
![[Pasted image 20250414010341.png]]

18. now just continue move on  and the flag is shown 
![[Pasted image 20250414010433.png]]
 or u can 
 ```gdb
 x/s $rbp
```


