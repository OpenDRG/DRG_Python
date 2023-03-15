from drg_group.changsha_2023.Base import message,intersect,SS_VALID
from drg_group.changsha_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["00.5000x001","00.5000x004","00.5000x005","00.5001","00.5002","00.5100x001","00.5101","00.5102","00.5301","00.5302","00.5401","00.5402"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FK2入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FK29_group(record):
      return 'FK29'

    return 'FK2'
  else:
    return ''

