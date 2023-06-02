from drg_group.foshan_2022.Base import message,intersect,has_mcc,has_cc,SS_VALID

def group(record):
  adrg_zd=["Z51.800x095","Z51.800x951","Z51.800x952","Z51.800x981","Z51.801","Z51.805","Z51.807","Z51.810"]
  adrg_zd1=[]
  adrg_ss=["99.2800x006"]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and has_mcc(record.zdList[0],record.zdList[1:]):
    message('符合RG11入组条件，匹配规则：主诊断匹配、主手术匹配、伴严重并发症或合并症')
    return True