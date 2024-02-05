try:
    with open('Bai1.12.inp','r') as file:
        a=file.read().splitlines()
        result=' '.join(a).split()
        final=' '.join(result)
    with open('Bai1.12.out','w') as newfile:
        newfile.write('{}'.format(result))
except:
        with open('Bai1.12.out','w',encoding='utf-8') as newfile:
            newfile.write('File không tồn tại!')