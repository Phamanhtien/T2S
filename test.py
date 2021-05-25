
'''
import pickle


a = ['a','b','c']
c = [1,2,3,4]


kaka = open('haha.txt','wb')
pickle.dump(a,kaka)
pickle.dump(c,kaka)

kaka = open('haha.txt','rb')
a = pickle.load(kaka)
print(a) 
'''

import struct

a = ['a','b','c']
c = [1,2,3,4]

data = struct.pack('list',a)