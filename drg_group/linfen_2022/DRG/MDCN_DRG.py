from drg_group.linfen_2022.Base import has_mcc,has_cc,intersect
def NA19_group(record):
  return True
def NC19_group(record):
  return True
def ND19_group(record):
  return True
def NE19_group(record):
  return True
def NJ19_group(record):
  return True
def NS19_group(record):
  return True
def NB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def NR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def NZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def NA23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NB13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NF13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NA25_group(record):
  return True
def NB15_group(record):
  return True
def NF15_group(record):
  return True
def NR15_group(record):
  return True
def NZ15_group(record):
  return True

