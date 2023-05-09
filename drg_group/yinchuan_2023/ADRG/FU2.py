from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I25.104","I44.000","I44.100","I44.101","I44.102","I44.303","I44.602","I45.101","I45.102","I45.200","I45.501","I45.502","I45.600","I45.600x003","I45.600x004","I45.600x005","I47.100","I47.100x004","I47.100x005","I47.101","I47.102","I47.104","I47.106","I47.108","I47.109","I47.900","I48.000","I48.100","I48.100x002","I48.100x003","I48.200","I48.900x004","I48.900x015","I49.100x001","I49.101","I49.200x001","I49.300x002","I49.301","I49.303","I49.402","I49.403","I49.500","I49.501","I49.800x010","I49.801","I49.802","I49.900","R00.000","R00.001","R00.100","R00.100x001","R00.200","R94.300x011"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合FU2入组条件，匹配规则：主诊断匹配')
    
    if MDCF_DRG.FU21_group(record):
      return 'FU21'

    if MDCF_DRG.FU23_group(record):
      return 'FU23'

    if MDCF_DRG.FU25_group(record):
      return 'FU25'

    return 'FU2'
  else:
    return ''

