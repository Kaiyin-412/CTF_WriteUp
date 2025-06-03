1.Ermm i solve it at 2:29 , did not manage to submit it on time (submission closed at 2:30).

2.first throw it into ida and check for the string . 
![[Pasted image 20250512021601.png]]

3.the flag found is important let us have a look . 

![[Pasted image 20250512021717.png]]

4.so basically we need to have a input of 16 and pass the luhn check and it reveal the first part then we need to pass the check second part to get the full content of flag . 

5.so after i check the luhnCheck function basically just check for luhn number and i prompt gpt to give me a 16 digit luhn number and we try enter it . 
![[Pasted image 20250512022017.png]]

6.ok we get the first part let us proceed to second part . 

![[Pasted image 20250512022111.png]]

actually is just use our input and do some encryption then then stored in Buf1 

then it compare with data in encryptedSecondPart , So we just need to use encryptedSecondPart to reverse back and found the input we need to enter . 

7.at first i try script it but always got prob then i throw it to gpt then  i solve it .

```python
encrypted = [0xBF, 0xEB, 0xA3, 0xAF, 0x97, 0xA7, 0x9F, 0xEF]

def reverse_byte(b):
    for val in range(100):
        v = val ^ 0xAA
        if ((v << 2) | (v >> 6)) & 0xFF == b:
            return f"{val:02d}"  # Pad to 2 digits
    return "??"

result = ''.join(reverse_byte(b) for b in encrypted)
print("Recovered digits:", result)
```



![[Pasted image 20250512023257.png]]

Reflection 
need to add 0xFF since in the program is using only 8 bits so to match it we need to & 0xFF before compare . 