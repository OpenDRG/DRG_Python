from drg_group.anyang_2021.Base import has_mcc,has_cc,intersect
def NC19_group(record):
  return True
def ND19_group(record):
  return True
def NZ19_group(record):
  return True
def NA21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def NR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def NA1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NB1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NS1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NA23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def NR1B_group(record):
  return True
def NA15_group(record):
  return True
def NA25_group(record):
  return True
def NB15_group(record):
  return True
def NS15_group(record):
  return True
def NE1AA_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:])) and record.age<=14
def NF1AA_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:])) and record.age<=14
def NJ1AA_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:])) and record.age<=14
def NE15A_group(record):
  return record.age<=14
def NF15A_group(record):
  return record.age<=14
def NJ15A_group(record):
  return record.age<=14
def NE1AB_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:])) and record.age>14
def NF1AB_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:])) and record.age>14
def NJ1AB_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:])) and record.age>14
def NE15B_group(record):
  return record.age>14
def NF15B_group(record):
  return record.age>14
def NJ15B_group(record):
  return record.age>14

