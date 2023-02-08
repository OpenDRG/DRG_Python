from drg_group.taizhou_2022.Base import message,intersect,SS_VALID
from drg_group.taizhou_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["35.0501","35.0502","35.0701","35.0900","35.9500x006","35.9600x008","35.9601","35.9602","35.9603","35.9604","35.9700x001","35.9700x002","35.9700x003","35.9700x004","35.9700x005","35.9700x006"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FL3入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FL39_group(record):
      return 'FL39'

    return 'FL3'
  else:
    return ''

