from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCK_DRG

def group(record):
  adrg_zd=["C73.x00","C73.x00x003","D34.x00","D35.100","D44.201","E04.100x005","E04.101","E04.102","E04.200","E04.200x003","E04.201","E04.901","E04.902","E05.900x001","E06.300x005","E06.304","E07.901","E21.401","Q89.206"]
  adrg_zd1=[]
  adrg_ss=["06.0100x001","06.0901","06.0902","06.1200","06.3100","06.3101","06.3102","06.7x02","06.8100","06.8100x002","06.8902","06.8903","06.8904","06.9501","06.9800","06.9900x002","40.1900x002"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合KD2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCK_DRG.KD29_group(record):
      return 'KD29'

    return 'KD2'
  else:
    return ''

