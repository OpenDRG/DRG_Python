from drg_group.yunnan_2022.Base import message,intersect,SS_VALID
from drg_group.yunnan_2022.DRG import MDCL_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["38.3701","55.9200x002","55.9200x006","55.9201","55.9202","55.9203","55.9204","55.9205","55.9206","55.9300","55.9300x001","55.9400","55.9500","55.9601","56.3300x001","57.0x01","57.1101","57.1700x001","57.1701","57.1800x001","57.3300","58.2300","59.0000","59.0301","59.0302","59.1902","59.2101","59.2102","59.8x02","59.9201","59.9300","59.9400","59.9501","59.9502","98.5101","98.5102","98.5103","98.5104"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合LJ1入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if MDCL_DRG.LJ11_group(record):
      return 'LJ11'

    if MDCL_DRG.LJ15_group(record):
      return 'LJ15'

    return 'LJ1'
  else:
    return ''

