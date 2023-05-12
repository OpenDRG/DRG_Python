from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=["A18.006+M49.0*","A18.007+M49.0*","A18.009+M49.0*","A18.010+M49.0*","A23.901+M49.1*","A23.902+M01.3*","M20.100x002","M40.100","M40.100x051","M40.200x041","M40.200x061","M40.201","M41.101","M41.200","M41.400","M41.400x091","M41.500","M41.501","M41.800","M41.900","M41.900x061","M42.100","M43.006","M43.009","M46.300x061","M46.500x092","M46.501","M47.003+G99.2*","M47.101+G99.2*","M47.201","M47.801","M47.802","M48.002","M48.003","M48.004","M48.005","M48.006","M48.801","M48.808","M50.001+G99.2*","M50.101+G55.1*","M50.201","M51.101+G55.1*","M51.201","M51.202","M51.204","M53.203","M53.205","M53.207","M80.000","M80.801","M80.900","M85.000x084","M89.818","M99.500x003","Q67.501","Q76.300x011","Q76.400x101","S12.200x031","S12.200x041","S13.100x062","S13.103","S22.000x003","S22.000x051","S22.000x061","S22.100","S32.000x002","S32.000x011","S32.000x021","S32.000x031","S32.000x041","S32.000x051","S32.702","T84.200x003"]
  adrg_zd1=[]
  adrg_ss=["81.0200x001","81.0200x002","81.0300x001","81.0401","81.0402","81.0500x005","81.0500x006","81.0501","81.0502","81.0600x005","81.0600x006","81.0601","81.0700x002","81.0701","81.0702","81.0800x016","81.0800x017","81.0800x018","81.0801","81.0802"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合IB2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCI_DRG.IB29_group(record):
      return 'IB29'

    return 'IB2'
  else:
    return ''
