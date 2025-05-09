1. first we unzip the file 
```bash
unzip Reykjavik 
```

2. next we open ida to analysis it 
3. after some simple ananlysis i found that we need to bypass it 
![[Pasted image 20250413002344.png]]

the first wan 
```bash
cmp edi , 1
```
if it equal to 1 we will be jump to wrong path thus we need to change it 

4. run with gdb 
```bash
gdb -q ./Reykjavik 
```

5. we first set a breakpoint at main and continue step until cmp rdi , 1
```bash
b * main
```
![[Pasted image 20250413002643.png]]

6. next we set rdi = 0x2
```bash
set $rdi = 0x2
```

7. after that we will be comming to here  
![[Pasted image 20250413002739.png]]

now we should be aware of the repe cmpsb in assembly it looks like 
![[Pasted image 20250413002918.png]]

after searching it is like a strcmp function and i use ida to decompile found is it a strcmp function thr 
![[Pasted image 20250413003149.png]]

8. so in order for us to not getting the false flag we must make sure they are not equal , but when i ni i found i being escape from the program thus i decide to let rdi and rdi have same value to finish the operation of repz then i modify the value during test al ,al 
```bash
set $rsi = $rdi 
```
then we continue until test al ,al 

9. so now actually i do some research test al ,al is performing a and operation it sets ZF (zero flag) to zero if al is 0 then je (jump equal ) is same funciton as jz will jump to the function .
10. now we at test al,al and look above we dun want let al = 0 since it will bring us to false flag thus we must change it .
![[Pasted image 20250413003951.png]]

11. after set it just ni until strcmp func 
```bash
set $al = 1
```

12. why the strcmp thr will have flag refer here 
![[Pasted image 20250413004359.png]]

thr is v6 in strcmp and it exist as the congrats flag thr thus v6 is our flag . 

13. ![[Pasted image 20250413004506.png]]

14. CTFlearn{Eye_L0ve_Iceland_}"