s = 'Nishant Nitin Musmade     hello    hiii '
# i = len(s)-1
# last_word = ''
# while s[i]!= ' ':
#     last_word=last_word+s[i]
#     i=i-1

# print(len(last_word))

import time
tic = time.time()
print(tic)
s = s.strip()
# toc = time.time()
# print(toc)
# print((toc-tic)*1000)
# tic = time.time()
i = len(s)-1
last_word = ''
while s[i]!=' ' and i>=0:
    last_word=last_word+s[i]
    i=i-1

print(len(last_word))
toc = time.time()
print((toc-tic)*1000)