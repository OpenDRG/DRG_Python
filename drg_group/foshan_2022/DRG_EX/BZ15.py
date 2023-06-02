from drg_group.foshan_2022.Base import message,intersect,has_mcc,has_cc,SS_VALID

def group(record):
  adrg_zd=["G91.100x002","G91.100","I69.300x002","I69.300x003","I69.300"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BZ15入组条件，匹配规则：主诊断匹配')
    return True