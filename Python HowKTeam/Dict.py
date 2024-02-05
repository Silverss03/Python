a={'codename':'Silverss','bday':108}
a={key:value for key,value in [('codename','Silverss'),('bday',108)]}
a={}
a=dict([('codename','Silverss'),('bday',108)])
codename='Soap'
bday= '?/?/?'
a=dict([('codename','Silverss'),('bday',108)])
a=('codename','bday','Silverss')
a=dict.fromkeys(a,'K')
a ['codename']= 'Soap MacTavish'
a['codename']= a['codename'] + ' Liteunant'
a['Status'] = 'KIA'
a1=a.copy()
#a.clear()
a1=a.get(r'codename','default') #Không có key thì ra none,nếu có default thì ra default
a1=dict(a.items())
#a1=a.keys()
#a1=a.values()
a1=a.pop('codename','default') #Không có thì sẽ lấy ra default
#a1.a.popitem() pop ngẫu nhiên,nếu dict rỗng thì lỗi
#a1=a.setdefault('Status','default')
#a1=a.update(a=1,b=2)
print(a)
print(a1)
