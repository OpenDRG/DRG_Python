from drg_group.yinchuan_2023.Base import has_mcc,has_cc,intersect
def NA29_group(record):
  return True
def NB19_group(record):
  return True
def NC19_group(record):
  return True
def ND19_group(record):
  return True
def NE19_group(record):
  return True
def NF19_group(record):
  return True
def NJ19_group(record):
  return True
def NS19_group(record):
  return True
def NZ19_group(record):
  return True
def NR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def NR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NR15_group(record):
  return True

