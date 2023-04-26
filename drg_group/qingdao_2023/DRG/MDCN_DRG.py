from drg_group.qingdao_2023.Base import has_mcc,has_cc,intersect
def NA19_group(record):
  return True
def NB19_group(record):
  return True
def NC19_group(record):
  return True
def ND19_group(record):
  return True
def NE19_group(record):
  return True
def NS19_group(record):
  return True
def NR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def NA23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NF13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NA25_group(record):
  return True
def NF15_group(record):
  return True
def NJ15_group(record):
  return True
def NR15_group(record):
  return True
def NZ15_group(record):
  return True

