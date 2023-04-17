from drg_group.suzhou_2023.Base import messages,has_mcc,has_cc

def ZD19_group(record):
  return True

def ZB19_group(record):
  return True

def ZJ19_group(record):
  return True

def ZC19_group(record):
  return True

def ZZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def ZZ1B_group(record):
  return True

