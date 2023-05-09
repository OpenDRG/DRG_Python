from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I10.x00x002","I10.x00x016","I10.x03","I10.x04","I10.x05","I10.x06","I10.x09","I10.x10","I10.x12","I10.x14","I11.901","I15.100x001","I15.102","I15.200x001","I15.800x006","I15.900"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合FV2入组条件，匹配规则：主诊断匹配')
    
    if MDCF_DRG.FV21_group(record):
      return 'FV21'

    if MDCF_DRG.FV23_group(record):
      return 'FV23'

    if MDCF_DRG.FV25_group(record):
      return 'FV25'

    return 'FV2'
  else:
    return ''

