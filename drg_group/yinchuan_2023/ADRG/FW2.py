from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I80.001","I80.002","I80.104","I80.201","I80.206","I80.207","I80.209","I80.300x006","I80.301","I80.302","I80.303","I80.901","I80.902","I82.203","I82.301","I82.801","I82.802","I82.803","I82.805","I82.806","I82.900x002","I82.900x004","I83.000","I83.001","I83.100x001","I83.101","I83.102","I83.200x001","I83.900x004","I83.901","I83.902","I83.903","I83.905","I87.100x008","I87.104","I87.106","I87.111","I87.113","I87.115","I87.116","I87.117","I87.201","I87.202","I87.805","Q27.800x042","Q27.817","Q27.818","Q28.900x001","Q82.800x015","R02.x00","S35.500x004","S75.200x001","S95.200"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合FW2入组条件，匹配规则：主诊断匹配')
    
    if MDCF_DRG.FW21_group(record):
      return 'FW21'

    if MDCF_DRG.FW25_group(record):
      return 'FW25'

    return 'FW2'
  else:
    return ''

