from drg_group.linfen_2022.Base import has_mcc,has_cc,intersect
def TB19_group(record):
  return True
def TR19_group(record):
  return True
def TR29_group(record):
  return True
def TS19_group(record):
  return True
def TS29_group(record):
  return True
def TT19_group(record):
  return True
def TT29_group(record):
  return True
def TU19_group(record):
  return True
def TV19_group(record):
  return True
def TW13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def TW15_group(record):
  return True

