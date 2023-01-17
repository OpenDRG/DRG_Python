from drg_group.chs_drg_11.Base import messages,has_mcc,has_cc

def NS19_group(record):
  return True

def ND19_group(record):
  return True

def NJ19_group(record):
  return True

def NG19_group(record):
  return True

def NE19_group(record):
  return True

def NA29_group(record):
  return True

def NA19_group(record):
  return True

def NF19_group(record):
  return True

def NZ19_group(record):
  return True

def NB19_group(record):
  return True

def NC19_group(record):
  return True

def NR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def NR15_group(record):
  return True

