import pexpect
m_p = pexpect.spawn('python smtp.py')
m_p.timeout=60
m_p.expect('gmail')
m_p.sendline('nirmalrajkumar1991@gmail.com')
m_p.expect('Password:')
m_p.sendline('')
m_p.expect('to:')
m_p.sendline('anuj.285aj@gmail.com')
m_p.expect('subject:')
m_p.sendline('hello')
m_p.close()

