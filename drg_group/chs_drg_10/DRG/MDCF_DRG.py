from drg_group.chs_drg_10.Base import has_mcc,has_cc,intersect
def FB19_group(record):
  return True
def FB29_group(record):
  return True
def FB39_group(record):
  return True
def FC19_group(record):
  return True
def FC29_group(record):
  return True
def FC39_group(record):
  return True
def FD19_group(record):
  return True
def FD29_group(record):
  return True
def FD39_group(record):
  return True
def FE19_group(record):
  return True
def FF39_group(record):
  return True
def FF49_group(record):
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
def FL29_group(record):
  return True
def FM19_group(record):
  return True
def FM29_group(record):
  return True
def FM39_group(record):
  return True
def FR19_group(record):
  return True
def FR39_group(record):
  return True
def FR49_group(record):
  return True
def FT19_group(record):
  return True
def FT39_group(record):
  return True
def FU29_group(record):
  return True
def FV29_group(record):
  return True
def FV39_group(record):
  return True
def FV49_group(record):
  return True
def FW29_group(record):
  return True
def FZ19_group(record):
  return True
def FF11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FF21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FN11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FN21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FR21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FT21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FW11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def FF13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FF23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FN13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FN23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FR23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FT23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FV13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FW13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def FF15_group(record):
  return True
def FF25_group(record):
  return True
def FN15_group(record):
  return True
def FN25_group(record):
  return True
def FR25_group(record):
  return True
def FS15_group(record):
  return True
def FT25_group(record):
  return True
def FU15_group(record):
  return True
def FV15_group(record):
  return True
def FW15_group(record):
  return True

