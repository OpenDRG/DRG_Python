from drg_group.foshan_2022.Base import message,intersect,has_mcc,has_cc,SS_VALID

def group(record):
  adrg_zd=["Z51.000x003","Z51.000x008","Z51.000x012","Z51.001","Z51.002","Z51.003"]
  adrg_zd1=[]
  adrg_ss=["92.2400x002","92.2400x003","92.2400x005","92.2400x006","92.2501","92.2700x002","92.2702","92.2703","92.2704","92.2705","92.2706","92.2900x001","92.3101","92.3300","99.2500x036","99.2500x037","99.2500x038","99.2500x039","99.2502","99.2503","99.2504","99.2505","99.2506","99.2800x004","99.2800x005","99.2800x006","99.2801"]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList[1:],adrg_ss):
    message('符合RC11入组条件，匹配规则：主诊断匹配、主手术匹配、其他手术匹配')
    return True