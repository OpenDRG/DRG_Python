from drg_group.wuhan_2022.Base import message,intersect,SS_VALID
from drg_group.wuhan_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["36.1000x001","36.1000x002","36.1100","36.1200","36.1300","36.1400","36.1500","36.1600","36.1700x001","36.1900x001","36.2x00"]
  adrg_ss1=["00.2400x001","00.5900x003","00.5901","00.5902","37.2100","37.2200","37.2300","37.2600x001","88.5201","88.5202","88.5301","88.5302","88.5400x001","88.5500","88.5500x002","88.5600","88.5600x002","88.5700x003","88.5701","88.5800","88.5900"]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss) and intersect(record.ssList,adrg_ss1):
    message('符合FC2入组条件，匹配规则：双手术匹配')
    
    if MDCF_DRG.FC29_group(record):
      return 'FC29'

    return 'FC2'
  else:
    return ''

