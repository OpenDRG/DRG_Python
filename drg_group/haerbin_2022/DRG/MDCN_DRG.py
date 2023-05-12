from drg_group.haerbin_2022.Base import has_mcc,has_cc,intersect
def NA19_group(record):
  return True
def NA29_group(record):
  return True
def NB19_group(record):
  return True
def NC19_group(record):
  return True
def ND19_group(record):
  return True
def NF19_group(record):
  return True
def NG19_group(record):
  return True
def NS19_group(record):
  return True
def NE11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def NZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def NJ1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NR1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NE1B_group(record):
  return True
def NZ1B_group(record):
  return True
def NJ15_group(record):
  return True
def NR15_group(record):
  return True

