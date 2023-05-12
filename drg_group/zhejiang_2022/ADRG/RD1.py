from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCR_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["07.2101","32.2004","32.2400x001","32.2500x001","32.2900x005","39.7100x004","39.7200x005","39.7900x011","39.7900x013","39.7900x017","39.7900x019","39.7900x020","39.7900x021","39.7900x025","39.7902","39.7903","39.7904","39.7906","41.4200x003","44.4400x004","44.4400x005","44.4403","50.2301","50.2302","50.2303","50.2401","50.2402","50.2403","50.2404","50.2501","50.2502","50.2503","50.2902","50.9300","52.2202","54.4x00x039","54.4x00x048","68.2500x001","99.2500x017","99.2501","99.2502"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合RD1入组条件，匹配规则：主手术匹配')
    
    if MDCR_DRG.RD11_group(record):
      return 'RD11'

    if MDCR_DRG.RD13_group(record):
      return 'RD13'

    if MDCR_DRG.RD15_group(record):
      return 'RD15'

    return ''
  else:
    return ''

