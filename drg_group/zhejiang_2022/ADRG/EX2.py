from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCE_DRG

def group(record):
  adrg_zd=["A37.000","A37.100","A37.800x001","A37.900","A37.900x003","A37.900x004","A37.901+J17.0*","J20.000","J20.100","J20.200","J20.300","J20.400","J20.500","J20.600","J20.700","J20.800","J20.900","J20.901","J20.902","J21.000","J21.100","J21.801","J21.900","J21.900x002","J21.901","J21.902"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and (not record.ssList or not record.ssList[0] in SS_VALID):
    message('符合EX2入组条件，匹配规则：主诊断匹配')
    
    if MDCE_DRG.EX29_group(record):
      return 'EX29'

    return ''
  else:
    return ''

