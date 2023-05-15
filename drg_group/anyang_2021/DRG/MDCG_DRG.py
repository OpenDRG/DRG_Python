from drg_group.anyang_2021.Base import has_mcc,has_cc,intersect
def GE29_group(record):
  return True
def GB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GC11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GD11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GK21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GU21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GD2A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GF1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GK1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GK3A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GT1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GZ1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GC13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GD13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GK23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GU23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GV13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GB1B_group(record):
  return True
def GR1B_group(record):
  return True
def GC15_group(record):
  return True
def GD15_group(record):
  return True
def GD25_group(record):
  return True
def GF15_group(record):
  return True
def GK15_group(record):
  return True
def GK25_group(record):
  return True
def GK35_group(record):
  return True
def GS15_group(record):
  return True
def GT15_group(record):
  return True
def GU15_group(record):
  return True
def GU25_group(record):
  return True
def GV15_group(record):
  return True
def GZ15_group(record):
  return True
def GC21A_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:]) and record.age<=14
def GF21A_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:]) and record.age<=14
def GG11A_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:]) and record.age<=14
def GJ11A_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:]) and record.age<=14
def GE1AA_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:])) and record.age<=14
def GW1AA_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:])) and record.age<=14
def GC23A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:])) and record.age<=14
def GF23A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:])) and record.age<=14
def GG13A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:])) and record.age<=14
def GJ13A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:])) and record.age<=14
def GC25A_group(record):
  return record.age<=14
def GE15A_group(record):
  return record.age<=14
def GF25A_group(record):
  return record.age<=14
def GG15A_group(record):
  return record.age<=14
def GJ15A_group(record):
  return record.age<=14
def GW15A_group(record):
  return record.age<=14
def GB29A_group(record):
  return record.age<=14
def GC21B_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:]) and record.age>14
def GF21B_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:]) and record.age>14
def GG11B_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:]) and record.age>14
def GJ11B_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:]) and record.age>14
def GE1AB_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:])) and record.age>14
def GW1AB_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:])) and record.age>14
def GC23B_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:])) and record.age>14
def GF23B_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:])) and record.age>14
def GG13B_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:])) and record.age>14
def GJ13B_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:])) and record.age>14
def GC25B_group(record):
  return record.age>14
def GE15B_group(record):
  return record.age>14
def GF25B_group(record):
  return record.age>14
def GG15B_group(record):
  return record.age>14
def GJ15B_group(record):
  return record.age>14
def GW15B_group(record):
  return record.age>14
def GB29B_group(record):
  return record.age>14

