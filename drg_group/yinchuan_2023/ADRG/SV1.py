from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCS_DRG

def group(record):
  adrg_zd=["A01.000","A01.000x017","A01.100","A01.400","A19.200","A19.200x001","A19.900","A19.900x005","A23.000","A23.000x001","A23.100x001","A23.800","A23.900x001","A23.900x004","A30.300x002","A31.803","A35.x00x001","A38.x00","A38.x00x010","A42.900","A43.800x001","A49.001","A49.002","A49.100x004","A49.101","A49.102","A49.103","A49.300","A49.801","A49.803","A49.806","A49.810","A49.812","A49.813","A49.815","A49.900","A49.901","A49.902","Z03.000"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合SV1入组条件，匹配规则：主诊断匹配')
    
    if MDCS_DRG.SV11_group(record):
      return 'SV11'

    if MDCS_DRG.SV13_group(record):
      return 'SV13'

    if MDCS_DRG.SV15_group(record):
      return 'SV15'

    return 'SV1'
  else:
    return ''

