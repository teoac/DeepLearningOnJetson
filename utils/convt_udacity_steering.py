import csv
import shutil

csv_open = open('final_example.csv', 'r')
csv_reader = csv.reader(csv_open)
header = next(csv_reader) # header 읽고 다음행으로 이동
for row in csv_reader:
    fNo = row[0]
    sAng = float(row[1])
    print('Frame No:', fNo, 'Steering Angle:', sAng)
    tmp = sAng*10
    tmp2 = round(tmp)
    if tmp2 == -4:
        tmp3 = 'Copy '+fNo+'.jpg to /m04'
        print(tmp3)
        shutil.copy('./center/'+fNo+'.jpg', 'm04')
    elif tmp2 == -3:
        tmp3 = 'Copy '+fNo+'.jpg to /m03'
        print(tmp3)
        shutil.copy('./center/'+fNo+'.jpg', 'm03')
    elif tmp2 == -2:
        tmp3 = 'Copy '+fNo+'.jpg to /m02'
        print(tmp3)
        shutil.copy('./center/'+fNo+'.jpg', 'm02')
    elif tmp2 == -1:
        tmp3 = 'Copy '+fNo+'.jpg to /m01'
        print(tmp3)
        shutil.copy('./center/'+fNo+'.jpg', 'm01')
    elif tmp2 == 1:
        tmp3 = 'Copy '+fNo+'.jpg to /p01'
        print(tmp3)
        shutil.copy('./center/'+fNo+'.jpg', 'p01')
    elif tmp2 == 2:
        tmp3 = 'Copy '+fNo+'.jpg to /p02'
        print(tmp3)
        shutil.copy('./center/'+fNo+'.jpg', 'p02')
    elif tmp2 == 3:
        tmp3 = 'Copy '+fNo+'.jpg to /p03'
        print(tmp3)
        shutil.copy('./center/'+fNo+'.jpg', 'p03')
    elif tmp2 == 4:
        tmp3 = 'Copy '+fNo+'.jpg to /p04'
        print(tmp3)
        shutil.copy('./center/'+fNo+'.jpg', 'p04')
    else:
        tmp3 = 'Copy '+fNo+'.jpg to /000'
        print(tmp3)
        shutil.copy('./center/'+fNo+'.jpg', '000')

print('Sorting is finished. The /center including all files are moved to other directories.')
shutil.move('center', '../driving_original/center')
shutil.move('final_example.csv', '../driviing_original/final_example.csv')
csv_open.close()
