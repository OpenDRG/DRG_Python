from drg_group.foshan_2022.Base import has_mcc,has_cc,intersect
def RA19_group(record):
  return True
def RA29_group(record):
  return True
def RA39_group(record):
  return True
def RA49_group(record):
  return True
def RB29_group(record):
  return True
def RC15_group(record):
  return True
def RT29_group(record):
  return True
def RV19_group(record):
  return True
def RB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RD11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RE11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RS21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RW11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RW21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def RE13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def RR13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def RS13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def RU13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def RW13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def RB13_group(record):
  return True
def RD13_group(record):
  return True
def RS23_group(record):
  return True
def RT13_group(record):
  return True
def RW23_group(record):
  return True
def RE15_group(record):
  return True
def RR15_group(record):
  return True
def RS15_group(record):
  return True
def RU15_group(record):
  return True
def RW15_group(record):
  return True

