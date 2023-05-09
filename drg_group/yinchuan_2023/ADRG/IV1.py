from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=["Q65.000","Q65.100","Q65.200","Q65.300","Q65.801","Q65.802","Q65.803","Q66.000","Q66.600","Q66.700","Q66.800x006","Q66.800x008","Q66.800x010","Q66.800x015","Q66.801","Q66.803","Q66.804","Q67.600","Q67.700","Q68.001","Q68.002","Q68.100x009","Q68.100x010","Q68.102","Q68.201","Q68.800x006","Q68.800x018","Q68.800x020","Q68.800x024","Q68.807","Q68.812","Q68.813","Q69.000","Q69.100","Q69.900x001","Q69.900x002","Q70.400x002","Q70.900x001","Q70.900x002","Q72.601","Q72.900","Q74.001","Q74.003","Q74.010","Q74.100x004","Q74.100x006","Q74.101","Q74.102","Q74.106","Q74.900","Q76.500","Q78.400x002","Q78.400x006","Q78.405","Q78.600x002","Q78.900","Q79.800x004","Q79.800x005","Q79.800x006"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合IV1入组条件，匹配规则：主诊断匹配')
    
    if MDCI_DRG.IV13_group(record):
      return 'IV13'

    if MDCI_DRG.IV15_group(record):
      return 'IV15'

    return 'IV1'
  else:
    return ''

