from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCN_DRG

def group(record):
  adrg_zd=["A18.100x019+N77.1*","A18.102","A18.111+N74.1*","A18.112+N74.0*","A18.113+N74.1*","A18.114+N74.1*","A18.115+N74.1*","N70.001","N70.100","N70.900x007","N70.904","N70.905","N71.101","N72.x00x003","N73.500","N76.100x001","N76.200","N76.801"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合NS1入组条件，匹配规则：主诊断匹配')
    
    if MDCN_DRG.NS19_group(record):
      return 'NS19'

    return 'NS1'
  else:
    return ''

