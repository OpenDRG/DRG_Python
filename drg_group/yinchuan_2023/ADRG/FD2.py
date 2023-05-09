from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["A18.808+I32.0*","D15.101","D15.102","D15.103","D48.712","I08.103","I20.000","I20.801","I21.900","I23.300x001","I25.102","I25.301","I31.300","I31.901","I35.100","I45.102","I45.600","I45.600x003","I45.600x004","I45.600x005","I47.100","I47.100x004","I47.100x005","I47.101","I47.102","I47.104","I47.106","I47.108","I47.200","I47.200x008","I47.201","I47.203","I48.000","I48.100","I48.100x003","I48.900x003","I48.900x004","I49.100x001","I49.101","I49.300x002","I49.301","I49.500","I49.501","I50.002","I50.101","R94.300x011"]
  adrg_zd1=[]
  adrg_ss=["37.1100x009","37.1200x005","37.1200x010","37.1200x011","37.1204","37.3101","37.3104","37.3300x008","37.3300x014","37.3300x016","37.3300x018","37.3301","37.3302","37.3305","37.3306","37.3600x007","37.4900x002","37.9000x001"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FD2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FD21_group(record):
      return 'FD21'

    if MDCF_DRG.FD23_group(record):
      return 'FD23'

    if MDCF_DRG.FD25_group(record):
      return 'FD25'

    return 'FD2'
  else:
    return ''

