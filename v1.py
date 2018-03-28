import string
from ctypes import windll
import time
import os, sys
from os import walk


import subprocess
import ftplib


def ftpSend(host,user,passs,destFolder,newFile):
    #Login FTP to Summit
    #host = "192.168.196.92"
    #user = "mxfmovie"
    print("New File",newFile)
    passs = ""
    ftp = ftplib.FTP(host)
    ftp.login(user,passs)
    ftp.cwd(destFolder)
    #print ftp.pwd()
    print ("Enviando ",os.path.basename(newFile) ," a ftp Dest...")
    ftp.storbinary('STOR '+os.path.basename(newFile),open(newFile,'rb'))
    ftp.quit()
    print ("Listo.")



def muxer(video,ffmpeg_path,temp_dir,ingest_folder,stratus_ftp,stratus_ftp_user,stratus_ftp_pass,ftp_material_name):
  
    FinalVideo = ftp_material_name 

    

    print("ingest_folder: ",ingest_folder,"stratus_ftp: ",stratus_ftp," stratus_ftp_user: ",stratus_ftp_user," stratus_ftp_pass:",stratus_ftp_pass)
    
    videoMerge = ffmpeg_path+'ffmpeg -i '+video+' -vcodec mpeg2video -vtag xd5b -s 1920x1080 -pix_fmt yuv420p -rtbufsize 50000k -b:v 50000k -dc 9 -flags +ilme+ildct -top 1 -acodec pcm_s16le -ac 4 -f mxf '+temp_dir+FinalVideo+'.mxf'
    print("Muxing Video" + videoMerge)
    videoMerge2 = videoMerge.split(' ')
    print(videoMerge2)
    

    p = subprocess.Popen(videoMerge2)
    p.wait()
    print("Sending: "+temp_dir+FinalVideo)
    ftpSend(stratus_ftp,stratus_ftp_user,stratus_ftp_pass,ingest_folder,temp_dir+FinalVideo+'.mxf')
    # drive =""
    print(FinalVideo,' ingestado.')



ffmpeg_path = ""

temp_dir = "C:\\Users\\enrique.nieto\\Documents\\develops 2017\\Milenio\\LiveUStoreForward\\temp\\"
temp_dir = ""
ingest_folder = "\\TEST\\"
stratus_ftp = "192.168.196.139"
stratus_ftp_user = "mxfmovie"
stratus_ftp_pass = ""

if(os.path.exists(temp_dir)):
	print("Existe ",temp_dir)
else:
	print("No existe ", temp_dir)

muxer("ggdf_180301_022155.mp4",ffmpeg_path,temp_dir,ingest_folder,stratus_ftp,stratus_ftp_user,stratus_ftp_pass,"pruebaSF2")