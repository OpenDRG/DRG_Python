from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCG_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["45.4200x003","45.4201","45.4202","45.4300x008","45.4302","45.4303","45.4304","45.4305","45.4306","45.4900x005","46.8500x008","46.8500x009","46.8511","46.8600","46.9601","48.3200x001","48.3200x003","48.3201","48.3301","48.3508","48.3602","98.0303","98.0401","98.0500x003"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合GK3入组条件，匹配规则：主手术匹配')
    
    if MDCG_DRG.GK31_group(record):
      return 'GK31'

    if MDCG_DRG.GK33_group(record):
      return 'GK33'

    if MDCG_DRG.GK35_group(record):
      return 'GK35'

    return ''
  else:
    return ''

