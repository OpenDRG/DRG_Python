from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCB_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["38.3000x001","38.3100x001","38.6100x002","38.6101","38.8000","38.8101","39.2801","39.2802","39.5100x004","39.5100x007","39.5102","39.5103","39.5104","39.5105","39.5106","39.5107","39.5108","39.5200x002","39.5200x003","39.5202","39.5203","39.7203","39.9800x003"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合BC1入组条件，匹配规则：主手术匹配')
    
    if MDCB_DRG.BC11_group(record):
      return 'BC11'

    if MDCB_DRG.BC13_group(record):
      return 'BC13'

    if MDCB_DRG.BC15_group(record):
      return 'BC15'

    return ''
  else:
    return ''

