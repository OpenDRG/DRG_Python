from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=["A18.006+M49.0*","A18.800x027+M63.0*","A23.901+M49.1*","C49.200x001","C49.200x002","C49.600","C49.601","D16.304","D18.009","D21.100x002","D21.102","D21.202","D21.900x001","D21.900x008","D21.900x013","D36.700x029","D36.700x030","D36.714","D36.715","D48.109","D48.717","D48.720","M06.900","M10.000","M10.002","M10.900x093","M12.500","M16.900","M17.000","M17.101","M17.900","M17.900x004","M19.900x097","M19.904","M19.905","M20.000x011","M20.002","M20.006","M20.007","M20.100x002","M20.400x001","M20.506","M21.201","M21.302","M21.400","M21.505","M25.900x061","M35.901","M43.006","M45.x00","M46.504","M47.001+G99.2*","M47.101+G99.2*","M47.201","M47.801","M47.802","M48.005","M48.901","M48.903","M50.201","M51.101+G55.1*","M51.202","M51.204","M53.101","M53.207","M60.000x093","M60.902","M62.200x001","M62.403","M62.405","M62.406","M62.800x002","M62.800x061","M62.810","M62.813","M62.901","M65.004","M65.400","M65.802","M65.900x093","M65.910","M66.204","M66.304","M67.001","M67.100x041","M67.101","M67.400","M67.400x031","M67.401","M67.402","M67.800x041","M67.800x092","M67.800x095","M70.403","M72.000","M72.001","M72.202","M72.406","M72.600","M72.804","M72.908","M72.909","M72.920","M75.001","M75.102","M75.501","M76.301","M76.600","M76.802","M76.806","M77.101","M77.300","M77.500","M77.800x001","M79.500x061","M79.503","M79.504","M79.600x021","M79.808","M79.900x001","M79.906","M86.900","M86.907","M89.820","M92.701","Q65.000","Q65.100","Q66.000","Q66.700","Q66.803","Q68.102","Q74.010","Q79.800x006","S46.002","S46.200x001","S46.201","S46.300x003","S46.801","S51.901","S52.811","S56.000x002","S56.000x003","S56.001","S56.100x001","S56.100x003","S56.200x001","S56.200x002","S56.200x003","S56.300x002","S56.300x003","S56.301","S56.400x002","S56.400x003","S56.500x001","S56.700x001","S56.801","S59.700","S59.900","S61.701","S61.702","S61.901","S61.902","S62.311","S62.510","S62.600x021","S62.611","S62.802","S63.100x021","S66.000x005","S66.000x006","S66.000x007","S66.000x008","S66.000x009","S66.100x001","S66.100x003","S66.100x004","S66.100x005","S66.100x006","S66.100x007","S66.100x008","S66.100x009","S66.200x001","S66.200x002","S66.200x006","S66.200x007","S66.200x008","S66.200x009","S66.300x001","S66.300x002","S66.300x003","S66.300x004","S66.300x005","S66.300x006","S66.300x007","S66.300x008","S66.300x009","S66.400x008","S66.500x009","S66.600x001","S66.601","S66.700x001","S66.900x001","S66.900x003","S66.900x004","S68.001","S68.100x001","S68.200x001","S68.201","S69.700","S76.100x001","S76.100x002","S76.100x004","S76.101","S76.300x002","S82.211","S82.600","S86.001","S86.200x002","S86.300x002","S86.300x003","S86.300x004","S86.300x005","S86.700x002","S91.301","S91.302","S92.201","S92.310","S92.500x001","S96.100x001","S96.101","S96.102","S96.200x001","S96.801","T11.102","T11.500","T11.500x003","T11.900","T13.001","T13.100x003","T13.900","T14.601","T14.602","T14.701","T79.600","T79.601","T84.600x003","T84.800x010","T87.500","Z47.001"]
  adrg_zd1=[]
  adrg_ss=["34.4x01","82.0101","82.0102","82.0200x001","82.0201","82.1200x002","82.1202","82.2100","82.2101","82.2200","82.2900x001","82.3301","82.3500x001","82.3500x002","82.3501","82.3601","82.4100","82.4400x001","82.4400x002","82.4500x001","82.4500x009","82.4500x011","82.4500x012","82.4500x013","82.4501","82.4602","82.5301","82.5501","82.5502","82.5600x002","82.5601","82.5700x001","82.8500x001","82.8500x002","82.8600x001","82.8600x006","82.8600x012","82.8600x013","82.9100x004","82.9103","82.9501","83.0100x001","83.0101","83.0102","83.0200x005","83.0200x006","83.0201","83.0202","83.0203","83.0204","83.1201","83.1202","83.1300x001","83.1300x006","83.1300x007","83.1300x008","83.1301","83.1400x006","83.1405","83.3200","83.3200x007","83.3200x009","83.3200x012","83.3201","83.4202","83.4400x002","83.4400x003","83.6100","83.6301","83.6400x007","83.6400x008","83.6400x009","83.6400x011","83.6400x013","83.6400x015","83.6401","83.6402","83.6500x002","83.6500x003","83.6500x005","83.6500x006","83.6500x011","83.6500x012","83.6500x016","83.6500x018","83.6501","83.6502","83.7300x002","83.7500x003","83.7500x004","83.7501","83.7600x002","83.7600x003","83.7600x005","83.7600x006","83.7600x010","83.7700x017","83.7700x026","83.7700x027","83.7700x031","83.7702","83.7900x002","83.7900x003","83.8202","83.8500x001","83.8500x003","83.8500x009","83.8500x028","83.8500x029","83.8501","83.8600","83.8700x001","83.8700x007","83.8701","83.8901","83.9100x001","83.9100x005","83.9100x007","83.9101","83.9103","83.9104","83.9105","86.2800x012","86.8900x011"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合IH1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCI_DRG.IH19_group(record):
      return 'IH19'

    return 'IH1'
  else:
    return ''
