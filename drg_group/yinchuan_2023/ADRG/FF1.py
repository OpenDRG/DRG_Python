from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I80.207","I80.302","I80.303","I80.902","I83.000","I83.001","I83.101","I83.200x001","I83.900x004","I83.903","I83.905","I87.115","I87.116","I87.201","I87.202"]
  adrg_zd1=[]
  adrg_ss=["38.5900x005","38.5900x008","38.5900x010","38.5901","38.5902","38.5903","38.5904","38.5905","38.5906","38.5907"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FF1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FF19_group(record):
      return 'FF19'

    return 'FF1'
  else:
    return ''

