from drg_group.wuhan_2022.Base import message,intersect,SS_VALID
from drg_group.wuhan_2022.DRG import MDCI_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["04.0310","04.0715","04.0716","04.0717","04.0719","04.0720","04.0721","04.0733","04.1102","04.1103","04.3x06","04.3x15","04.3x16","04.4900x043","04.4900x044","04.4900x045","04.4912","04.6x09","04.7407","04.7408","04.7409","04.7410","04.7412","04.7413","04.7414","04.7417","04.7418","04.7900","04.8101","04.8106","04.8900"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合IH1入组条件，匹配规则：主手术匹配')
    
    if MDCI_DRG.IH11_group(record):
      return 'IH11'

    if MDCI_DRG.IH1B_group(record):
      return 'IH1B'

    return 'IH1'
  else:
    return ''

