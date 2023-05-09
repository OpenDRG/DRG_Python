from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCJ_DRG

def group(record):
  adrg_zd=["S20.200","S20.201","S20.801","S20.802","S30.000x001","S30.000x003","S30.001","S30.002","S30.003","S30.800x001","S30.900x003","S31.001","S39.910","S40.000x001","S40.001","S50.101","S50.800x041","S50.800x081","S60.100x001","S60.201","S60.202","S60.800x043","S60.801","S60.900x002","S60.901","S70.000","S70.100","S70.800x032","S70.900x001","S70.901","S80.000","S80.100x002","S80.101","S80.800x011","S80.800x041","S80.901","S90.000","S90.100","S90.300x001","S90.300x002","S90.301","S90.700","S90.800x043","T00.600x001","T00.900","T00.900x005","T00.901","T01.301","T11.000x041","T11.001","T11.101","T13.000x041","T14.000","T14.000x031","T14.001","T14.003","T14.101"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合JT1入组条件，匹配规则：主诊断匹配')
    
    if MDCJ_DRG.JT19_group(record):
      return 'JT19'

    return 'JT1'
  else:
    return ''

