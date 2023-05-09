from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCE_DRG

def group(record):
  adrg_zd=["A15.007","A15.201","A15.601","A15.603","A16.008","A16.500x004","A16.500x010","A16.501","C34.000x003","C34.001","C34.100x003","C34.100x004","C34.201","C34.300x004","C34.803","C34.900x005","C49.300x003","C78.000","C78.200","D02.200x002","D14.300x001","D38.101","D38.300x001","J39.805","J43.901","J43.902","J44.000","J60.x00x002","J85.100","J86.007","J86.902","J90.x01","J93.100x001","J93.800x001","J94.802","J94.804","J98.011","J98.409","J98.414","R91.x00x001","R91.x03","R91.x04","S27.200","T17.500","T17.804"]
  adrg_zd1=[]
  adrg_ss=["32.0901","32.2100x005","32.2400x001","32.2802","32.2803","32.2804","32.2901","32.2902","32.2904","33.0x03","33.1x04","33.2500x002","33.7901","33.9101","34.0200x001","34.0600","34.0900x010","34.2000","34.2100x001","34.2301","34.4x00x008"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合EB2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCE_DRG.EB29_group(record):
      return 'EB29'

    return 'EB2'
  else:
    return ''

