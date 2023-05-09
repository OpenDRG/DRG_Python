from drg_group.yunnan_2022.Base import has_mcc,has_cc,intersect
def NB19_group(record):
  return True
def NC19_group(record):
  return True
def ND19_group(record):
  return True
def NS19_group(record):
  return True
def NZ19_group(record):
  return True
def NJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def NA13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NA23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NE13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NF13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NA15_group(record):
  return True
def NA25_group(record):
  return True
def NE15_group(record):
  return True
def NF15_group(record):
  return True
def NJ15_group(record):
  return True
def NR15_group(record):
  return True

