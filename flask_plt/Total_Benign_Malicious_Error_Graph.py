from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from io import BytesIO
import matplotlib.pyplot as plt
import csv
root = Tk()
root.title('file select')
 
def instart():
    global my_image # 함수에서 이미지를 기억하도록 전역변수 선언 (안하면 사진이 안보임)
    root.filename = filedialog.askopenfilename(initialdir='C:\\Users\\82105\\Desktop\\pyCSV\\csv', title='파일선택', filetypes=(
    ('csv files', '*.csv'), ('all files', '*.*')))
 
    Label(root, text=root.filename).pack() # 파일경로 view
    print("경로: "+root.filename)

    
    f=open(root.filename,encoding='utf-8')
    data=csv.reader(f)

    result=[]
    result2=[]
    cnt00b=0
    cnt00m=0
    cnt00s=0
    cnt00e=0

    cnt23b=0
    cnt23m=0
    cnt23s=0
    cnt23e=0

    cnt22b=0
    cnt22m=0
    cnt22s=0
    cnt22e=0

    cnt21b=0
    cnt21m=0
    cnt21s=0
    cnt21e=0

    cnt20b=0
    cnt20m=0
    cnt20s=0
    cnt20e=0

    cnt19b=0
    cnt19m=0
    cnt19s=0
    cnt19e=0

    cnt18b=0
    cnt18m=0
    cnt18s=0
    cnt18e=0

    cnt17b=0
    cnt17m=0
    cnt17s=0
    cnt17e=0

    cnt16b=0
    cnt16m=0
    cnt16s=0
    cnt16e=0

    cnt15b=0
    cnt15m=0
    cnt15s=0
    cnt15e=0

    cnt14b=0
    cnt14m=0
    cnt14s=0
    cnt14e=0

    cnt13b=0
    cnt13m=0
    cnt13s=0
    cnt13e=0

    cnt12b=0
    cnt12m=0
    cnt12s=0
    cnt12e=0

    cnt11b=0
    cnt11m=0
    cnt11s=0
    cnt11e=0

    cnt10b=0
    cnt10m=0
    cnt10s=0
    cnt10e=0

    cnt09b=0
    cnt09m=0
    cnt09s=0
    cnt09e=0

    cnt08b=0
    cnt08m=0
    cnt08s=0
    cnt08e=0

    cnt07b=0
    cnt07m=0
    cnt07s=0
    cnt07e=0

    cnt06b=0
    cnt06m=0
    cnt06s=0
    cnt06e=0

    cnt05b=0
    cnt05m=0
    cnt05s=0
    cnt05e=0

    cnt04b=0
    cnt04m=0
    cnt04s=0
    cnt04e=0

    cnt03b=0
    cnt03m=0
    cnt03s=0
    cnt03e=0

    cnt02b=0
    cnt02m=0
    cnt02s=0
    cnt02e=0

    cnt01b=0
    cnt01m=0
    cnt01s=0
    cnt01e=0
    for row in data:
        if row[0]!='':
            my_str=row[0]
            result2=row[2]
            result=my_str[11:13] #시간 별로 나누기위해 시간들만 추출
            result_count=result2[0]
            
            
    #         print('시간 : '+result+' | Diagnosis : '+result2)   #시간 다수 출력
            
            if result == "23" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt23b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt23m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt23s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt23e+=1
            if result == "00" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt00b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt00m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt00s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt00e+=1
            if result == "22" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt22b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt22m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt22s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt22e+=1
            if result == "21" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt21b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt21m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt21s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt21e+=1
            if result == "20" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt20b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt20m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt20s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt20e+=1
            if result == "19" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt19b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt19m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt19s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt19e+=1
            if result == "18" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt18b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt18m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt18s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt18e+=1
            if result == "17" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt17b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt17m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt17s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt17e+=1
            if result == "16" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt16b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt16m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt16s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt16e+=1    
            if result == "15" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt15b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt15m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt15s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt15e+=1
            if result == "14" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt14b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt14m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt14s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt14e+=1
            if result == "13" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt13b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt13m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt13s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt13e+=1
            if result == "12" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt12b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt12m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt12s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt12e+=1
            if result == "11" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt11b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt11m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt11s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt11e+=1
            if result == "10" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt10b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt10m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt10s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt10e+=1   
            if result == "09" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt09b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt09m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt09s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt09e+=1
            if result == "08" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt08b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt08m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt08s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt08e+=1
            if result == "07" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt07b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt07m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt07s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt07e+=1
            if result == "06" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt06b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt06m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt06s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt06e+=1    
            if result == "05" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt05b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt05m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt05s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt05e+=1
            if result == "04" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt04b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt04m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt04s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt04e+=1
            if result == "03" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt03b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt03m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt03s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt03e+=1
            if result == "02" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt02b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt02m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt02s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt02e+=1
            if result == "01" :
                if result2 =="BENIGN":
                    for row in result_count:
                        cnt01b+=1
                if result2 == "MALICIOUS":
                    for row in result_count:
                        cnt01m+=1
                if result2 == "SUSPICIOUS":
                    for row in result_count:
                        cnt01s+=1
                if result2 == "ERROR ":
                    for row in result_count:
                        cnt01e+=1

    totalcnt00=cnt00b+cnt00m+cnt00s+cnt00e #합계의 개수

    totalcnt23=cnt23b+cnt23m+cnt23s+cnt23e

        
    totalcnt22=cnt22b+cnt22m+cnt22s+cnt22e


    totalcnt21=cnt21b+cnt21m+cnt21s+cnt21e


    totalcnt20=cnt20b+cnt20m+cnt20s+cnt20e


    totalcnt19=cnt19b+cnt19m+cnt19s+cnt19e


    totalcnt18=cnt18b+cnt18m+cnt18s+cnt18e


    totalcnt17=cnt17b+cnt17m+cnt17s+cnt17e


    totalcnt16=cnt16b+cnt16m+cnt16s+cnt16e


    totalcnt15=cnt15b+cnt15m+cnt15s+cnt15e


    totalcnt14=cnt14b+cnt14m+cnt14s+cnt14e


    totalcnt13=cnt13b+cnt13m+cnt13s+cnt13e


    totalcnt12=cnt12b+cnt12m+cnt12s+cnt12e


    totalcnt11=cnt11b+cnt11m+cnt11s+cnt11e


    totalcnt10=cnt10b+cnt10m+cnt10s+cnt10e


    totalcnt09=cnt09b+cnt09m+cnt09s+cnt09e


    totalcnt08=cnt08b+cnt08m+cnt08s+cnt08e


    totalcnt07=cnt07b+cnt07m+cnt07s+cnt07e


    totalcnt06=cnt06b+cnt06m+cnt06s+cnt06e
                    
    totalcnt05=cnt05b+cnt05m+cnt05s+cnt05e


    totalcnt04=cnt04b+cnt04m+cnt04s+cnt04e


    totalcnt03=cnt03b+cnt03m+cnt03s+cnt03e


    totalcnt02=cnt02b+cnt02m+cnt02s+cnt02e


    totalcnt01=cnt01b+cnt01m+cnt01s+cnt01e


    f.close()
    benign=[cnt00b,cnt01b,cnt02b,cnt03b,cnt04b,cnt05b,cnt06b,cnt07b,cnt08b,cnt09b,
            cnt10b,cnt11b,cnt12b,cnt13b,cnt14b,cnt15b,cnt16b,cnt17b,cnt18b,cnt19b,
            cnt20b,cnt21b,cnt22b,cnt23b]
    malicious=[cnt00m,cnt01m,cnt02m,cnt03m,cnt04m,cnt05m,cnt06m,cnt07m,cnt08m,cnt09m,
            cnt10m,cnt11m,cnt12m,cnt13m,cnt14m,cnt15m,cnt16m,cnt17m,cnt18m,cnt19m,
            cnt20m,cnt21m,cnt22m,cnt23m]
    suspicious=[cnt00s,cnt01s,cnt02s,cnt03s,cnt04s,cnt05s,cnt06s,cnt07s,cnt08s,cnt09s
                ,cnt10s,cnt11s,cnt12s,cnt13s,cnt14s,cnt15s,cnt16s,cnt17s,cnt18s,cnt19s,
                cnt20s,cnt21s,cnt22s,cnt23s]

    error=[cnt00e,cnt01e,cnt02e,cnt03e,cnt04e,cnt05e,cnt06e,cnt07e,cnt08e,cnt09e,
        cnt10e,cnt11e,cnt12e,cnt13e,cnt14e,cnt15e,cnt16e,cnt17e,cnt18e,cnt19e
        ,cnt20e,cnt21e,cnt22e,cnt23e]
    total=[totalcnt00,totalcnt01,totalcnt02,totalcnt03,totalcnt04,
        totalcnt05,totalcnt06,totalcnt07,totalcnt08,totalcnt09,
        totalcnt10,totalcnt11,totalcnt12,totalcnt13,totalcnt14,
        totalcnt15,totalcnt16,totalcnt17,totalcnt18,totalcnt19,
        totalcnt20,totalcnt21,totalcnt22,totalcnt23]

    time=['00','01','02','03','04','05','06','07','08','09',
        '10','11','12','13','14','15','16','17','18','19',
        '20','21','22','23']

    benignx=[1,6,11,16,21,26,31,36,41,46,51,56,61,66,71,76,81,86,91,96,101,106,111,116]
    maliciousx=[2,7,12,17,22,27,32,37,42,47,52,57,62,67,72,77,82,87,92,97,102,107,112,117]
    suspiciousx=[3,8,13,18,23,28,33,38,43,48,53,58,63,68,73,78,83,88,93,98,103,108,113,118]
    errorx=[4,9,14,19,24,29,34,39,44,49,54,59,64,69,74,79,84,89,94,99,104,109,114,119]
    totalx=[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120]

    fig = plt.figure(figsize=(10,10)) ## 캔버스 생성
    fig.set_facecolor('white') ## 배경색 설정
    ticklabel=['00','01','02','03','04','05','06','07','08','09',
            '10','11','12','13','14','15','16','17','18','19',
            '20','21','22','23']
    plt.bar(benignx,benign,color='skyblue',width=1,label="BENIGN")
    plt.bar(maliciousx,malicious,color='g',width=1,label="MALICIOUS")
    plt.bar(suspiciousx,suspicious,color='y',width=1,label="SUSPICIOUS")
    plt.bar(errorx,error,color='red',width=1,label="ERROR")
    plt.bar(totalx,total,color='black',width=1,label="TOTAL")
    plt.xlabel('Time')
    plt.ylabel('Data')
    plt.legend(loc=0)
    plt.xticks(benignx,ticklabel,fontsize=10,rotation=0)

    plt.show()
    img = BytesIO()
    plt.savefig(img, format='png', dpi=200)
    img.seek(0)

    # my_image = ImageTk.PhotoImage(Image.open(root.filename)) ## 밑에 사진 뜨는거
    Label(img).pack() #사진 view
 
 
my_btn = Button(root, text='파일열기', command=instart).pack()
 
root.mainloop()