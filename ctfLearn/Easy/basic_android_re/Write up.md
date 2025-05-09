1. use apktool to decode the apk file
```bash
apktool d 962
```

2. next we use jadx-gui to open the decompile file 
```bash
jadx-gui
```

3. next we naviagte to the main activity 
![[Pasted image 20250412234943.png]]

4. ![[Pasted image 20250412235006.png]]

5. so we just need to brute force the md5 hash 
![[Pasted image 20250412235037.png]]

6. CTFlearn{Spring2019_is_not_secure!}