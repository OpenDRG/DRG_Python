from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCH_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["50.1101","50.2303","51.0102","51.1000","51.1100","51.1101","51.1102","51.1103","51.1105","51.1201","51.1202","51.1301","51.1302","51.1402","51.1403","51.1404","51.1500","51.9802","51.9809","52.1101","52.1301","52.1303","52.1400","52.1900x001"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合HL1入组条件，匹配规则：主手术匹配')
    
    if MDCH_DRG.HL11_group(record):
      return 'HL11'

    if MDCH_DRG.HL13_group(record):
      return 'HL13'

    if MDCH_DRG.HL15_group(record):
      return 'HL15'

    return ''
  else:
    return ''

