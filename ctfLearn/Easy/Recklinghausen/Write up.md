1. use ida to diassemble it

2. then we get to here , the argv[1] will be the argument we passed it into so we change it to input as the variable name to make it more readable . 
![[Pasted image 20250420022555.png]]

3. actually the main point is CheckMsg , because our input is pass into lets check it . 
4. 
![[Pasted image 20250420022743.png]]
- a1 is our input 
- then v1 will storing the length 
- msg5 is storing 21 means our input is 21 length 
- then we move on to here
![[Pasted image 20250420023011.png]]

- basically the code is doing a comparison 
- first we must what is byte_50E2 and byte_50E1 
![[Screenshot 2025-04-20 023407.png]]
![[Pasted image 20250420023457.png]]

- if they are equal the v3 will inc and it will check for the second character in our input , from here we can get by our input . 
- a1[v3] = byte_50E2[v3] ^ byte_50E1 

5. this is simple python script to solve it 
```python
v1 = [0x3d , 0x2a , 0x38,0x12 , 0x1b , 0x1f , 0x0c, 0x10,0x5 , 0x2c , 0x0b , 0x16 , 0x0c, 0x18 , 0x1B , 0x0d , 0x0a , 0x0d, 0x0e, 0x17,0x1b , 0x12,0x1b ,0x21 , 0x38 , 0x1b , 0x0d, 0x0a , 0x17,0x8 , 0x1f ,
      0x12 , 0x3]

v2 = 0x7e

for i in range (0,len(v1)) :
    print(chr(v1[i] ^ v2),end='')
```

6. CTFlearn{Ruhrfestspiele_Festival}

