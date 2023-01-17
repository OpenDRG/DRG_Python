from drg_group.suzhou_2022.Base import messages,has_mcc,has_cc

def GF19_group(record):
  return True

def GT19_group(record):
  return True

def GF29_group(record):
  return True

def GK19_group(record):
  return True

def GZ19_group(record):
  return True

def GE29_group(record):
  return True

def GR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def GU21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def GD21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def GK21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def GJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def GU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def GV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def GB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def GC11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def GC21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def GB21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def GD1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def GW1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def GK3A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def GS1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def GE1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def GG1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def GR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def GK23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def GC23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def GV13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def GJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def GC13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def GU23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def GU1B_group(record):
  return True

def GD2B_group(record):
  return True

def GB2B_group(record):
  return True

def GB1B_group(record):
  return True

def GC15_group(record):
  return True

def GU25_group(record):
  return True

def GD15_group(record):
  return True

def GK25_group(record):
  return True

def GW15_group(record):
  return True

def GK35_group(record):
  return True

def GE15_group(record):
  return True

def GV15_group(record):
  return True

def GC25_group(record):
  return True

def GJ15_group(record):
  return True

def GG15_group(record):
  return True

def GS15_group(record):
  return True

def GR15_group(record):
  return True

