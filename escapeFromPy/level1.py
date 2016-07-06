#!/usr/bin/env python
 
# config with socat
# Use socat to run as a listening service
# socat TCP-LISTEN:1337,fork EXEC:./level1.py,pty,stderr
 
def securized():
        UNSAFE = ['open',
         'file',
         'execfile',
         'compile',
         'reload',
         '__import__',
         'eval',
         'input']
        for func in UNSAFE:
          del __builtins__.__dict__[func]
 
 
from re import search
securized()
print 'Can you read the key.txt?'
while True:
    try:
      x = search('\S+', raw_input()).group(0)
      if "key.txt" in x:
       print "Hey ! this is fun, you have to read a key.txt but i avoid this string, padawan :-)"
       exit()
      if "sudo" in x:
       print "Good try, but too dangerous !"
       exit()
      if "sh" in x:
       print "Good try, but not allowed :-)"
       exit()
      print "x=", x
      a = None
      exec 'x=' + x
      print 'you got:', a
    except Exception, e:
      print 'Exception: ', e
