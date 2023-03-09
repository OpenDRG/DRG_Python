from drg_group.lanzhou_2022.Base import has_mcc,has_cc,intersect
def TB19_group(record):
  return True
def TR29_group(record):
  return True
def TS19_group(record):
  return True
def TT29_group(record):
  return True
def TU19_group(record):
  return True
def TV19_group(record):
  return True
def TW11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def TR1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def TS2A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def TT1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def TW13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def TR15_group(record):
  return True
def TS25_group(record):
  return True
def TT15_group(record):
  return True
def TW15_group(record):
  return True

