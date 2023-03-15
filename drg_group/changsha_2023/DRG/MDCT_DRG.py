from drg_group.changsha_2023.Base import has_mcc,has_cc,intersect
def TR29_group(record):
  return True
def TS19_group(record):
  return True
def TV19_group(record):
  return True
def TU1A_CS_group(record):
  return int(record.age)<=6
def TU1B_CS_group(record):
  return True
def TB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def TR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def TS21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def TT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def TW11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def TB13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def TT23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def TW13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def TB15_group(record):
  return True
def TR15_group(record):
  return True
def TS25_group(record):
  return True
def TT15_group(record):
  return True
def TT25_group(record):
  return True
def TW15_group(record):
  return True

