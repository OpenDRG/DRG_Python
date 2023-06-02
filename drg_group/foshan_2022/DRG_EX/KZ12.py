from drg_group.foshan_2022.Base import message,intersect,has_mcc,has_cc,SS_VALID

def group(record):
  adrg_zd=["E10.500x021+I79.2*","E10.500x044","E10.500x045","E10.500x046","E10.500x047","E10.500x048","E10.500x049","E10.503","E10.505","E10.600x910","E10.600x911","E10.600x920","E10.600x930","E10.700x031","E10.700x032","E11.500x044","E11.500x045","E11.500x046","E11.500x047","E11.500x048","E11.500x049","E11.503","E11.505","E11.600x910","E11.600x911","E11.600x920","E11.600x930","E11.700x031","E11.700x032","E14.500x021+I79.2*","E14.500x042","E14.500x044","E14.500x045","E14.500x046","E14.500x047","E14.500x048","E14.500x049","E14.500x050","E14.600x910","E14.600x911","E14.600x920","E14.600x930","E14.700x031","E14.700x032","E66.200"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.zdList[0] in adrg_zd and has_cc(record.zdList[0],record.zdList[1:]):
    message('符合KZ12入组条件，匹配规则：主诊断匹配、伴一般并发症或合并症')
    return True