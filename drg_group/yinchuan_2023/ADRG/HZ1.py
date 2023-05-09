from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCH_DRG

def group(record):
  adrg_zd=["A18.814+K77.0*","B25.100+K77.0*","B54.x00","B54.x00x003+K77.0*","B67.000x001+K77.0*","B67.800x001+K77.0*","D13.400","D13.501","D17.700x015","D18.013","D37.600x003","E80.400","E80.602","I77.000x017","I81.x00","I82.000x001","I87.803","K71.600x002","K71.601","K71.900","K71.900x003","K71.901","K72.004","K73.200x002","K75.000","K75.001","K75.003","K75.400","K75.804","K75.901","K76.000","K76.600x007","K76.601","K76.800x006","K76.800x009","K76.800x015","K76.801","K76.803","K76.804","K76.806","K76.807","K76.811","K76.814","K76.816","K76.900x002","K76.901","M35.003+K77.8*","Q27.800x004","Q44.601","Q85.911","R17.900x001","R17.901","R93.200x001","R93.203","R94.500","S36.100x001","S36.100x011","S36.102","T85.800x802"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合HZ1入组条件，匹配规则：主诊断匹配')
    
    if MDCH_DRG.HZ11_group(record):
      return 'HZ11'

    if MDCH_DRG.HZ13_group(record):
      return 'HZ13'

    if MDCH_DRG.HZ15_group(record):
      return 'HZ15'

    return 'HZ1'
  else:
    return ''

