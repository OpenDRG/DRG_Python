from drg_group.suzhou_2023.Base import messages,has_mcc,has_cc

def WJ19_group(record):
  return True

def WR19_group(record):
  return True

def WB19_group(record):
  return True

def WC19_group(record):
  return True

def WZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def WZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def WZ15_group(record):
  return True

