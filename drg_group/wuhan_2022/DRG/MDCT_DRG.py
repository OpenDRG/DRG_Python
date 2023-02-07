from drg_group.wuhan_2022.Base import messages,has_mcc,has_cc,intersect
def TT29_group(record):
  return True
def TB19_group(record):
  return True
def TV19_group(record):
  return True
def TR19_group(record):
  return True
def TT19_group(record):
  return True
def TS19_group(record):
  return True
def TR29_group(record):
  return True
def TU19_group(record):
  return True
def TS21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def TW1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def TS23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def TS25_group(record):
  return True
def TW15_group(record):
  return True

