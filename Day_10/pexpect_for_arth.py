import pexpect
import sys
m = pexpect.spawn('python arth.py')
m.logfile_read = sys.stdout
m.expect("enter the first value ")
m.sendline('5')
m.expect("enter the second value ")
m.sendline('6')
m.expect("enter the character ")
m.sendline('+')
m.expect('\n')
m.close()
