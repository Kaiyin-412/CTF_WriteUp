1. open ida and disassemble it 
2. this is the main point 
![[Pasted image 20250418003149.png]]

3. let check what is kernelenc lets click inside 
![[Pasted image 20250418003305.png]]
is like storing an array of string

4. so basically it will pass in the input and do some calcualtion and check whether the input equal to kernelenc value .
5. so we just bruteforce it 

```python
v1 = "W8Hj?1VESL^g4xwcvtW%humtEosd$Fq^dXPvi$#sSEe@o618Zl9.5PFrvC%O_E*LB%Igl8qur9SuLAp4MkK#pRzwJHI*Fn9mUs%mGK^RQKO.G*JFJvV%?VJpCpVF9eJuz5&kB!&_VF5DrF?U?jfm&x^9aC7X2(&cGGzbLbOsSOuBeq*ZT%fpc&9riTDO5X%RuTKI@vCqu#CsTAp$Q9WoXJv96.ySdB2EfMK*$NX?.U*aDrfPQQPhFB9cC6y0hMGvbgjBogSux65gTL#Cm9TQt7nTayu9Vr%thh2GnnikE8JnIwlHfreZep^sZ6IrnXT#qu50Lv.Rd_XPDfgwzWcJ3ISjKM!ftRllVyF$?RE_dcJT5&uKZJ!WsqR853uLzcs!8&VyRuTDsiq#6PdmBNlPI$tPi?wZ5$ACCf9yda!OkP.Dc73Nx.Nt1Rj0O.?P!sZDB^d0LN1qXR31!t?OZ#mm7SfZHPO*4gx1J0nyC^d2EKeq^f4h7mSqaIcMv0ZT@G0M"

temp = 0

for i in range (0,11) :
    for k in range (20,128):
        temp = k

        if (i == 0 ):
            current = (3131961357 % ( k * k * k + k * k)) & 511
            if (chr(k) == v1[current]):
                print(chr(temp),end ='')
                break
        else :
            current = ((3131961357+(3*i)) % (k * k + k * k * k + (3*i)) & 511)
            if (chr(k) == v1[current]):
                print(chr(temp),end='')
                break
```

6. we will get this K0nstancja_ , wrap it with CTFlearn{}
7. CTFlearn{K0nstancja_}