from drg_group.chs_drg_10.Base import message,intersect,SS_VALID
from drg_group.chs_drg_10.DRG import MDCK_DRG

def group(record):
  adrg_zd=["C73.x00","C73.x00x003","C74.000","C74.100","C74.900","C75.000","C75.100","C75.200","C75.300","C75.900","C79.700","C79.800x839","C79.805","C79.825","D09.300","D09.301","D09.302","D09.303","D09.304"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合KR1入组条件，匹配规则：主诊断匹配')
    
    if MDCK_DRG.KR19_group(record):
      return 'KR19'

    return 'KR1'
  else:
    return ''

