f=open("dimene.xml","w+")
f.writelines('<?xml version="1.0" encoding="utf-8"?>\n')
f.writelines('<resources>\n')
for x in range(0,301):
    f.writelines('<dimen name="_'+str(x)+'dp">'+str(x)+'dp</dimen>\n')
for x in range(0,300):
    f.writelines('<dimen name="_'+str(x)+'sp">'+str(x)+'sp</dimen>\n')
f.writelines('</resources>\n')
f.close()