from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCJ_DRG

def group(record):
  adrg_zd=["D17.000x004","D17.100x001","D17.100x002","D17.100x003","D17.101","D17.200x001","D17.200x002","D17.200x003","D17.200x004","D17.200x005","D17.300x001","D17.300x002","D17.300x004","D17.300x005","D17.500x010","D17.500x011","D17.900x001","D17.900x002","D18.000x010","D18.000x018","D18.000x847","D18.000x848","D18.000x849","D18.000x850","D18.000x851","D18.000x852","D18.005","D18.006","D18.007","D22.500","D22.511","D22.600","D22.601","D22.700","D22.900","D22.900x002","D23.400x003","D23.401","D23.500","D23.501","D23.504","D23.506","D23.600x001","D23.602","D23.700x001","D23.900","D36.700x009","D48.503","D48.515","L90.500x009","L90.500x026","L90.500x029","L90.500x030","L90.500x040","L90.500x043","L90.500x045","L90.500x048","L90.500x052","L90.500x055","L90.500x058","L90.500x060","L90.500x062","L90.500x063","L90.502","L90.503","L90.505","L91.001","L91.801","L92.200","L92.800","L92.901","L92.903","M79.801","M79.802","M79.804","M79.806","M79.811","R22.000x005","R22.002","R22.003","R22.004","R22.005","R22.006","R22.100x001","R22.100x002","R22.200x004","R22.202","R22.203","R22.204","R22.205","R22.206","R22.207","R22.300x001","R22.300x002","R22.302","R22.400x002","R22.400x003","R22.402","R22.902","R22.903","R22.904"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合JV1入组条件，匹配规则：主诊断匹配')
    
    if MDCJ_DRG.JV19_group(record):
      return 'JV19'

    return 'JV1'
  else:
    return ''

