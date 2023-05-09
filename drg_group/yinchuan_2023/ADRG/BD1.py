from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["B02.202+G53.0*","C72.000","C72.001","C72.900x004","D18.000x024","D32.100x001","D32.102","D32.103","D32.104","D33.400","D33.401","D33.402","D33.403","D33.902","D36.100x053","D36.100x057","D36.109","G06.100x002","G44.100x004","G57.000","G58.001","G83.400","G83.802","G93.000x002","G95.108","G95.200","G95.800x010","G95.900x003","I61.802","I62.101","I77.002","M51.003+G99.2*","Q06.801","Q27.801","Q85.900x052","R26.802","S14.100x021","S14.101","T09.300"]
  adrg_zd1=[]
  adrg_ss=["03.0100x001","03.0900x003","03.0900x004","03.0900x006","03.0900x007","03.0900x009","03.0900x010","03.0900x019","03.0901","03.0909","03.0911","03.0912","03.3100x001","03.4x00x001","03.4x00x008","03.4x01","03.4x03","03.4x04","03.4x05","03.4x06","03.4x07","03.5900x005","03.6x00x011","03.6x02","03.7100","04.2x04","04.2x05","38.6100x001"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合BD1入组条件，匹配规则：主诊断匹配、某一手术匹配')
    
    if MDCB_DRG.BD11_group(record):
      return 'BD11'

    if MDCB_DRG.BD13_group(record):
      return 'BD13'

    if MDCB_DRG.BD15_group(record):
      return 'BD15'

    return 'BD1'
  else:
    return ''

