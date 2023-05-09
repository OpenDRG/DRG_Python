from drg_group.liaocheng_2022.Base import has_mcc,has_cc,intersect
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
def NZ19_group(record):
  return True
def NA11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def NS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def NA13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NA15_group(record):
  return True
def NR15_group(record):
  return True
def NS15_group(record):
  return True

