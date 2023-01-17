from drg_group.suzhou_2022.Base import messages,has_mcc,has_cc

def PB19_group(record):
  return True

def PR19_group(record):
  return True

def PS19_group(record):
  return True

def PK19_group(record):
  return True

def PC19_group(record):
  return True

def PJ19_group(record):
  return True

def PV19_group(record):
  return True

def PU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def PS21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def PS31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def PS41_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def PU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def PS4B_group(record):
  return True

def PS2B_group(record):
  return True

def PS3B_group(record):
  return True

def PU15_group(record):
  return True

