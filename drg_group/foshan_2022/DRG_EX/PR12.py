from drg_group.foshan_2022.Base import message,intersect,has_mcc,has_cc,SS_VALID

def group(record):
  adrg_zd=["P22.000","P22.000x001","P22.100x003","P22.801","P22.900"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.zdList[0] in adrg_zd and record.ageDay!=None and record.ageDay<=28:
    message('符合PR12入组条件，匹配规则：主诊断匹配、新生儿')
    return True