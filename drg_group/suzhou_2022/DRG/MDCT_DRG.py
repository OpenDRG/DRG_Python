from drg_group.suzhou_2022.Base import messages,has_mcc,has_cc

def TR19_group(record):
  return True

def TV19_group(record):
  return True

def TS19_group(record):
  return True

def TR29_group(record):
  return True

def TU19_group(record):
  return True

def TT29_group(record):
  return True

def TW11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def TS2A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def TT1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def TB1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def TW13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def TW15_group(record):
  return True

def TT15_group(record):
  return True

def TB15_group(record):
  return True

def TS25_group(record):
  return True

