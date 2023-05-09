from drg_group.lanzhou_2023.Base import message,intersect,SS_VALID
from drg_group.lanzhou_2023.DRG import MDCE_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["31.1x00x005","31.4100","31.4200x001","31.4200x003","31.4201","31.4202","31.4300x002","31.4301","31.4400x001","31.9400","33.2100","33.2200x002","33.2200x003","33.2300x002","33.2300x003","33.2301","33.2302","33.9200","34.7300x001","96.0500x001","96.5602"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合EJ1入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if MDCE_DRG.EJ11_group(record):
      return 'EJ11'

    if MDCE_DRG.EJ1B_group(record):
      return 'EJ14'

    return 'EJ1'
  else:
    return ''

