from drg_group.yunnan_2023.Base import message,intersect,SS_VALID
from drg_group.yunnan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["35.0100x002","35.0101","35.0200x003","35.0201","35.0300x002","35.0301","35.0400x001","35.0401","35.0600x001","35.0600x002","35.0800x001","35.1000","35.1100x003","35.1100x004","35.1100x005","35.1101","35.1200x001","35.1200x002","35.1200x003","35.1201","35.1202","35.1300x002","35.1300x004","35.1300x005","35.1301","35.1400x001","35.1400x002","35.1400x003","35.1400x006","35.1401","35.1402","35.2000x001","35.2000x002","35.2000x003","35.2100x002","35.2100x003","35.2100x004","35.2100x005","35.2101","35.2200x002","35.2200x004","35.2201","35.2300x002","35.2301","35.2302","35.2400x002","35.2401","35.2402","35.2500x002","35.2501","35.2600x002","35.2601","35.2701","35.2702","35.2801","35.2802","35.3101","35.3200x003","35.3201","35.3202","35.3300x001","35.3300x002","35.3300x003","35.3500x002","35.3500x003","35.3500x004","35.3500x005","35.3500x006","35.3500x007","35.3500x008","35.3500x009","35.3501","35.9500x001","35.9500x003","35.9500x004","35.9500x005","35.9502","35.9900x001","35.9900x002","37.3300x017","37.3300x026"]
  adrg_ss1=["00.6600x004","00.6601","17.5500x002","17.5500x003","17.5501","36.0300x002","36.0300x003","36.0300x006","36.0301","36.0302","36.0303","36.0400","36.0601","36.0602","36.0700","36.0700x004","36.0701","36.1000x001","36.1000x002","36.1100","36.1200","36.1300","36.1400","36.1500","36.1600","36.1700x001","36.1900x001","36.3400","36.9100","36.9900x002","36.9900x006","36.9900x007","36.9900x008","36.9900x009","36.9900x010","36.9900x011","36.9900x012","36.9900x013","36.9901","36.9902","36.9903","37.1100x005","37.1100x007"]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and intersect(record.ssList,adrg_ss) and intersect(record.ssList,adrg_ss1):
    message('符合FB1入组条件，匹配规则：双手术匹配')
    
    
    if MDCF_DRG.FB19_group(record):
      return 'FB19'

    return ''
  else:
    return ''
