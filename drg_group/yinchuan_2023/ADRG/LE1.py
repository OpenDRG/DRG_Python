from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCL_DRG

def group(record):
  adrg_zd=["C67.900","C68.000","C68.803","D18.000x806","D30.400","N20.200x001","N21.000","N21.100","N30.000","N34.001","N35.000","N35.100x001","N35.800","N35.900","N35.901","N36.000","N36.100","N36.200","N36.806","N36.807","N36.808","N36.809","N36.901","N39.300","N39.403","N99.101","N99.800x006","Q64.702","S37.301","T19.000"]
  adrg_zd1=[]
  adrg_ss=["58.0x01","58.1x01","58.3101","58.3103","58.3901","58.3903","58.3905","58.3906","58.4301","58.4600x007","58.4700","58.4900x003","58.4901","58.5x00","58.5x00x002","58.6x00x001","58.6x00x003","58.9200x002","58.9201","59.5x00","59.5x01","59.7903","59.9903","98.1900x001"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合LE1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCL_DRG.LE19_group(record):
      return 'LE19'

    return 'LE1'
  else:
    return ''

