# ReverseIP
Littlebit Library for Reverse IP

### How to Use?
<b>1.</b> Clone this repository using git:

```
git clone https://github.com/EtcAug10/ReverseIP
```

<b>2.</b> Then make new file with *PY* extension for make python program. In this case, i make exmpl.py, Then code first as importing the library functions.

```python
#exmpl.py
#!/usr/bin/env python3

# if exmpl.py is out of the ReverseIP directory, then include the folder name
import ReverseIP.reverseip

#if exmpl.py is in the same directory, then just import the filename
import reverseip
```

<b>3.</b> Finally, code yourself every things you want by choosing the functions. Example:
```python
import reverseip

#Using OsintSH.
rev = reverseip.OsintSH()
ip = "127.0.0.1"
rev.get_data(ip)
print(rev.dump())
```
