from drg_group.foshan_2022.Base import has_mcc,has_cc,intersect
def PK10_group(record):
    return record.icuHours>120
def PS10_group(record):
    return record.icuHours>120
def PS12_group(record):
  return 1<=record.icuHours<=120
def PB19_group(record):
  return True
def PC19_group(record):
  return True
def PJ19_group(record):
  return True
def PS49_group(record):
  return True
def PS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PS21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PS31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PS13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def PU13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def PV13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def PS23_group(record):
  return True
def PS33_group(record):
  return True
def PS15_group(record):
  return True
def PU15_group(record):
  return True
def PV15_group(record):
  return True

