from drg_group.lanzhou_2022.Base import has_mcc,has_cc,intersect
def PB19_group(record):
  return True
def PC19_group(record):
  return True
def PJ19_group(record):
  return True
def PS19_group(record):
  return True
def PS39_group(record):
  return True
def PK11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PS21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PS4A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def PV1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def PU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def PK1B_group(record):
  return True
def PR1B_group(record):
  return True
def PS2B_group(record):
  return True
def PS45_group(record):
  return True
def PU15_group(record):
  return True
def PV15_group(record):
  return True

