from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCK_DRG

def group(record):
  adrg_zd=["C73.x00","C73.x00x003","C79.805","D34.x00","D34.x00x003","D44.000x001","D44.001","E04.100x005","E04.101","E04.102","E04.200","E04.200x003","E04.201","E04.901","E04.902","E04.903","E05.202","E05.203","E05.900x001","E06.100","E06.100x001","E06.300x005","E06.304","E06.500x002","E06.500x004","E06.900","E07.803","E07.901"]
  adrg_zd1=[]
  adrg_ss=["06.2x00","06.2x01","06.2x02","06.2x03","06.2x04","06.3900x003","06.3900x004","06.3900x011","06.3900x012","06.3900x013","06.3901","06.3902","06.3903","06.3905","06.3906","06.3907","06.3908","06.4x00","06.4x01","06.4x02","06.5000","06.5100","06.5101","06.5200","06.9401","40.4100","40.4200"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合KD1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCK_DRG.KD19_group(record):
      return 'KD19'

    return 'KD1'
  else:
    return ''

