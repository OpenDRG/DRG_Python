from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCS_DRG

def group(record):
  adrg_zd=["A18.101","A18.103+N29.1*","A18.200x006","A18.207","A18.210","A19.900x005","A22.000","A41.900","A42.000","A49.814","A49.815","A49.901","A63.001","B00.901","B02.900x002","B08.100","B27.900x001","B42.900","B67.301","B67.400x001","B67.901","B67.904","B90.102+N29.1*","B99.x01","R50.900","T79.300x001","T81.400x001","T81.400x004","T81.405","T81.406","T85.703"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合SB1入组条件，匹配规则：主诊断匹配')
    
    if MDCS_DRG.SB11_group(record):
      return 'SB11'

    if MDCS_DRG.SB13_group(record):
      return 'SB13'

    if MDCS_DRG.SB15_group(record):
      return 'SB15'

    return 'SB1'
  else:
    return ''

