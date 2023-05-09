from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCX_DRG

def group(record):
  adrg_zd=["B90.002","B94.101","I69.400","I69.800x002","I69.802","K07.601","M23.201","M23.203","M23.204","M23.209","M23.215","M24.805","M24.808","Q89.900","T90.500x002","T91.205","T92.000","T92.100x009","T92.100x010","T92.100x011","T92.103","T92.104","T92.105","T92.106","T92.201","T92.202","T92.203","T92.204","T92.300","T92.300x002","T92.300x012","T92.301","T92.303","T92.400","T92.500x001","T92.500x004","T92.500x006","T92.500x009","T92.500x011","T92.500x016","T92.501","T92.800x002","T92.900","T93.100","T93.101","T93.102","T93.104","T93.200","T93.200x002","T93.200x007","T93.200x008","T93.200x010","T93.200x013","T93.201","T93.202","T93.203","T93.205","T93.206","T93.207","T93.208","T93.301","T93.400x002","T93.400x004","T93.500x002","T93.800","T94.002","Z50.101","Z50.801","Z54.800x004"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合XR2入组条件，匹配规则：主诊断匹配')
    
    if MDCX_DRG.XR21_group(record):
      return 'XR21'

    if MDCX_DRG.XR23_group(record):
      return 'XR23'

    if MDCX_DRG.XR25_group(record):
      return 'XR25'

    return 'XR2'
  else:
    return ''

