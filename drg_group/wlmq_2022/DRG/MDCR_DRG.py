from drg_group.wlmq_2022.Base import has_mcc,has_cc,intersect
def RA19_group(record):
  return True
def RA39_group(record):
  return True
def RA49_group(record):
  return True
def RB19_group(record):
  return True
def RD19_group(record):
  return True
def RE19_group(record):
  return True
def RG19_group(record):
  return True
def RS29_group(record):
  return True
def RT29_group(record):
  return True
def RW19_group(record):
  return True
def RW29_group(record):
  return True
def RA21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RB21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RC11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def RT13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def RU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def RV13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def RA25_group(record):
  return True
def RB25_group(record):
  return True
def RC15_group(record):
  return True
def RR15_group(record):
  return True
def RS15_group(record):
  return True
def RT15_group(record):
  return True
def RU15_group(record):
  return True
def RV15_group(record):
  return True

