from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCR_DRG

def group(record):
  adrg_zd=["C76.801","C77.301","C78.604","C79.811","C81.300","C81.700","C82.100","C82.200","C83.300","C83.800","C83.800x008","C83.900","C84.400","C84.502","C84.901","C85.200","C85.707","C85.715","C85.900","C85.900x008","C85.900x010","C85.900x014","C88.400","C88.401","C90.000x005","C90.000x023","C90.000x034","C91.000","C91.000x009","C91.000x016","C91.001","C91.002","C91.003","C91.100","C91.300","C92.000","C92.000x011","C92.000x014","C92.000x015","C92.000x016","C92.000x017","C92.003","C92.004","C92.100x001","C92.100x016","C92.100x017","C92.400x011","C92.401","C92.402","C93.003","C93.100x012","C94.000x001","C94.202","C95.000","C95.900","C95.901","C96.604","C97.x00","C97.x01","D46.900","D46.900x002","D47.100x004","D47.100x008","D47.300","D47.401","D47.402","D47.700x006","D48.700x023","D48.715","Q85.802"]
  adrg_zd1=[]
  adrg_ss=["02.0600x003","03.4x03","25.0200","34.9101","34.9103","40.2908","45.4200x003","45.4307","48.3600x004","54.2100","54.9100x009","54.9101","60.2902","65.1201"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合RA2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCR_DRG.RA21_group(record):
      return 'RA21'

    if MDCR_DRG.RA23_group(record):
      return 'RA23'

    if MDCR_DRG.RA25_group(record):
      return 'RA25'

    return 'RA2'
  else:
    return ''

