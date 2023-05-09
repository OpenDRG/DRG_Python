from drg_group.yunnan_2022.Base import has_mcc,has_cc,intersect
def FB19_group(record):
  return True
def FD19_group(record):
  return True
def FD29_group(record):
  return True
def FD39_group(record):
  return True
def FE19_group(record):
  return True
def FE29_group(record):
  return True
def FF19_group(record):
  return True
def FF29_group(record):
  return True
def FK19_group(record):
  return True
def FK29_group(record):
  return True
def FK39_group(record):
  return True
def FL19_group(record):
  return True
def FL29_group(record):
  return True
def FL39_group(record):
  return True
def FM19_group(record):
  return True
def FM29_group(record):
  return True
def FM39_group(record):
  return True
def FN19_group(record):
  return True
def FP19_group(record):
  return True
def FR29_group(record):
  return True
def FR39_group(record):
  return True
def FR49_group(record):
  return True
def FT19_group(record):
  return True
def FT29_group(record):
  return True
def FT39_group(record):
  return True
def FT49_group(record):
  return True
def FU29_group(record):
  return True
def FV29_group(record):
  return True
def FZ19_group(record):
  return True
def FB21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FC11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FF31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FM41_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FW21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FF33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FN23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FV13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FV33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FW13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FW23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FB25_group(record):
  return True
def FC15_group(record):
  return True
def FF35_group(record):
  return True
def FJ15_group(record):
  return True
def FM45_group(record):
  return True
def FN25_group(record):
  return True
def FU15_group(record):
  return True
def FV15_group(record):
  return True
def FV35_group(record):
  return True
def FW15_group(record):
  return True
def FW25_group(record):
  return True

