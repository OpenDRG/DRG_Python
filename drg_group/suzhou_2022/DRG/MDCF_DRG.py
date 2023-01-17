from drg_group.suzhou_2022.Base import messages,has_mcc,has_cc

def FP19_group(record):
  return True

def FM29_group(record):
  return True

def FC19_group(record):
  return True

def FL19_group(record):
  return True

def FR39_group(record):
  return True

def FB29_group(record):
  return True

def FK39_group(record):
  return True

def FF19_group(record):
  return True

def FL29_group(record):
  return True

def FK19_group(record):
  return True

def FD19_group(record):
  return True

def FT29_group(record):
  return True

def FB19_group(record):
  return True

def FE19_group(record):
  return True

def FN19_group(record):
  return True

def FJ19_group(record):
  return True

def FT39_group(record):
  return True

def FD39_group(record):
  return True

def FR19_group(record):
  return True

def FE29_group(record):
  return True

def FK29_group(record):
  return True

def FR49_group(record):
  return True

def FM19_group(record):
  return True

def FV19_group(record):
  return True

def FL39_group(record):
  return True

def FM49_group(record):
  return True

def FF29_group(record):
  return True

def FM39_group(record):
  return True

def FU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def FR21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def FF31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def FW21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def FZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def FU21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

def FW1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def FV3A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def FD2A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def FT4A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def FV2A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def FT1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def FN2A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def FZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def FU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def FF33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def FR23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def FU23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def FW2B_group(record):
  return True

def FU25_group(record):
  return True

def FV25_group(record):
  return True

def FR25_group(record):
  return True

def FN25_group(record):
  return True

def FZ15_group(record):
  return True

def FF35_group(record):
  return True

def FT45_group(record):
  return True

def FT15_group(record):
  return True

def FW15_group(record):
  return True

def FD25_group(record):
  return True

def FV35_group(record):
  return True

def FU15_group(record):
  return True

