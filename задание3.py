a=open('students.csv',encoding='utf-8').readlines()
a.pop(0)
for i in range(len(a)):
    a[i]=a[i].strip().split(',')
    a[i][2]=int(a[i][2])
while True:
    id=input()
    if id=='СТОП':
        break
    id=int(id)
    flag=0
    for x in a:
        if x[2]==id:
            f, i, o = x[1].split()
            name = f'{i[0]}. {f}'
            print(f'Проект № {x[2]} делал: {name} он(а) получил(а) оценку - {x[-1]}')
            flag=1
            break
    if flag==0:
        print('Ничего не найдено')