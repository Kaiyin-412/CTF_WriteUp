1. use ida disassemble it
![[Pasted image 20250420015019.png]]

2. check the beerEmbassy function
![[Pasted image 20250420015053.png]]

it is initialised as 1 

3. thus we willl comming to HerbalTea0 let check it 
4. this is the first part looks messay but is useless
![[Pasted image 20250420015218.png]]

5. let check the another part 
![[Pasted image 20250420015251.png]]

ya we found smtg important seems s is my input and it pass in v6 . 
ok at first i try second condition but i found some unprintable chr thus for the unprinted i just change it to using the first condition . 

6. the script 
```python
v1 = [0x9f , 0x0Ae , 0x9c , 0xB6 , 0x0Bd , 0x0B9, 0x0Ef, 0x0Eb, 0x0E6 , 0x9e, 0x0B9, 0x0ec, 0x0b3, 0x0B9, 0x0E3, 0x0b9, 0x0bb, 0x0a8 , 0x089, 0x0e3, 0x0bd, 0x0Ef, 0x0Bb, 0x96, 0x0b9, 0xed , 0xe3 , 0x89 , 0xb9 , 0xe4 ]

print(len(v1))

for i in range (0,len(v1)):
    temp = 0xcb ^ v1[i]
    cur = temp -17
    if (cur >=33 and cur <=126):
        print(chr(cur),end='')
    else:
        temp = (v1[i] ^ 0xcb)+78
        print(chr(temp),end='')
```