from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCM_DRG

def group(record):
  adrg_zd=["A18.118+N51.1*","C60.000","C60.900","C62.900","I86.101","N40.x00","N41.000","N43.001","N43.100","N43.300","N43.301","N43.302","N44.x00","N44.x01","N44.x02","N45.906","N45.907","N45.908","N46.x01","N47.x00x001","N47.x01","N47.x03","N48.100","N48.800x005","N48.803","N48.811","N49.001","N49.204","N50.102","N50.800","N50.803","N50.816","N50.820","N50.902","Q53.100","Q53.101","Q53.102","Q53.200","Q53.202","Q53.901","Q53.902","Q55.003","Q55.004","Q55.202","Q55.606","S30.205","S31.200","S31.300x001","S39.900x007"]
  adrg_zd1=[]
  adrg_ss=["54.0x00x004","54.0x00x013","54.0x01","54.0x03","54.2100","54.5101","60.1901","60.7100","60.7200x002","61.0x00x003","61.0x01","61.0x02","61.0x03","61.0x04","61.3x03","61.4900x002","61.4901","61.4904","61.4905","62.9100","63.1x00x004","63.1x00x005","63.3x02","63.3x03","63.9900x001","64.0x00","86.2800x012","98.2402"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合MJ1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCM_DRG.MJ19_group(record):
      return 'MJ19'

    return 'MJ1'
  else:
    return ''

