from drg_group.yunnan_2023.Base import message,intersect,SS_VALID
from drg_group.yunnan_2023.DRG import MDCP_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["21.0902","31.3x03","31.7900x004","31.7900x005","45.9301","45.9303","47.1900x001","49.9100","58.0x05","58.3103","58.3905","58.5x00","58.5x01","59.0201","59.0202"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ageDay!=None and record.ageDay<=28:
    message('符合PJ1入组条件，匹配规则：主手术匹配、新生儿')
    
    
    if MDCP_DRG.PJ19_group(record):
      return 'PJ19'

    return ''
  else:
    return ''
