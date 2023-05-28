from drg_group.foshan_2022.Base import has_mcc,has_cc,intersect
def GC10_group(record):
    return record.icuHours>120
def GC12_group(record):
  return 1<=record.icuHours<=120
def GW16_group(record):
  return record.age<17 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GE15_group(record):
  return record.age<17
def GW17_group(record):
  return record.age<17
def GE29_group(record):
  return True
def GG19_group(record):
  return True
def GK19_group(record):
  return True
def GB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GB21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GC11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GC21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GD11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GD21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GE12_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GF21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GK21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GU21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GW11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def GF13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GK33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def GB13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def GB23_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def GC13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def GC23_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def GD13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def GD23_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def GE13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def GJ13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def GK23_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def GR13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def GS13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def GT13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def GU23_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def GV13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def GW13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def GZ13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def GF23_group(record):
  return True
def GU13_group(record):
  return True
def GB15_group(record):
  return True
def GB25_group(record):
  return True
def GC15_group(record):
  return True
def GC25_group(record):
  return True
def GD15_group(record):
  return True
def GD25_group(record):
  return True
def GE14_group(record):
  return True
def GF15_group(record):
  return True
def GJ15_group(record):
  return True
def GK25_group(record):
  return True
def GK35_group(record):
  return True
def GR15_group(record):
  return True
def GS15_group(record):
  return True
def GT15_group(record):
  return True
def GU25_group(record):
  return True
def GV15_group(record):
  return True
def GW15_group(record):
  return True
def GZ15_group(record):
  return True

