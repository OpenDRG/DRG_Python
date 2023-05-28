from drg_group.hefei_2023.Base import message,intersect,SS_VALID

def group(record):
  adrg_zd=["A15.000x010","A15.000x012","A15.000x014","A15.000x020","A15.000x022","A15.000x024","A15.100x002","A15.100x003","A15.100x004","A15.100x007","A15.100x008","A15.100x009","A15.500x010","A15.500x011","A15.500x012","A15.500x013","A15.500x014","A15.500x015","A15.500x020","A15.500x021","A15.500x022","A15.500x023","A15.500x024","A15.500x025","A19.000x001","A19.000x002","A19.000x003","A19.000x004","A19.000x005","A19.000x006","A19.000x011","A19.000x012","A19.000x013","A19.000x014","A19.000x015","A19.000x016"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合ES1Z入组条件，匹配规则：主诊断匹配')
    return True