from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from io import BytesIO
import matplotlib.pyplot as plt
import csv

root = Tk()

root.title('file select')
label1 = Label(root,text = "CSV파일을 넣어주세요.")
label2 = Label(root,text = "시간 당 [Total / DOC(X) / XLS(X) / PPT(X) / HWP(X) / PDF / HTML] 개수")
label1.pack()
label2.pack()
def instart():
    global my_image # 함수에서 이미지를 기억하도록 전역변수 선언 (안하면 사진이 안보임)
    
    
    root.filename = filedialog.askopenfilename(initialdir='', title='파일선택',filetypes=(
    ('csv files', '*.csv'), ('all files', '*.*')))
 
    Label(root, text=root.filename).pack() # 파일경로 view
    print("경로: "+root.filename)

    
    f=open(root.filename,encoding='utf-8')
    data=csv.reader(f)

    result=[]
    result2=[]
    cnt00doc=0
    cnt00xls=0
    cnt00ppt=0
    cnt00hwp=0
    cnt00pdf=0
    cnt00html=0

    cnt23doc=0
    cnt23xls=0
    cnt23ppt=0
    cnt23hwp=0
    cnt23pdf=0
    cnt23html=0

    cnt22doc=0
    cnt22xls=0
    cnt22ppt=0
    cnt22hwp=0
    cnt22pdf=0
    cnt22html=0

    cnt21doc=0
    cnt21xls=0
    cnt21ppt=0
    cnt21hwp=0
    cnt21pdf=0
    cnt21html=0

    cnt20doc=0
    cnt20xls=0
    cnt20ppt=0
    cnt20hwp=0
    cnt20pdf=0
    cnt20html=0

    cnt19doc=0
    cnt19xls=0
    cnt19ppt=0
    cnt19hwp=0
    cnt19pdf=0
    cnt19html=0

    cnt18doc=0
    cnt18xls=0
    cnt18ppt=0
    cnt18hwp=0
    cnt18pdf=0
    cnt18html=0

    cnt17doc=0
    cnt17xls=0
    cnt17ppt=0
    cnt17hwp=0
    cnt17pdf=0
    cnt17html=0

    cnt16doc=0
    cnt16xls=0
    cnt16ppt=0
    cnt16hwp=0
    cnt16pdf=0
    cnt16html=0

    cnt15doc=0
    cnt15xls=0
    cnt15ppt=0
    cnt15hwp=0
    cnt15pdf=0
    cnt15html=0

    cnt14doc=0
    cnt14xls=0
    cnt14ppt=0
    cnt14hwp=0
    cnt14pdf=0
    cnt14html=0

    cnt13doc=0
    cnt13xls=0
    cnt13ppt=0
    cnt13hwp=0
    cnt13pdf=0
    cnt13html=0

    cnt12doc=0
    cnt12xls=0
    cnt12ppt=0
    cnt12hwp=0
    cnt12pdf=0
    cnt12html=0

    cnt11doc=0
    cnt11xls=0
    cnt11ppt=0
    cnt11hwp=0
    cnt11pdf=0
    cnt11html=0

    cnt10doc=0
    cnt10xls=0
    cnt10ppt=0
    cnt10hwp=0
    cnt10pdf=0
    cnt10html=0

    cnt09doc=0
    cnt09xls=0
    cnt09ppt=0
    cnt09hwp=0
    cnt09pdf=0
    cnt09html=0

    cnt08doc=0
    cnt08xls=0
    cnt08ppt=0
    cnt08hwp=0
    cnt08pdf=0
    cnt08html=0

    cnt07doc=0
    cnt07xls=0
    cnt07ppt=0
    cnt07hwp=0
    cnt07pdf=0
    cnt07html=0

    cnt06doc=0
    cnt06xls=0
    cnt06ppt=0
    cnt06hwp=0
    cnt06pdf=0
    cnt06html=0

    cnt05doc=0
    cnt05xls=0
    cnt05ppt=0
    cnt05hwp=0
    cnt05pdf=0
    cnt05html=0

    cnt04doc=0
    cnt04xls=0
    cnt04ppt=0
    cnt04hwp=0
    cnt04pdf=0
    cnt04html=0

    cnt03doc=0
    cnt03xls=0
    cnt03ppt=0
    cnt03hwp=0
    cnt03pdf=0
    cnt03html=0

    cnt02doc=0
    cnt02xls=0
    cnt02ppt=0
    cnt02hwp=0
    cnt02pdf=0
    cnt02html=0

    cnt01doc=0
    cnt01xls=0
    cnt01ppt=0
    cnt01hwp=0
    cnt01pdf=0
    cnt01html=0
    for row in data:
        if row[0]!='':
            my_str=row[0]
            result2=row[4]
            result=my_str[11:13] #시간 별로 나누기위해 시간들만 추출
            result_count=result2[0]
            
            
    #         print('시간 : '+result+' | Diagnosis : '+result2)   #시간 다수 출력
            
            if result == "23" :
                if result2 =="doc":
                    for row in result_count:
                        cnt23doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt23xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt23ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt23hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt23pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt23html+=1        
            if result == "00" :
                if result2 =="doc":
                    for row in result_count:
                        cnt00doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt00xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt00ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt00hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt00pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt00html+=1
            if result == "22" :
                if result2 =="doc":
                    for row in result_count:
                        cnt22doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt22xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt22ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt22hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt22pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt22html+=1
            if result == "21" :
                if result2 =="doc":
                    for row in result_count:
                        cnt21doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt21xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt21ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt21hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt21pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt21html+=1
            if result == "20" :
                if result2 =="doc":
                    for row in result_count:
                        cnt20doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt20xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt20ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt20hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt20pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt20html+=1
            if result == "19" :
                if result2 =="doc":
                    for row in result_count:
                        cnt19doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt19xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt19ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt19hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt19pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt19html+=1
            if result == "18" :
                if result2 =="doc":
                    for row in result_count:
                        cnt18doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt18xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt18ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt18hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt18pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt18html+=1
            if result == "17" :
                if result2 =="doc":
                    for row in result_count:
                        cnt17doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt17xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt17ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt17hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt17pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt17html+=1
            if result == "16" :
                if result2 =="doc":
                    for row in result_count:
                        cnt16doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt16xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt16ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt16hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt16pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt16html+=1
            if result == "15" :
                if result2 =="doc":
                    for row in result_count:
                        cnt15doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt15xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt15ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt15hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt15pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt15html+=1
            if result == "14" :
                if result2 =="doc":
                    for row in result_count:
                        cnt14doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt14xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt14ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt14hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt14pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt14html+=1
            if result == "13" :
                if result2 =="doc":
                    for row in result_count:
                        cnt13doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt13xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt13ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt13hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt13pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt13html+=1
            if result == "12" :
                if result2 =="doc":
                    for row in result_count:
                        cnt12doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt12xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt12ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt12hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt12pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt12html+=1
            if result == "11" :
                if result2 =="doc":
                    for row in result_count:
                        cnt11doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt11xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt11ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt11hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt11pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt11html+=1
            if result == "10" :
                if result2 =="doc":
                    for row in result_count:
                        cnt10doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt10xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt10ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt10hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt10pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt10html+=1
            if result == "09" :
                if result2 =="doc":
                    for row in result_count:
                        cnt09doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt09xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt09ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt09hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt09pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt09html+=1
            if result == "08" :
                if result2 =="doc":
                    for row in result_count:
                        cnt08doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt08xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt08ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt08hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt08pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt08html+=1
            if result == "07" :
                if result2 =="doc":
                    for row in result_count:
                        cnt07doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt07xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt07ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt07hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt07pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt07html+=1
            if result == "06" :
                if result2 =="doc":
                    for row in result_count:
                        cnt06doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt06xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt06ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt06hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt06pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt06html+=1  
            if result == "05" :
                if result2 =="doc":
                    for row in result_count:
                        cnt05doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt05xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt05ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt05hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt05pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt05html+=1
            if result == "04" :
                if result2 =="doc":
                    for row in result_count:
                        cnt04doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt04xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt04ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt04hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt04pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt04html+=1
            if result == "03" :
                if result2 =="doc":
                    for row in result_count:
                        cnt03doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt03xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt03ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt03hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt03pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt03html+=1
            if result == "02" :
                if result2 =="doc":
                    for row in result_count:
                        cnt02doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt02xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt02ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt02hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt02pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt02html+=1
            if result == "01" :
                if result2 =="doc":
                    for row in result_count:
                        cnt01doc+=1
                if result2 == "xls":
                    for row in result_count:
                        cnt01xls+=1
                if result2 == "ppt":
                    for row in result_count:
                        cnt01ppt+=1
                if result2 == "hwp":
                    for row in result_count:
                        cnt01hwp+=1
                if result2 == "pdf":
                    for row in result_count:
                        cnt01pdf+=1
                if result2 == "html":
                    for row in result_count:
                        cnt01html+=1

    totalcnt00=cnt00doc+cnt00xls+cnt00ppt+cnt00hwp+cnt00pdf+cnt00html #합계의 개수

    totalcnt23=cnt23doc+cnt23xls+cnt23ppt+cnt23hwp+cnt23pdf+cnt23html

        
    totalcnt22=cnt22doc+cnt22xls+cnt22ppt+cnt22hwp+cnt22pdf+cnt22html


    totalcnt21=cnt21doc+cnt21xls+cnt21ppt+cnt21hwp+cnt21pdf+cnt21html


    totalcnt20=cnt20doc+cnt20xls+cnt20ppt+cnt20hwp+cnt20pdf+cnt20html


    totalcnt19=cnt19doc+cnt19xls+cnt19ppt+cnt19hwp+cnt19pdf+cnt19html


    totalcnt18=cnt18doc+cnt18xls+cnt18ppt+cnt18hwp+cnt18pdf+cnt18html


    totalcnt17=cnt17doc+cnt17xls+cnt17ppt+cnt17hwp+cnt17pdf+cnt17html


    totalcnt16=cnt16doc+cnt16xls+cnt16ppt+cnt16hwp+cnt16pdf+cnt16html


    totalcnt15=cnt15doc+cnt15xls+cnt15ppt+cnt15hwp+cnt15pdf+cnt15html


    totalcnt14=cnt14doc+cnt14xls+cnt14ppt+cnt14hwp+cnt14pdf+cnt14html


    totalcnt13=cnt13doc+cnt13xls+cnt13ppt+cnt13hwp+cnt13pdf+cnt13html


    totalcnt12=cnt12doc+cnt12xls+cnt12ppt+cnt12hwp+cnt12pdf+cnt12html


    totalcnt11=cnt11doc+cnt11xls+cnt11ppt+cnt11hwp+cnt11pdf+cnt11html


    totalcnt10=cnt10doc+cnt10xls+cnt10ppt+cnt10hwp+cnt10pdf+cnt10html


    totalcnt09=cnt09doc+cnt09xls+cnt09ppt+cnt09hwp+cnt09pdf+cnt09html


    totalcnt08=cnt08doc+cnt08xls+cnt08ppt+cnt08hwp+cnt08pdf+cnt08html


    totalcnt07=cnt07doc+cnt07xls+cnt07ppt+cnt07hwp+cnt07pdf+cnt07html


    totalcnt06=cnt06doc+cnt06xls+cnt06ppt+cnt06hwp+cnt06pdf+cnt06html
                    

    totalcnt05=cnt05doc+cnt05xls+cnt05ppt+cnt05hwp+cnt05pdf+cnt05html


    totalcnt04=cnt04doc+cnt04xls+cnt04ppt+cnt04hwp+cnt04pdf+cnt04html


    totalcnt03=cnt03doc+cnt03xls+cnt03ppt+cnt03hwp+cnt03pdf+cnt03html


    totalcnt02=cnt02doc+cnt02xls+cnt02ppt+cnt02hwp+cnt02pdf+cnt02html


    totalcnt01=cnt01doc+cnt01xls+cnt01ppt+cnt01hwp+cnt01pdf+cnt01html


    f.close()
    doc=[cnt00doc,cnt01doc,cnt02doc,cnt03doc,cnt04doc,cnt05doc,cnt06doc,cnt07doc,cnt08doc,cnt09doc,
            cnt10doc,cnt11doc,cnt12doc,cnt13doc,cnt14doc,cnt15doc,cnt16doc,cnt17doc,cnt18doc,cnt19doc,
            cnt20doc,cnt21doc,cnt22doc,cnt23doc]
    xls=[cnt00xls,cnt01xls,cnt02xls,cnt03xls,cnt04xls,cnt05xls,cnt06xls,cnt07xls,cnt08xls,cnt09xls,
            cnt10xls,cnt11xls,cnt12xls,cnt13xls,cnt14xls,cnt15xls,cnt16xls,cnt17xls,cnt18xls,cnt19xls,
            cnt20xls,cnt21xls,cnt22xls,cnt23xls]
    ppt=[cnt00ppt,cnt01ppt,cnt02ppt,cnt03ppt,cnt04ppt,cnt05ppt,cnt06ppt,cnt07ppt,cnt08ppt,cnt09ppt
                ,cnt10ppt,cnt11ppt,cnt12ppt,cnt13ppt,cnt14ppt,cnt15ppt,cnt16ppt,cnt17ppt,cnt18ppt,cnt19ppt,
                cnt20ppt,cnt21ppt,cnt22ppt,cnt23ppt]
    hwp=[cnt00hwp,cnt01hwp,cnt02hwp,cnt03hwp,cnt04hwp,cnt05hwp,cnt06hwp,cnt07hwp,cnt08hwp,cnt09hwp,
        cnt10hwp,cnt11hwp,cnt12hwp,cnt13hwp,cnt14hwp,cnt15hwp,cnt16hwp,cnt17hwp,cnt18hwp,cnt19hwp
        ,cnt20hwp,cnt21hwp,cnt22hwp,cnt23hwp]
    pdf=[cnt00pdf,cnt01pdf,cnt02pdf,cnt03pdf,cnt04pdf,cnt05pdf,cnt06pdf,cnt07pdf,cnt08pdf,cnt09pdf,
        cnt10pdf,cnt11pdf,cnt12pdf,cnt13pdf,cnt14pdf,cnt15pdf,cnt16pdf,cnt17pdf,cnt18pdf,cnt19pdf
        ,cnt20pdf,cnt21pdf,cnt22pdf,cnt23pdf]
    html=[cnt00html,cnt01html,cnt02html,cnt03html,cnt04html,cnt05html,cnt06html,cnt07html,cnt08html,cnt09html,
        cnt10html,cnt11html,cnt12html,cnt13html,cnt14html,cnt15html,cnt16html,cnt17html,cnt18html,cnt19html
        ,cnt20html,cnt21html,cnt22html,cnt23html]
    
    total=[totalcnt00,totalcnt01,totalcnt02,totalcnt03,totalcnt04,
        totalcnt05,totalcnt06,totalcnt07,totalcnt08,totalcnt09,
        totalcnt10,totalcnt11,totalcnt12,totalcnt13,totalcnt14,
        totalcnt15,totalcnt16,totalcnt17,totalcnt18,totalcnt19,
        totalcnt20,totalcnt21,totalcnt22,totalcnt23]

    time=['00','01','02','03','04','05','06','07','08','09',
        '10','11','12','13','14','15','16','17','18','19',
        '20','21','22','23']

    docx=[1,8,15,22,29,36,43,50,57,64,71,78,85,92,99,106,113,120,127,134,141,148,155,162]
    xlsx=[2,9,16,23,30,37,44,51,58,65,72,79,86,93,100,107,114,121,128,135,142,149,156,163]
    pptx=[3,10,17,24,31,38,45,52,59,66,73,80,87,94,101,108,115,122,129,136,143,150,157,164]
    hwpx=[4,11,18,25,32,39,46,53,60,67,74,81,88,95,102,109,116,123,130,137,144,151,158,165]
    pdfx=[5,12,19,26,33,40,47,54,61,68,75,82,89,96,103,110,117,124,131,138,145,152,159,166]
    htmlx=[6,13,20,27,34,41,48,55,62,69,76,83,90,97,104,111,118,125,132,139,146,153,160,167]
    totalx=[7,14,21,28,35,42,49,56,63,70,77,84,91,98,105,112,119,126,133,140,147,154,161,168]

    fig = plt.figure(figsize=(10,10)) ## 캔버스 생성
    fig.set_facecolor('white') ## 배경색 설정
    ticklabel=['00','01','02','03','04','05','06','07','08','09',
            '10','11','12','13','14','15','16','17','18','19',
            '20','21','22','23']
    plt.bar(docx,doc,color='skyblue',width=1,label="DOC(X)")
    plt.bar(xlsx,xls,color='g',width=1,label="XLS(X)")
    plt.bar(pptx,ppt,color='y',width=1,label="PPT(X)")
    plt.bar(hwpx,hwp,color='red',width=1,label="HWP(X)")
    plt.bar(pdfx,pdf,color='pink',width=1,label="PDF")
    plt.bar(htmlx,html,color='orange',width=1,label="HTML")
    plt.bar(totalx,total,color='black',width=1,label="TOTAL")

    plt.xlabel('Time')
    plt.ylabel('Data')
    plt.legend(loc=0)
    plt.title(root.filename)
    plt.xticks(docx,ticklabel,fontsize=10,rotation=0)

    plt.show()
    img = BytesIO()
    plt.savefig(img, format='png', dpi=200)
    img.seek(0)

    # my_image = ImageTk.PhotoImage(Image.open(root.filename)) ## 밑에 사진 뜨는거
    Label(img).pack() #사진 view
 
 
my_btn = Button(root, text='파일열기', command=instart).pack()
 
root.mainloop()