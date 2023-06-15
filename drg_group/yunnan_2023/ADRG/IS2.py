from drg_group.yunnan_2023.Base import message,intersect,SS_VALID
from drg_group.yunnan_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=["M22.000","M22.100","M22.200x001","M22.201","M22.300x001","M22.301","M22.400","M22.801","M22.802","M23.000x031","M23.000x061","M23.001","M23.100","M23.300x061","M23.300x062","M23.301","M23.302","M23.303","M23.304","M23.305","M23.306","M23.307","M23.308","M23.309","M23.310","M23.311","M23.500x091","M23.800x001","M23.801","M23.802","M23.803","M23.804","M23.805","M23.806","M23.807","M23.808","M23.809","M23.810","M23.811","M23.812","M23.900","M24.101","M24.300x091","M24.303","M24.305","M24.306","M24.307","M24.308","M24.311","M24.401","M24.402","M24.403","M24.404","M24.405","M24.406","M24.409","M24.410","M24.411","M24.412","M24.414","M24.415","M24.416","M24.417","M84.000x062","M84.000x063","M84.100x012","M84.100x062","M84.100x063","M84.100x073","M84.100x074","M89.201","M89.202","M94.000","M94.001","S22.800","S22.810","S23.400","S23.401","S23.500","S23.501","S33.200x001","S33.200x002","S33.200x003","S33.300x001","S33.300x004","S33.400","S33.600x001","S33.700x001","S39.000x002","S39.000x004","S39.000x006","S42.000","S42.000x011","S42.000x021","S42.000x031","S42.000x091","S42.010","S42.100","S42.100x011","S42.100x021","S42.100x031","S42.100x041","S42.100x042","S42.100x091","S42.110","S42.200x001","S42.200x011","S42.200x031","S42.200x041","S42.200x091","S42.200x092","S42.202","S42.203","S42.210","S42.300","S42.300x002","S42.301","S42.310","S42.311","S42.400x001","S42.400x041","S42.400x042","S42.400x043","S42.400x051","S42.400x091","S42.400x092","S42.400x093","S42.401","S42.402","S42.403","S42.404","S42.410","S42.700","S42.710","S42.900","S42.910","S43.000","S43.000x011","S43.000x021","S43.000x031","S43.001","S43.002","S43.100","S43.301","S43.302","S43.400x001","S43.400x002","S43.400x003","S43.400x004","S43.400x005","S43.401","S43.500","S43.500x001","S43.500x002","S43.501","S43.600","S43.601","S43.700","S43.701","S46.000","S46.000x001","S46.002","S46.100x001","S46.100x003","S46.101","S46.200x001","S46.200x002","S46.200x003","S46.201","S46.300x001","S46.300x002","S46.300x003","S46.301","S46.700x001","S46.700x002","S46.701","S46.702","S46.800x001","S46.800x002","S46.800x003","S46.800x004","S46.800x005","S46.800x006","S46.800x007","S46.801","S46.802","S46.900x001","S46.900x002","S49.700","S49.800","S49.901","S52.000x001","S52.001","S52.002","S52.011","S52.813","S53.100","S53.100x011","S53.100x021","S53.100x031","S53.100x041","S53.101","S53.102","S53.400","S53.400x002","S71.101","S72.710","S73.000","S73.000x003","S73.000x011","S73.000x021","S73.001","S73.100","S73.100x002","S73.100x011","S73.100x021","S73.101","S76.000x002","S76.000x003","S76.100x001","S76.100x002","S76.100x003","S76.100x004","S76.101","S76.102","S76.200x002","S76.200x003","S76.300x001","S76.300x002","S76.301","S76.401","S76.402","S76.700x001","S79.700","S79.701","S79.901","S79.902","S81.901","S82.000","S82.000x002","S82.000x004","S82.010","S82.100x011","S82.100x012","S82.100x081","S82.100x082","S82.100x084","S82.100x085","S82.100x086","S82.100x087","S82.100x088","S82.100x089","S82.101","S82.102","S82.110","S82.111","S82.200x011","S82.200x081","S82.201","S82.202","S82.203","S82.210","S82.211","S82.212","S82.300x011","S82.300x012","S82.300x081","S82.300x082","S82.300x083","S82.301","S82.310","S82.311","S82.400x001","S82.400x002","S82.400x011","S82.400x012","S82.400x013","S82.400x014","S82.400x091","S82.401","S82.410","S82.411","S82.500","S82.500x001","S82.501","S82.510","S82.600","S82.600x001","S82.601","S82.610","S82.700","S82.710","S82.800x081","S82.800x082","S82.801","S82.802","S82.803","S82.810","S82.811","S82.812","S82.900","S82.910","S83.000","S83.001","S83.100","S83.100x011","S83.100x012","S83.100x021","S83.100x031","S83.100x041","S83.100x081","S83.101","S83.102","S83.200x001","S83.200x002","S83.200x003","S83.200x004","S83.200x005","S83.200x006","S83.201","S83.202","S83.300x001","S83.400x001","S83.400x002","S83.400x003","S83.400x011","S83.400x012","S83.400x021","S83.400x022","S83.400x031","S83.400x032","S83.400x041","S83.400x042","S83.401","S83.500x001","S83.500x002","S83.500x003","S83.500x011","S83.500x012","S83.500x021","S83.500x022","S83.500x031","S83.500x032","S83.500x041","S83.500x042","S83.501","S83.600x002","S83.600x003","S83.600x004","S83.600x005","S83.600x006","S83.600x007","S83.601","S83.602","S83.603","S83.700x001","S83.700x002","S83.700x003","S83.700x004","S83.700x005","S83.700x006","S86.100x001","S86.100x002","S86.100x003","S86.200x002","S86.201","S86.300x001","S86.300x002","S86.300x003","S86.300x004","S86.300x005","S86.300x006","S86.301","S86.700x001","S86.700x002","S86.701","S86.800","S86.901","S89.700","S89.800","S89.900","S91.300x811","S91.300x821","S92.100","S92.101","S92.110","S93.000","S93.000x004","S93.000x005","S93.001","S93.002","S93.003","S93.200x001","S93.200x002","S93.200x004","S93.200x005","S93.400","S93.400x002","S93.400x003","S93.400x004","S93.400x012","S93.400x021","S93.400x022","S93.400x031","S93.400x032","S93.401","S93.402","S93.403","S93.404","S93.405","T02.200x001","T02.210","T02.300x001","T02.310","T02.800x001","T02.810","T03.200x003","T09.200x005","T09.200x008","T10.x00","T10.x10","T11.102","T11.200x005","T11.200x006","T11.200x008","T11.200x009","T11.500","T11.500x002","T11.500x003","T11.800","T11.900","T12.x00","T12.x10","T13.001","T13.100x003","T13.100x004","T13.101","T13.200x002","T13.200x003","T13.200x005","T13.200x006","T13.200x007","T13.200x008","T13.200x009","T13.201","T13.202","T13.203","T13.501","T13.502","T13.800","T13.900"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合IS2入组条件，匹配规则：主诊断匹配')
    
    
    if MDCI_DRG.IS23_group(record):
      return 'IS23'

    if MDCI_DRG.IS25_group(record):
      return 'IS25'

    return ''
  else:
    return ''
