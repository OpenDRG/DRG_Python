from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["D18.000x028","D35.500","G45.801","G93.501","I63.201","I63.204","I63.205","I63.402","I63.500","I63.900","I63.902","I63.905","I65.200x001","I65.201","I65.202","I67.100x019","I67.500","Q28.200"]
  adrg_zd1=[]
  adrg_ss=["38.0100x001","38.0200x002","38.0201","38.1200x003","38.1201","38.1202","38.3101","38.3200x002","38.6101","38.6102","39.2800x002","39.2801","39.5001","39.5900x006","39.8901"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合BE1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCB_DRG.BE19_group(record):
      return 'BE19'

    return 'BE1'
  else:
    return ''

