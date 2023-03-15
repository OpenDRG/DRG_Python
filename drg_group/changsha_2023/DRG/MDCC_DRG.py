from drg_group.changsha_2023.Base import has_mcc,has_cc,intersect
def CB49_group(record):
  return True
def CR19_group(record):
  return True
def CV19_group(record):
  return True
def CD1A_CS_group(record):
  return int(record.age)<=6
def CD1B_CS_group(record):
  return True
def CB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CB31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CW11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CX11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CB23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CC13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CD23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CB15_group(record):
  return True
def CB25_group(record):
  return True
def CB35_group(record):
  return True
def CC15_group(record):
  return True
def CD25_group(record):
  return True
def CJ15_group(record):
  return True
def CS15_group(record):
  return True
def CT15_group(record):
  return True
def CU15_group(record):
  return True
def CW15_group(record):
  return True
def CX15_group(record):
  return True
def CZ15_group(record):
  return True

