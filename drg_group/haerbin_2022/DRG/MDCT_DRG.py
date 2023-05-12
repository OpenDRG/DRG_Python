from drg_group.haerbin_2022.Base import has_mcc,has_cc,intersect
def TR19_group(record):
  return True
def TR29_group(record):
  return True
def TS19_group(record):
  return True
def TT19_group(record):
  return True
def TT29_group(record):
  return True
def TU19_group(record):
  return True
def TV19_group(record):
  return True
def TW19_group(record):
  return True
def TB1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def TS2A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def TB15_group(record):
  return True
def TS25_group(record):
  return True

