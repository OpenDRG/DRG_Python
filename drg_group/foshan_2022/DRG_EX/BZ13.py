from drg_group.foshan_2022.Base import message,intersect,has_mcc,has_cc,SS_VALID

def group(record):
  adrg_zd=["E06.302+G94.8*","E16.108+G94.8*","E51.200+G32.8*","G09.x01","G91.800x006","G92.x00x002","G92.x00x003","G92.x00","G92.x01","G92.x02","G93.101","G93.102","G93.400x001","G93.400x002","G93.400x005","G93.400x007","G93.400x008","G93.400","G93.403","G93.404","G93.405","G93.800x007","G93.802","G93.901","I61.904","I67.201","I67.400x001","I69.000x001","I69.000x002","I69.000x003","I69.100x001","I69.100x002","I69.100x003","I69.200x001","I69.800x003","M32.114+G94.8*","T80.600x007","T80.600x008","T80.600x009"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BZ13入组条件，匹配规则：主诊断匹配')
    return True