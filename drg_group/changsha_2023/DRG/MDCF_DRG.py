from drg_group.changsha_2023.Base import has_mcc,has_cc,intersect
def FB19_group(record):
  return True
def FB29_group(record):
  return True
def FD39_group(record):
  return True
def FE19_group(record):
  return True
def FE29_group(record):
  return True
def FF19_group(record):
  return True
def FJ19_group(record):
  return True
def FK19_group(record):
  return True
def FK29_group(record):
  return True
def FK39_group(record):
  return True
def FL19_group(record):
  return True
def FL39_group(record):
  return True
def FM29_group(record):
  return True
def FM49_group(record):
  return True
def FN19_group(record):
  return True
def FP19_group(record):
  return True
def FR19_group(record):
  return True
def FR49_group(record):
  return True
def FT29_group(record):
  return True
def FU29_group(record):
  return True
def FV1A_CS_group(record):
  return int(record.age)<=6
def FV1B_CS_group(record):
  return True
def FC11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FD11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FD21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FF31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FL21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FM11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FM31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FN21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FR21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FR31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FT41_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FV21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FV31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FW11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FW21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FD23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FF23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FF33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FT13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FT33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FC15_group(record):
  return True
def FD15_group(record):
  return True
def FD25_group(record):
  return True
def FF25_group(record):
  return True
def FF35_group(record):
  return True
def FL25_group(record):
  return True
def FM15_group(record):
  return True
def FM35_group(record):
  return True
def FN25_group(record):
  return True
def FR25_group(record):
  return True
def FR35_group(record):
  return True
def FT15_group(record):
  return True
def FT35_group(record):
  return True
def FT45_group(record):
  return True
def FU15_group(record):
  return True
def FV25_group(record):
  return True
def FV35_group(record):
  return True
def FW15_group(record):
  return True
def FW25_group(record):
  return True
def FZ15_group(record):
  return True

