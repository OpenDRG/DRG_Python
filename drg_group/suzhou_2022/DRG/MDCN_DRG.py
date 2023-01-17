from drg_group.suzhou_2022.Base import messages,has_mcc,has_cc

def NF19_group(record):
  return True

def NE19_group(record):
  return True

def NB19_group(record):
  return True

def NA29_group(record):
  return True

def NZ19_group(record):
  return True

def NA19_group(record):
  return True

def NG19_group(record):
  return True

def NC19_group(record):
  return True

def ND19_group(record):
  return True

def NR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def NJ1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def NS1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def NR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def NR15_group(record):
  return True

def NS15_group(record):
  return True

def NJ15_group(record):
  return True

