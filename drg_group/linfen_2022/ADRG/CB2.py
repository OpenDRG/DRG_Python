from drg_group.linfen_2022.Base import message,intersect,SS_VALID
from drg_group.linfen_2022.DRG import MDCC_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["12.1100x002","12.1101","12.1200x001","12.1201","12.1202","12.1203","12.1300","12.1400x001","12.1400x008","12.1401","12.1402","12.1403","12.1404","12.3100","12.3200x001","12.3300","12.3301","12.3500","12.3501","12.3502","12.3503","12.3504","12.3900x001","12.3900x004","12.3901","12.3902","12.4100x001","12.4100x002","12.4100x003","12.4100x004","12.4401","12.6301","12.9701","12.9702","12.9703"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合CB2入组条件，匹配规则：主手术匹配')
    
    if MDCC_DRG.CB23_group(record):
      return 'CB23'

    if MDCC_DRG.CB25_group(record):
      return 'CB25'

    return 'CB2'
  else:
    return ''

