str = open('INI6')

def dict_find(str):
 dict_s={}
 for word in str.split(' '):
 if word in dict_s:
 dict_s[word]=dict_s[word]+1
 else:
 dict_s[word]=1
 for key, value in dict_s.items():
 print key + ' ' + repr(value)