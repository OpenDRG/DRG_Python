from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCS_DRG

def group(record):
  adrg_zd=["A01.000x010","A01.000x012","A02.000","A02.003","A02.004","A02.900x003","A18.101","A18.103+N29.1*","A18.106+N29.1*","A18.108+N33.0*","A18.200x006","A18.207","A18.210","A18.211","A18.212","A22.000","A26.000","A31.000","A31.000x001","A48.100x001","A50.900","A51.303","A51.304","A52.101","A52.300","A53.000x001","A53.900","A54.002","A54.900x001","A60.001","A63.001","A63.002","A69.200","A70.x00","A78.x00","A79.901","A93.801","B00.202","B00.205","B02.900x001","B08.200","B08.200x002","B18.103+N08.0*","B26.804","B26.900x001","B37.800x088","B49.x00x007","B49.x11","B49.x18","B50.900x001","B67.907","B69.802","B69.803","B74.901","B99.x00x001","B99.x01","T88.000"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合SZ1入组条件，匹配规则：主诊断匹配')
    
    if MDCS_DRG.SZ11_group(record):
      return 'SZ11'

    if MDCS_DRG.SZ13_group(record):
      return 'SZ13'

    if MDCS_DRG.SZ15_group(record):
      return 'SZ15'

    return 'SZ1'
  else:
    return ''

