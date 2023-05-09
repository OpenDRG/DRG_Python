from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCL_DRG

def group(record):
  adrg_zd=["D69.005+N08.2*","E10.200x214+N08.3*","E10.200x215+N08.3*","E11.200x031+N29.8*","E11.200x214+N08.3*","E11.200x215+N08.3*","E11.201+N08.3*","E14.200x215+N08.3*","I12.000x001","I13.100x001","M31.701+N08.5*","M32.101+N08.5*","N02.801","N03.900","N03.900x007","N03.901","N04.900","N13.203","N13.301","N17.800","N17.900","N18.200","N18.300","N18.400","N18.500","N18.902","N28.900x017","Q61.300","Z45.800x007","Z46.800x001","Z46.800x002","Z49.000x002","Z49.000x004","Z49.101","Z49.201"]
  adrg_zd1=[]
  adrg_ss=["38.0300x003","38.9501","38.9502","39.2700x001","39.2700x002","39.2700x003","39.4200x001","39.4200x002","39.4200x004","39.5000x032","54.9300x003","54.9300x004","54.9300x006","54.9300x007","54.9300x011","54.9300x012","97.8600x007","97.8600x008","97.8600x009","97.8601","97.8900x004","97.8900x005"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合LF1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCL_DRG.LF11_group(record):
      return 'LF11'

    if MDCL_DRG.LF13_group(record):
      return 'LF13'

    if MDCL_DRG.LF15_group(record):
      return 'LF15'

    return 'LF1'
  else:
    return ''

