from drg_group.yancheng_2023.Base import message,intersect,SS_VALID
from drg_group.yancheng_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=["C40.000x006","C40.001","C40.002","C40.003","C40.004","C40.005","C40.100x006","C40.100x007","C40.101","C40.102","C40.103","C40.200x005","C40.201","C40.202","C40.203","C40.300x003","C40.300x004","C40.300x005","C40.300x009","C40.300x010","C40.300x011","C40.301","C40.302","C40.303","C40.304","C40.800","C40.900x001","C40.901","C41.100x002","C41.200x005","C41.201","C41.202","C41.203","C41.300x002","C41.301","C41.302","C41.400x008","C41.400x009","C41.401","C41.402","C41.403","C41.404","C41.405","C41.406","C41.800","C41.800x001","C41.900x001","C41.901","C49.100x001","C49.100x002","C49.100x006","C49.101","C49.102","C49.103","C49.200x001","C49.200x002","C49.200x005","C49.200x006","C49.201","C49.202","C49.300x002","C49.301","C49.400","C49.400x003","C49.401","C49.500","C49.500x001","C49.500x008","C49.501","C49.502","C49.503","C49.504","C49.505","C49.600","C49.601","C49.800","C49.900x003","C79.500x001","C79.500x006","C79.500x008","C79.500x009","C79.500x010","C79.500x011","C79.500x012","C79.500x013","C79.500x021","C79.500x022","C79.500x024","C79.500x025","C79.500x026","C79.500x030","C79.500x031","C79.500x032","C79.501","C79.506","C79.507","C79.508","C79.509","C79.800x835","C79.800x836","C79.800x847","D36.105","D48.000x001","D48.000x004","D48.000x028","D48.001","D48.002","D48.003","D48.004","D48.005","D48.006","D48.007","D48.008","D48.009","D48.010","D48.011","D48.012","D48.013","D48.014","D48.015","D48.016","D48.017","D48.018","D48.019","D48.020","D48.021","D48.022","D48.023","D48.100x003","D48.100x006","D48.100x007","D48.100x009","D48.100x018","D48.100x020","D48.100x021","D48.100x025","D48.101","D48.102","D48.103","D48.104","D48.105","D48.106","D48.107","D48.108","D48.109","D48.110","D48.111","D48.112","D48.114","D48.116","D48.118","D48.120","D48.122","D48.124","D48.126","D48.128","D48.130","D48.132","D48.134","D48.903+M90.7*","M48.401","M80.000","M80.100","M80.200","M80.300","M80.400","M80.500","M80.800","M80.801","M80.900","M84.300x091","M84.301"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合IU3入组条件，匹配规则：主诊断匹配')
    
    if MDCI_DRG.IU31_group(record):
      return 'IU31'

    if MDCI_DRG.IU35_group(record):
      return 'IU35'

    return 'IU3'
  else:
    return ''
