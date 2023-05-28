from drg_group.hefei_2023.Base import message,intersect,SS_VALID

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["42.4000","42.4203","42.4201","42.4200.42.4200x001","42.4202","42.4202x002","42.4100"]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合GB1Z入组条件，匹配规则：主手术匹配、某一手术匹配')
    return True