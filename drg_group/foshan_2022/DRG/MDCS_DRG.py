from drg_group.foshan_2022.Base import has_mcc,has_cc,intersect
def ST16_group(record):
    return record.inHospitalTime>12
def SB10_group(record):
    return record.icuHours>120
def SR10_group(record):
    return record.icuHours>120
def SB12_group(record):
  return 1<=record.icuHours<=120
def SR12_group(record):
  return 1<=record.icuHours<=120
def SU16_group(record):
  return record.age<17 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def SR16_group(record):
  return record.age<17 and has_mcc(record.zdList[0],record.zdList[1:])
def SR17_group(record):
  return record.age<17 and has_cc(record.zdList[0],record.zdList[1:])
def SR18_group(record):
  return record.age<17
def SU17_group(record):
  return record.age<17
def SB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def SR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def SS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ST11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def SV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def SZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def SU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def SB13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def SR13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def SS13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def ST13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def SV13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def SZ13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def SB15_group(record):
  return True
def SR15_group(record):
  return True
def SS15_group(record):
  return True
def ST15_group(record):
  return True
def SU15_group(record):
  return True
def SV15_group(record):
  return True
def SZ15_group(record):
  return True

