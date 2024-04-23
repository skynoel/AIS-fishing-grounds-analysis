import AIS.mad
import AIS.patd
import AIS.chr_patd


mod=str(input("請輸入你想要執行的模式(1:mad,2:patd,3:chr_patd,4:asd,5:pfg)"))
if mod=="1":
    file=str(input("請輸入要被執行的資料夾路徑"))
    name=str(input("請輸入欲儲存的檔名(須加上.xlsx)"))
    year=str(input("請輸入要被執行的檔案年分"))
    month=str(input("請輸入要被執行的檔案月份"))
    file2=AIS.mad.avperm(file,name,year,month)  #將經過時間碼標記的原始資料轉變為個小時每分鐘平均封包數的資料，並回傳檔名
    AIS.mad.graph(file2)#利用該資料繪製成MAD
elif mod=="2":
    file=str(input("請輸入要被執行的檔案路徑"))
    name=str(input("請輸入欲儲存的檔名(須加上.xlsx)"))
    file3=AIS.patd.chose(file,name)#在MAD資料中以特定算法標記出封包數較多的時間產生EXCEL檔並回傳檔名
elif mod=="3":
    file=str(input("請輸入要被執行的檔案路徑"))
    name=str(input("請輸入欲儲存的檔名(須加上.xlsx)"))
    file4=AIS.chr_patd.chr(file,name)#將PATD檔加入琪合規則產生新的EXCEL檔並回傳檔名
elif mod=="4" or mod=="5":
    print("此功能尚未開放")
else :
    print("不要亂輸入")



  
   




