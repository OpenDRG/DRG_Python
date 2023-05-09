from drg_group.nanping_2023.Base import message,intersect,SS_VALID
from drg_group.nanping_2023.DRG import MDCE_DRG

def group(record):
  adrg_zd=["J45.000","J45.000x001","J45.000x003","J45.002","J45.003","J45.004","J45.005","J45.006","J45.007","J45.100","J45.100x002","J45.100x003","J45.800","J45.900","J45.900x001","J45.900x002","J45.900x011","J45.900x012","J45.900x013","J45.900x021","J45.900x023","J45.900x031","J45.900x041","J45.901","J45.902","J45.903","J46.x00x002","J46.x00x003","J46.x00x006","J46.x00x008","J46.x00x009","J46.x00x010","J46.x01","J46.x02"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合EX1入组条件，匹配规则：主诊断匹配')
    
    if MDCE_DRG.EX11_group(record):
      return 'EX11'

    if MDCE_DRG.EX13_group(record):
      return 'EX13'

    if MDCE_DRG.EX15_group(record):
      return 'EX15'

    return 'EX1'
  else:
    return ''

