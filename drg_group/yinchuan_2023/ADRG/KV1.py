from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCK_DRG

def group(record):
  adrg_zd=["E16.803","E71.000","E71.101","E71.102","E72.101","E72.200x004","E72.202","E72.900x006","E74.800x006","E74.801","E75.501","E77.801","E78.000","E78.002","E78.100","E78.200","E78.500","E79.001","E83.500x001","E88.203","E88.803","E88.900x010","E88.903"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合KV1入组条件，匹配规则：主诊断匹配')
    
    if MDCK_DRG.KV11_group(record):
      return 'KV11'

    if MDCK_DRG.KV13_group(record):
      return 'KV13'

    if MDCK_DRG.KV15_group(record):
      return 'KV15'

    return 'KV1'
  else:
    return ''

