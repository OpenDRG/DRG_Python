from drg_group.yantai_2023.Base import message,intersect,SS_VALID
from drg_group.yantai_2023.DRG import MDCG_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["53.7100","53.7100x001","53.7101","53.7200x001","53.7201","53.7202","53.7500","53.9x00x016","53.9x00x017","53.9x00x020","53.9x00x021","53.9x00x022","53.9x01","53.9x02","53.9x03","53.9x04","53.9x05","53.9x06"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合GE2入组条件，匹配规则：主手术匹配')
    
    if MDCG_DRG.GE29_group(record):
      return 'GE29'

    return 'GE2'
  else:
    return ''

