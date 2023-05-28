from drg_group.hefei_2023.Base import has_mcc,has_cc,intersect
def TB19_group(record):
  return True
def TR29_group(record):
  return True
def TS19_group(record):
  return True
def TS29_group(record):
  return True
def TU19_group(record):
  return True
def TV19_group(record):
  return True
def TR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def TW11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def TR13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def TT13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def TT23_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def TW13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def TR15_group(record):
  return True
def TT15_group(record):
  return True
def TT25_group(record):
  return True
def TW15_group(record):
  return True

