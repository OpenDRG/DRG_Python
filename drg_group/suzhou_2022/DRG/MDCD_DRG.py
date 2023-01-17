from drg_group.suzhou_2022.Base import messages,has_mcc,has_cc

def DD29_group(record):
  return True

def DG29_group(record):
  return True

def DB19_group(record):
  return True

def DK19_group(record):
  return True

def DC29_group(record):
  return True

def DG19_group(record):
  return True

def DB29_group(record):
  return True

def DA19_group(record):
  return True

def DE29_group(record):
  return True

def DC19_group(record):
  return True

def DV19_group(record):
  return True

def DB39_group(record):
  return True

def DJ19_group(record):
  return True

def DD19_group(record):
  return True

def DU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def DR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def DZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def DS1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def DW1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def DT2A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def DT1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def DE1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def DU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def DZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def DR1B_group(record):
  return True

def DE15_group(record):
  return True

def DW15_group(record):
  return True

def DZ15_group(record):
  return True

def DU15_group(record):
  return True

def DT15_group(record):
  return True

def DS15_group(record):
  return True

def DT25_group(record):
  return True

