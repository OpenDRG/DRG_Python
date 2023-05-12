from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCE_DRG

def group(record):
  adrg_zd=["J39.801","J39.802","J39.803","J39.804","J39.805","J39.806","J42.x00","J42.x00x001","J42.x00x003","J42.x00x004","J42.x00x005","J42.x00x006","J42.x01","J43.000","J43.000x003","J43.001","J43.100","J43.101","J43.200","J43.800x001","J43.900","J43.900x001","J43.901","J43.902","J43.903","J43.904","J44.000","J44.100","J44.800x001","J44.801","J44.802","J44.803","J44.805","J44.806","J44.807","J44.900","J44.900x002","J44.900x003","J44.900x004","J44.900x005","J47.x00","J47.x01","J47.x02","J47.x03","J98.200","J98.300"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and (not record.ssList or not record.ssList[0] in SS_VALID):
    message('符合ET2入组条件，匹配规则：主诊断匹配')
    
    if MDCE_DRG.ET21_group(record):
      return 'ET21'

    if MDCE_DRG.ET23_group(record):
      return 'ET23'

    if MDCE_DRG.ET25_group(record):
      return 'ET25'

    return ''
  else:
    return ''

