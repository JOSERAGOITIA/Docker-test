
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import email.message
from turtle import st

from importlib.resources import contents
from json import load
from multiprocessing import connection
from re import S
import pandas as pd
import csv
import sqlite3





def main():
    msg = email.message.Message()
    msg = MIMEMultipart()
    message =  "Number of transactions in January: "+  filtered_df_jan  + "  Average credit amount January : "+str(Average_creditjan) + "  Average debit amount Janyary :"+str(Average_debitjan) +"\n" + "Number of transactions in February: "+ filtered_df_feb + "  Average credit amount February : "+str(Average_creditfeb) +"  Average debit amount February :"+str(Average_debitfeb) +"\n" +"Number of transactions in March: "+ filtered_df_mar + "  Average credit amount March : "+str(Average_creditmar) +"  Average debit amount March :"+str(Average_debitmar) +"\n" + "Number of transactions in April: "+ filtered_df_apr + "  Average credit amount April : "+str(Average_creditapr) +"  Average debit amount April :"+str(Average_debitapr) +"\n" "Number of transactions in May: "+ filtered_df_may + "  Average credit amount May : "+str(Average_creditmay) +"  Average debir amount May :"+str(Average_debitmay) +"\n"
    password = "umlpjdcoidhxrbxj"
    msg['From'] = "joseragoitia@gmail.com"
    msg['To'] = "jmflores0495@gmail.com"
    msg['Subject'] = "Stori Challenge "
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print("correo enviado")


def balance_ave():
    balance_df=df
    positive=(balance_df[balance_df["Transaction"]>0].sum())+(balance_df[balance_df["Transaction"]<0].sum())
    positive=positive['Transaction'].astype(float)
    #print(positive)
    return positive
def creditjan():
    creditjan=ave_df_jan
    rslt_creditjan = creditjan[creditjan['Transaction'] > 0]
    Average_creditjan=(rslt_creditjan['Transaction'].sum())/(rslt_creditjan['Id'].count())
    #print(Average_creditjan)
    return Average_creditjan
def debitjan():
    debitjan=ave_df_jan
    rslt_debitjan = debitjan[debitjan['Transaction'] < 0]
    Average_debitjan=(rslt_debitjan['Transaction'].sum())/(rslt_debitjan['Id'].count())
    #print(Average_debitjan)
    return Average_debitjan
def creditfeb():
    creditfeb=ave_df_feb
    rslt_creditfeb=creditfeb[creditfeb['Transaction'] > 0]
    Average_creditfeb=(rslt_creditfeb['Transaction'].sum())/(rslt_creditfeb['Id'].count())
    #print(Average_creditfeb)
    return Average_creditfeb
def debitfeb():
    debitfeb=ave_df_feb
    rslt_debitfeb = debitfeb[debitfeb['Transaction'] < 0]
    Average_debitfeb=(rslt_debitfeb['Transaction'].sum())/(rslt_debitfeb['Id'].count())
    #print(Average_debitfeb)
    return Average_debitfeb
def creditmar():
    creditmar=ave_df_mar
    rslt_creditmar=creditmar[creditmar['Transaction'] > 0]
    Average_creditmar=(rslt_creditmar['Transaction'].sum())/(rslt_creditmar['Id'].count())
    #print(Average_creditmar)
    return Average_creditmar
def debitmar():
    debitmar=ave_df_mar
    rslt_debitmar = debitmar[debitmar['Transaction'] < 0]
    Average_debitmar=(rslt_debitmar['Transaction'].sum())/(rslt_debitmar['Id'].count())
    #print(Average_debitmar)
    return Average_debitmar
def creditapr():
    creditapr=ave_df_apr
    rslt_creditapr=creditapr[creditapr['Transaction'] > 0]
    Average_creditapr=(rslt_creditapr['Transaction'].sum())/(rslt_creditapr['Id'].count())
    #print(Average_creditapr)
    return Average_creditapr
def debitapr():
    debitapr=ave_df_apr
    rslt_debitapr = debitapr[debitapr['Transaction'] < 0]
    Average_debitapr=(rslt_debitapr['Transaction'].sum())/(rslt_debitapr['Id'].count())
    #print(Average_debitapr)
    return Average_debitapr
def creditmay():
    creditmay=ave_df_may
    rslt_creditmay=creditmay[creditmay['Transaction'] > 0]
    Average_creditmay=(rslt_creditmay['Transaction'].sum())/(rslt_creditmay['Id'].count())
    #print(Average_creditmay)
    return Average_creditmay
def debitmay():
    debitmay=ave_df_may
    rslt_debitmay = debitmay[debitmay['Transaction'] < 0]
    Average_debitmay=(rslt_debitmay['Transaction'].sum())/(rslt_debitmay['Id'].count())
    #print(Average_debitmay)
    return  Average_debitmay
    

    
#file="D:\Jose Maria Flores Ragoitia\GitHub\Docker\Docker-test\data\data.csv"
data = pd.read_csv('data.csv')
df=pd.DataFrame(data,columns=['Id','Date','Transaction'])
df = df.replace({'Transaction':{'+':1, '-':-1}})
df["Transaction"] = pd.to_numeric(df["Transaction"])
df["Date"]=pd.to_datetime(df["Date"],format='%m/%d/%Y',dayfirst=False)
#print(df)
######balance_ave
#positive=float(balance_ave())
######January#########
df_jan = (df["Date"] > '2021-12-31') & (df["Date"] <= '2022-01-31')
ave_df_jan=df.loc[df_jan]
filtered_df_jan=ave_df_jan["Id"].count()
filtered_df_jan=str(filtered_df_jan)
Average_creditjan=str(creditjan())
Average_debitjan=str(debitjan())
######Feb#########
df_feb = (df["Date"] > '2022-01-31') & (df["Date"] <= '2022-02-28')
ave_df_feb=df.loc[df_feb]
filtered_df_feb=ave_df_feb["Id"].count()
filtered_df_feb=str(filtered_df_feb)
Average_creditfeb=str(creditfeb())
Average_debitfeb=str(debitfeb())
######March#########
df_mar = (df["Date"] > '2022-02-28') & (df["Date"] <= '2022-03-31')
ave_df_mar=df.loc[df_mar]
filtered_df_mar=ave_df_mar["Id"].count()
filtered_df_mar=str(filtered_df_mar)
Average_creditmar=str(creditmar())
Average_debitmar=str(debitmar())
#####April######
df_apr=(df["Date"] > '2022-03-31') & (df["Date"] <= '2022-04-30')
ave_df_apr=df.loc[df_apr]
filtered_df_apr=ave_df_apr["Id"].count()
filtered_df_apr=str(filtered_df_apr)
Average_creditapr=str(creditapr())
Average_debitapr=str(debitapr())
#####May###################
df_may=(df["Date"] > '2022-04-30') & (df["Date"] <= '2022-05-31')
ave_df_may=df.loc[df_may]
filtered_df_may=ave_df_may["Id"].count()
filtered_df_may=str(filtered_df_may)
Average_creditmay=int(creditmay())
Average_debitmay=int(debitmay())











def saveall_data_database():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS test(Id text, date text,trans VARCHAR(255))')
    conn.commit()
    #file='D:\Jose Maria Flores Ragoitia\Stori\Transaction.csv'
    data = pd.read_csv('data.csv')
    df=pd.DataFrame(data,columns=['Id','Date','Transaction'])
    df.to_sql('test',conn,if_exists='replace', index=False)
    cur.execute('''SELECT * FROM test''')
    for row in cur.fetchall():
        print(row)
    conn.commit()
    conn.close()
    print("Se creo la DATABASE")



saveall_data_database()
main()


