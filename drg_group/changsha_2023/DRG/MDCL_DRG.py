from drg_group.changsha_2023.Base import has_mcc,has_cc,intersect
def LB29_group(record):
  return True
def LC19_group(record):
  return True
def LT19_group(record):
  return True
def LA11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def LA21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def LB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def LD11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def LF11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def LJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def LL11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def LR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def LS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def LU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def LV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def LW11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def LX11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def LZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def LE13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def LF13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def LJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def LS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def LU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def LZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def LA15_group(record):
  return True
def LA25_group(record):
  return True
def LB15_group(record):
  return True
def LD15_group(record):
  return True
def LE15_group(record):
  return True
def LF15_group(record):
  return True
def LJ15_group(record):
  return True
def LL15_group(record):
  return True
def LR15_group(record):
  return True
def LS15_group(record):
  return True
def LU15_group(record):
  return True
def LV15_group(record):
  return True
def LW15_group(record):
  return True
def LX15_group(record):
  return True
def LZ15_group(record):
  return True

