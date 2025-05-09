1. first we use online scan qr code to scan the qr png
2. then we will get 
```
f0VMRgEBAQAAAAAAAAAAAAIAAwABAAAAgIAECDQAAACMAgAAAAAAADQAIAACACgABgAFAAEAAAAAAAAAAIAECACABAjFAAAAxQAAAAUAAAAAEAAAAQAAAMgAAADIkAQIyJAECFcAAABXAAAABgAAAAAQAAAAAAAAAAAAAAAAAAC6CgAAALkUkQQIuwEAAAC4BAAAAM2AMcA8B3Qdi5DkkAQIQOkAAAAAVYnlUIDyF4hVAFhd6d////+7AAAAALgBAAAAzYAAAAA5w6nhu7PDvHtqbj09fSAgPFw6ICBfXyAgUDAARkVIYSQnagBRw7NBOGTDunAwbTk5cse5MDQwVjA1ZmYxTGxrOVwwb09cQy9cMDAAQ1RGbGVhcm57CgAAAAAAAAAAAAAAAAAAAAAAAAAAAACAgAQIAAAAAAMAAQAAAAAAyJAECAAAAAADAAIAAQAAAAAAAAAAAAAABADx/wgAAADIkAQIAAAAAAAAAgAPAAAA5JAECAAAAAAAAAIAFQAAAOyQBAgAAAAAAAACAB0AAAAUkQQIAAAAAAAAAgAjAAAAmIAECAAAAAAAAAEAKAAAAKiABAgAAAAAAAABADUAAAC5gAQIAAAAAAAAAQA/AAAAgIAECAAAAAAQAAEAOgAAAB+RBAgAAAAAEAACAEYAAAAfkQQIAAAAABAAAgBNAAAAIJEECAAAAAAQAAIAAHFyLmFzbQByYW5kb20AZWZsYWcAcmFuZG9tMgBzZmxhZwBsb29wAGJpdGVfb2ZfZmxhZwBkb25lAF9fYnNzX3N0YXJ0AF9lZGF0YQBfZW5kAAAuc3ltdGFiAC5zdHJ0YWIALnNoc3RydGFiAC50ZXh0AC5kYXRhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAbAAAAAQAAAAYAAACAgAQIgAAAAEUAAAAAAAAAAAAAABAAAAAAAAAAIQAAAAEAAAADAAAAyJAECMgAAABXAAAAAAAAAAAAAAAEAAAAAAAAAAEAAAACAAAAAAAAAAAAAAAgAQAA8AAAAAQAAAALAAAABAAAABAAAAAJAAAAAwAAAAAAAAAAAAAAEAIAAFIAAAAAAAAAAAAAAAEAAAAAAAAAEQAAAAMAAAAAAAAAAAAAAGICAAAnAAAAAAAAAAAAAAABAAAAAAAAAA==
```
3. its look like a base64 string lets try decode it 
```
ELF��������������4���������4� ��(������������������������������W���W���������������������
���������1<t@����UPU�X]����������9{jn==}  <\:  __  P0�FEHa$'j�QA8dp0m99r040V05ff1Llk9\0oO\C/\00�CTFlearn{
������������������������������������������������������������������������������������������#����������(����������5����������?���������:���������F���������M��� �������qr.asm�random�eflag�random2�sflag�loop�bite_of_flag�done�__bss_start�_edata�_end��.symtab�.strtab�.shstrtab�.text�.data��������������������������������������������������������E������������������!������������W�������������������������������� �����������������	����������������R��������������������������������b��'������������������
```

4. its like elf file so at first i have no clue , but after i found we can put it into a file and make it executable
```bash
echo "f0VMRgEBAQAAAAAAAAAAAAIAAwABAAAAgIAECDQAAACMAgAAAAAAADQAIAACACgABgAFAAEAAAAAAAAAAIAECACABAjFAAAAxQAAAAUAAAAAEAAAAQAAAMgAAADIkAQIyJAECFcAAABXAAAABgAAAAAQAAAAAAAAAAAAAAAAAAC6CgAAALkUkQQIuwEAAAC4BAAAAM2AMcA8B3Qdi5DkkAQIQOkAAAAAVYnlUIDyF4hVAFhd6d////+7AAAAALgBAAAAzYAAAAA5w6nhu7PDvHtqbj09fSAgPFw6ICBfXyAgUDAARkVIYSQnagBRw7NBOGTDunAwbTk5cse5MDQwVjA1ZmYxTGxrOVwwb09cQy9cMDAAQ1RGbGVhcm57CgAAAAAAAAAAAAAAAAAAAAAAAAAAAACAgAQIAAAAAAMAAQAAAAAAyJAECAAAAAADAAIAAQAAAAAAAAAAAAAABADx/wgAAADIkAQIAAAAAAAAAgAPAAAA5JAECAAAAAAAAAIAFQAAAOyQBAgAAAAAAAACAB0AAAAUkQQIAAAAAAAAAgAjAAAAmIAECAAAAAAAAAEAKAAAAKiABAgAAAAAAAABADUAAAC5gAQIAAAAAAAAAQA/AAAAgIAECAAAAAAQAAEAOgAAAB+RBAgAAAAAEAACAEYAAAAfkQQIAAAAABAAAgBNAAAAIJEECAAAAAAQAAIAAHFyLmFzbQByYW5kb20AZWZsYWcAcmFuZG9tMgBzZmxhZwBsb29wAGJpdGVfb2ZfZmxhZwBkb25lAF9fYnNzX3N0YXJ0AF9lZGF0YQBfZW5kAAAuc3ltdGFiAC5zdHJ0YWIALnNoc3RydGFiAC50ZXh0AC5kYXRhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAbAAAAAQAAAAYAAACAgAQIgAAAAEUAAAAAAAAAAAAAABAAAAAAAAAAIQAAAAEAAAADAAAAyJAECMgAAABXAAAAAAAAAAAAAAAEAAAAAAAAAAEAAAACAAAAAAAAAAAAAAAgAQAA8AAAAAQAAAALAAAABAAAABAAAAAJAAAAAwAAAAAAAAAAAAAAEAIAAFIAAAAAAAAAAAAAAAEAAAAAAAAAEQAAAAMAAAAAAAAAAAAAAGICAAAnAAAAAAAAAAAAAAABAAAAAAAAAA==" > qr.txt
```

```bash
cat qr.txt | base64 -d > qr
chmod +x qr
```

5. next we open ida to analysis it 
![[Pasted image 20250414230700.png]]

its look like encrypr or decrypt function but nvm its look like we need to get the value of a1 . 

6. lets try have a look on assembly on ida 
![[Pasted image 20250414230956.png]]

(hightlight with green wan) its look like we need to reach here and check the value store in ebp 

7. let start gdb  and set a breakpoint at the function
```gdb
b * _start
```

8. ni until here 
![[Pasted image 20250414231223.png]]
the value stored in rbp is Q 
u can also use this command to check the string store 
```gdb 
x/s $ebp
```

9. then we continue the same step until obtain all the value 
10. CTFlearn{QR_v303}