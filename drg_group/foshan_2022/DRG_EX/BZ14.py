from drg_group.foshan_2022.Base import message,intersect,SS_VALID

def group(record):
  adrg_zd=["G91.100X002","G91.100","I69.300X002","I69.300X003","I69.300"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BZ14入组条件，匹配规则：主诊断匹配')
    return True