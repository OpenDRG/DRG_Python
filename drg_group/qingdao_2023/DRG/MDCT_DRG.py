from drg_group.qingdao_2023.Base import has_mcc,has_cc,intersect
def TB19_group(record):
  return True
def TR19_group(record):
  return True
def TR29_group(record):
  return True
def TT19_group(record):
  return True
def TT29_group(record):
  return True
def TU19_group(record):
  return True
def TW19_group(record):
  return True
def TS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def TS23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def TV13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def TS15_group(record):
  return True
def TS25_group(record):
  return True
def TV15_group(record):
  return True

