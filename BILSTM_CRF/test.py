#f=open('data_path/test_data', 'r',encoding = 'gb18030')
#data = f.readline().strip().split('\t')[0]
#print(len(data),data.encode('gb18030').decode('latin1'))
#a = input()
with open('data','r',encoding='gb18030') as f:
    d=f.readline().strip()
    print (len(list(d)))
#print (len(a))
