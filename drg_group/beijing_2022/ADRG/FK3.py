from drg_group.beijing_2022.Base import message,intersect,SS_VALID
from drg_group.beijing_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["37.8000x001","37.8000x002","37.8001","37.8101","37.8201","37.8301","37.8501","37.8601","37.8701","37.8901","37.8902","37.8903","37.9400x001","37.9400x002","37.9401","37.9402","37.9403","37.9404","37.9600x001","37.9600x002","37.9800x001","37.9800x002","37.9800x003","37.9800x004"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FK3入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FK39_group(record):
      return 'FK39'

    return 'FK3'
  else:
    return ''

