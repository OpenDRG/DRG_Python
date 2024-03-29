from drg_group.hefei_2023.Base import message,intersect,SS_VALID
from drg_group.hefei_2023.DRG import MDCN_DRG
from drg_group.hefei_2023.DRG_EX import NC1X

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["38.8607","38.8609","38.8700x002","38.8700x008","38.8700x009","38.8702","54.4x10","68.0x00x004","68.0x00x005","68.0x00x006","68.0x00x007","68.0x01","68.1300","68.1501","68.2400","68.2401","68.2500x001","68.2501","68.3100x002","68.3101","68.3102","68.3103","68.3104","68.3105","68.3106","68.3900x003","68.3901","68.3902","68.3903","68.3904","68.3905","68.3906","68.3907","68.4100","68.4101","68.4102","68.4103","68.4104","68.4900x004","68.4900x006","68.4901","68.4902","68.4903","68.4905","68.5100x004","68.5100x005","68.5101","68.5102","68.5103","68.5900x002","68.5900x003","68.5901","68.5902","68.6100x001","68.6100x002","68.6101","68.6900x001","68.6900x002","68.6901","68.6902","68.7100x001","68.7900x003","68.7901","68.9x00"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合NC1入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if NC1X.group(record):
      return 'NC1X'

    
    if MDCN_DRG.NC11_group(record):
      return 'NC11'

    if MDCN_DRG.NC13_group(record):
      return 'NC13'

    if MDCN_DRG.NC15_group(record):
      return 'NC15'

    return ''
  else:
    return ''

