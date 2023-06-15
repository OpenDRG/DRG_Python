from drg_group.yunnan_2023.Base import message,intersect,SS_VALID
from drg_group.yunnan_2023.ADRG import GB1,GB2,GC1,GC2,GD1,GD2,GE1,GE2,GF1,GF2,GG1,GJ1,GK1,GK2,GK3,GR1,GS1,GT1,GU1,GU2,GV1,GW1,GZ1

def group(record):
  mdc_zd=["A00.000x001","A00.100x001","A00.900","A00.900x002","A00.900x003","A00.900x004","A00.900x005","A03.000x001","A03.100x001","A03.200x001","A03.300x001","A03.800x001","A03.800x002","A03.900","A03.900x002","A03.900x005","A03.900x007","A03.900x008","A03.900x009","A03.901","A03.902","A03.903","A03.904","A04.000x002","A04.100x001","A04.200x001","A04.300x001","A04.400x004","A04.401","A04.500","A04.600","A04.600x001","A04.700","A04.700x002","A04.701","A04.702","A04.800x001","A04.800x003","A04.800x006","A04.800x007","A04.800x010","A04.801","A04.802","A04.803","A04.900","A04.901","A04.902","A05.000","A05.000x001","A05.100","A05.200","A05.200x002","A05.202","A05.300","A05.300x001","A05.400","A05.400x001","A05.800","A05.900","A07.000","A07.100","A07.200","A07.300","A07.300x002","A07.800x002","A07.801","A07.900x001","A08.000","A08.100x001","A08.101","A08.200","A08.300","A08.301","A08.400","A08.400x003","A08.401","A08.402","A08.500","A09.000x001","A09.000x003","A09.000x006","A09.001","A09.002","A09.003","A09.004","A09.005","A09.006","A09.007","A09.900x003","A09.900x004","A09.900x006","A09.900x007","A09.901","A09.902","A09.903","A09.904","A18.300x009+K93.0*","A18.300x013+K93.0*","A18.300x014+K93.0*","A18.300x015+K93.0*","A18.300x016","A18.302+K93.0*","A18.303+K93.0*","A18.304+K93.0*","A18.305+K93.0*","A18.306+K93.0*","A18.307+K93.0*","A18.308","A18.309","A18.310","A18.311+K93.0*","A18.312+K93.0*","A18.313+K93.0*","A18.314+K67.3*","A18.315+K93.0*","A18.316+K93.0*","A18.800x014+K23.0*","A18.807+K23.0*","A18.812+K93.8*","A49.809","A52.710+K67.2*","A54.807+K67.1*","A60.102+K93.8*","A74.801+K67.0*","B37.800x091","B37.804","B37.805","B37.806","B46.200x001+K93.8*","B49.x00x002","B49.x12","B49.x16","B49.x17","B66.501","B77.000x001+K93.8*","B77.001+K93.8*","B82.000","B82.900","B82.901","B87.800x002+K93.8*","C15.000","C15.100","C15.100x002","C15.100x003","C15.100x004","C15.200","C15.300","C15.400","C15.500","C15.800x001","C15.800x002","C15.800x003","C15.800x004","C15.801","C15.802","C15.900","C15.900x003","C16.000","C16.000x003","C16.000x004","C16.001","C16.002","C16.100","C16.200","C16.301","C16.400","C16.401","C16.402","C16.500","C16.600","C16.800","C16.800x002","C16.800x003","C16.801","C16.802","C16.803","C16.804","C16.900","C16.900x003","C16.902","C16.903","C17.000","C17.100","C17.200","C17.300","C17.800","C17.801","C17.900","C17.900x002","C18.000","C18.001","C18.100","C18.200","C18.300","C18.400","C18.500","C18.600","C18.700","C18.800x002","C18.801","C18.802","C18.803","C18.900","C18.900x001","C18.901","C19.x00","C19.x01","C20.x00","C20.x00x003","C20.x01","C21.000","C21.100","C21.101","C21.200","C21.800","C21.801","C21.802","C26.000","C26.800","C26.800x001","C26.800x002","C26.800x003","C26.900","C26.901","C45.100","C45.100x005","C45.101","C45.102","C45.103","C45.700x002","C45.700x005","C45.703","C45.705","C48.000","C48.100","C48.103","C48.104","C48.105","C48.200","C48.201","C48.800","C76.200","C76.304","C77.106","C77.200x001","C77.201","C77.207","C77.208","C78.400","C78.401","C78.402","C78.403","C78.500x004","C78.500x006","C78.500x008","C78.501","C78.502","C78.503","C78.504","C78.505","C78.600x004","C78.601","C78.602","C78.603","C78.800x005","C78.800x010","C78.800x013","C78.800x014","C78.801","C78.802","C78.803","C78.804","C78.809","C79.800x834","C79.809","D00.100","D00.200","D00.200x002","D00.200x003","D01.000","D01.100","D01.200","D01.300x001","D01.301","D01.401","D01.402","D01.403","D01.404","D01.405","D01.900","D09.700x002","D12.000","D12.000x002","D12.001","D12.100","D12.200","D12.300","D12.301","D12.302","D12.400","D12.500","D12.600","D12.601","D12.602","D12.603","D12.700","D12.800","D12.900x001","D12.901","D13.000","D13.100","D13.101","D13.200","D13.301","D13.302","D13.303","D13.304","D13.900","D13.900x003","D13.902","D17.500","D17.500x001","D17.500x003","D17.500x004","D17.500x005","D17.500x007","D17.500x008","D17.500x009","D17.700x017","D17.700x022","D17.700x027","D17.701","D17.702","D18.000x040","D18.000x041","D18.000x042","D18.000x043","D18.000x045","D18.000x046","D18.000x801","D18.000x825","D18.000x838","D18.000x859","D18.012","D18.100x001","D18.106","D19.100","D20.000","D20.100","D20.101","D20.102","D36.700x014","D36.700x018","D36.700x019","D36.707","D36.708","D36.901","D37.100x001","D37.100x002","D37.100x003","D37.101","D37.102","D37.103","D37.200x001","D37.200x002","D37.200x003","D37.200x004","D37.201","D37.202","D37.203","D37.204","D37.205","D37.206","D37.207","D37.300x001","D37.301","D37.400x001","D37.400x002","D37.401","D37.402","D37.403","D37.404","D37.405","D37.406","D37.407","D37.408","D37.409","D37.410","D37.411","D37.500x001","D37.500x002","D37.501","D37.502","D37.503","D37.606","D37.607","D37.700x001","D37.700x002","D37.700x007","D37.701","D37.702","D37.707","D37.708","D37.709","D37.710","D37.900x001","D37.901","D48.117","D48.121","D48.129","D48.300x001","D48.301","D48.400x002","D48.400x003","D48.401","D48.402","D48.403","D48.700x004","D48.700x005","D48.713","D48.714","E10.400x330+G99.0*","E10.400x340+G99.0*","E10.400x350+G99.0*","E10.400x370+G99.0*","E11.400x330+G99.0*","E11.400x340+G99.0*","E11.400x350+G99.0*","E11.406+G99.0*","E14.400x330+G99.0*","E14.400x340+G99.0*","E14.400x350+G99.0*","E14.400x370+G99.0*","E16.400","E16.400x003","E16.401","E16.402","E73.000","E73.100","E73.800","E73.900","E84.102","E85.417+K93.8*","I72.800x063","I72.800x131","I72.800x132","I72.800x142","I72.801","I72.802","I72.807","I72.815","I72.816","I74.800x011","I77.400","I78.802","I85.000x001","I85.900x001","I85.901","I86.400","I86.400x001","I86.400x002","I86.400x004","I86.401","I86.800x014","I86.800x022","I86.812","I88.000x003","I88.001","I88.105","I89.005","I89.006","I89.800x006","I89.800x019","I89.801","I89.803","J11.800x002","K20.x00","K20.x00x001","K20.x00x003","K20.x00x006","K20.x01","K20.x02","K20.x03","K21.001","K21.900x003","K21.901","K21.902","K21.903","K22.000x001","K22.000x002","K22.100","K22.101","K22.102","K22.103","K22.200","K22.201","K22.202","K22.203","K22.204","K22.205","K22.206","K22.207","K22.208","K22.209","K22.300","K22.301","K22.400","K22.400x003","K22.401","K22.500","K22.600x001","K22.601","K22.700x001","K22.800x003","K22.800x011","K22.801","K22.802","K22.803","K22.804","K22.805","K22.806","K22.807","K22.808","K22.809","K22.811","K22.812","K22.813","K22.814","K22.815","K22.900x001","K22.901","K25.000","K25.000x001","K25.000x002","K25.001","K25.100x001","K25.200x001","K25.300x001","K25.400x001","K25.400x002","K25.401","K25.500x001","K25.501","K25.600","K25.700","K25.900x001","K25.901","K25.902","K25.903","K26.000","K26.001","K26.100","K26.200x001","K26.200x002","K26.300","K26.400x003","K26.401","K26.500x001","K26.501","K26.600","K26.701","K26.900x001","K26.900x002","K27.000","K27.100x001","K27.200","K27.300","K27.400","K27.400x001","K27.400x002","K27.400x004","K27.401","K27.500","K27.500x001","K27.500x002","K27.500x005","K27.501","K27.502","K27.503","K27.600","K27.600x001","K27.700x001","K27.900x001","K27.900x002","K27.900x005","K27.901","K27.902","K28.000","K28.100","K28.200","K28.300x001","K28.400x002","K28.401","K28.500","K28.500x001","K28.600","K28.600x001","K28.700","K28.900x001","K28.900x002","K28.901","K29.000","K29.001","K29.100x001","K29.101","K29.200","K29.300","K29.400","K29.500","K29.501","K29.600","K29.600x006","K29.600x007","K29.601","K29.602","K29.603","K29.604","K29.605","K29.606","K29.608","K29.700","K29.700x002","K29.701","K29.800","K29.801","K29.802","K29.900","K30.x00","K30.x00x001","K31.000","K31.100","K31.100x002","K31.101","K31.102","K31.103","K31.104","K31.200","K31.300","K31.400","K31.500","K31.501","K31.502","K31.600x004","K31.600x005","K31.601","K31.602","K31.603","K31.604","K31.605","K31.606","K31.607","K31.608","K31.609","K31.701","K31.702","K31.703","K31.800x801","K31.800x802","K31.800x806","K31.800x808","K31.801","K31.802","K31.803","K31.804","K31.805","K31.806","K31.807","K31.808","K31.809","K31.810","K31.811","K31.812","K31.813","K31.814","K31.815","K31.816","K31.818","K31.819","K31.820","K31.821","K31.901","K31.902","K31.903","K31.904","K31.905","K35.200","K35.201","K35.300","K35.301","K35.800x001","K36.x00x003","K36.x00x004","K36.x01","K36.x02","K37.x00","K37.x00x002","K38.000","K38.000x002","K38.100","K38.200","K38.300","K38.800x001","K38.800x003","K38.800x004","K38.801","K38.802","K38.900","K40.000x001","K40.001","K40.002","K40.100x001","K40.101","K40.102","K40.200x001","K40.201","K40.202","K40.203","K40.204","K40.300","K40.301","K40.302","K40.303","K40.304","K40.305","K40.306","K40.307","K40.308","K40.309","K40.310","K40.311","K40.312","K40.313","K40.314","K40.315","K40.400x001","K40.401","K40.402","K40.900x001","K40.900x002","K40.900x003","K40.900x004","K40.900x005","K40.900x006","K40.901","K40.902","K40.903","K40.904","K40.905","K40.906","K40.907","K41.000","K41.100x001","K41.200x001","K41.300x002","K41.300x003","K41.301","K41.302","K41.400x001","K41.900x001","K42.000x001","K42.001","K42.100x001","K42.900","K42.901","K42.902","K43.000","K43.001","K43.002","K43.003","K43.004","K43.100","K43.200","K43.301","K43.302","K43.303","K43.304","K43.400","K43.500","K43.601","K43.602","K43.603","K43.604","K43.605","K43.700","K43.900","K43.900x001","K43.902","K44.000x001","K44.000x002","K44.100x001","K44.900x001","K44.901","K45.000","K45.002","K45.003","K45.100","K45.800","K45.801","K45.802","K45.804","K45.805","K45.806","K45.807","K45.808","K46.000","K46.000x002","K46.001","K46.002","K46.100","K46.100x001","K46.101","K46.900","K46.900x002","K46.900x003","K46.900x004","K46.900x012","K46.901","K46.902","K46.903","K46.905","K50.000","K50.000x001","K50.000x005","K50.001","K50.002","K50.101","K50.102","K50.103","K50.104","K50.800","K50.800x001","K50.801","K50.900","K51.000","K51.001","K51.002","K51.003","K51.200x001","K51.201","K51.202","K51.203","K51.300","K51.301","K51.302","K51.303","K51.400","K51.401","K51.500","K51.800x001","K51.900","K51.901","K51.902","K51.903","K52.000","K52.000x001","K52.001","K52.101","K52.102","K52.103","K52.104","K52.200x004","K52.201","K52.202","K52.203","K52.204","K52.300","K52.800x003","K52.801","K52.802","K52.803","K52.804","K52.901","K52.902","K52.903","K52.904","K52.907","K52.908","K52.909","K52.910","K52.911","K52.912","K52.914","K52.917","K52.918","K52.919","K55.000","K55.000x005","K55.000x010","K55.000x011","K55.000x015","K55.001","K55.002","K55.003","K55.004","K55.005","K55.006","K55.007","K55.008","K55.009","K55.010","K55.011","K55.012","K55.013","K55.100","K55.100x001","K55.100x005","K55.100x006","K55.100x008","K55.101","K55.102","K55.103","K55.104","K55.105","K55.106","K55.200","K55.200x013","K55.201","K55.202","K55.300","K55.300x001","K55.800x003","K55.800x004","K55.801","K55.900","K55.900x004","K55.901","K55.902","K56.000","K56.001","K56.100","K56.101","K56.102","K56.200","K56.200x003","K56.200x011","K56.201","K56.202","K56.203","K56.300","K56.400x001","K56.400x003","K56.401","K56.500x003","K56.501","K56.503","K56.600x001","K56.600x005","K56.600x008","K56.601","K56.602","K56.603","K56.604","K56.700","K56.700x003","K56.701","K57.000","K57.001","K57.002","K57.003","K57.100x005","K57.101","K57.102","K57.103","K57.104","K57.105","K57.106","K57.107","K57.108","K57.200x001","K57.201","K57.202","K57.300x006","K57.301","K57.302","K57.303","K57.304","K57.305","K57.400","K57.401","K57.500","K57.800","K57.800x001","K57.801","K57.900","K57.900x001","K58.100","K58.200","K58.300","K58.800","K58.801","K59.000","K59.002","K59.003","K59.100","K59.101","K59.200","K59.200x002","K59.200x003","K59.301","K59.302","K59.303","K59.400","K59.400x002","K59.401","K59.800x002","K59.800x005","K59.801","K59.900x001","K59.900x002","K60.000","K60.100","K60.200","K60.300","K60.301","K60.302","K60.303","K60.400","K60.400x003","K60.401","K60.402","K60.403","K60.500","K61.000","K61.001","K61.002","K61.100","K61.101","K61.200","K61.300","K61.400","K62.000","K62.001","K62.100","K62.100x002","K62.200","K62.200x001","K62.201","K62.202","K62.300","K62.300x003","K62.301","K62.400x002","K62.400x003","K62.400x004","K62.401","K62.402","K62.500x001","K62.501","K62.600x002","K62.601","K62.602","K62.700","K62.800x001","K62.800x005","K62.800x009","K62.800x010","K62.800x012","K62.800x017","K62.800x021","K62.801","K62.802","K62.803","K62.804","K62.805","K62.806","K62.807","K62.808","K62.809","K62.810","K62.811","K62.812","K62.813","K62.814","K62.815","K62.816","K62.817","K62.818","K62.819","K62.820","K62.821","K62.822","K62.901","K62.902","K62.903","K63.000","K63.001","K63.100x001","K63.101","K63.102","K63.103","K63.104","K63.105","K63.107","K63.108","K63.200","K63.200x003","K63.200x008","K63.201","K63.202","K63.203","K63.204","K63.205","K63.206","K63.207","K63.208","K63.209","K63.210","K63.211","K63.212","K63.213","K63.214","K63.215","K63.216","K63.301","K63.302","K63.303","K63.304","K63.305","K63.306","K63.307","K63.308","K63.400","K63.401","K63.402","K63.403","K63.500","K63.500x002","K63.500x084","K63.501","K63.502","K63.503","K63.504","K63.801","K63.802","K63.803","K63.804","K63.805","K63.806","K63.807","K63.809","K63.810","K63.812","K63.813","K63.814","K63.815","K63.816","K63.817","K63.818","K63.819","K63.900x001","K63.900x002","K63.900x003","K63.900x005","K63.901","K63.902","K64.000","K64.100","K64.200","K64.300","K64.400","K64.401","K64.402","K64.500","K64.501","K64.801","K64.802","K64.803","K64.804","K64.805","K64.806","K64.807","K64.808","K64.809","K64.810","K64.811","K64.900","K64.901","K65.000","K65.000x014","K65.001","K65.002","K65.003","K65.004","K65.005","K65.006","K65.008","K65.009","K65.010","K65.011","K65.012","K65.013","K65.014","K65.015","K65.016","K65.017","K65.800x001","K65.800x002","K65.801","K65.802","K65.803","K65.804","K65.805","K65.806","K65.807","K65.900","K65.901","K65.902","K65.903","K65.904","K65.905","K65.906","K66.000","K66.000x007","K66.001","K66.002","K66.003","K66.004","K66.005","K66.006","K66.007","K66.008","K66.100","K66.101","K66.102","K66.103","K66.200","K66.201","K66.800","K66.800x008","K66.800x009","K66.801","K66.802","K66.803","K66.805","K66.806","K66.807","K66.808","K66.809","K66.810","K66.811","K66.812","K66.901","K90.000","K90.000x001","K90.001","K90.002","K90.100x001","K90.100x002","K90.100x003","K90.200","K90.200x001","K90.300x001","K90.400","K90.400x003","K90.401","K90.402","K90.403","K90.404","K90.405","K90.406","K90.801","K90.802+M14.8*","K90.900x002","K90.901","K91.000","K91.100","K91.100x001","K91.101","K91.102","K91.103","K91.200x002","K91.201","K91.202","K91.300","K91.300x002","K91.301","K91.302","K91.303","K91.305","K91.401","K91.402","K91.404","K91.405","K91.406","K91.408","K91.800x007","K91.800x102","K91.800x103","K91.800x106","K91.800x111","K91.800x116","K91.800x117","K91.800x206","K91.800x412","K91.800x501","K91.800x601","K91.800x602","K91.800x702","K91.801","K91.802","K91.803","K91.804","K91.805","K91.808","K91.809","K91.810","K91.811","K91.812","K91.813","K91.814","K91.815","K91.816","K91.817","K91.818","K91.819","K91.820","K91.821","K91.824","K91.828","K91.829","K91.830","K91.831","K91.832","K91.833","K91.834","K91.835","K91.836","K91.837","K91.839","K91.842","K91.900","K92.000","K92.100x001","K92.200x001","K92.200x005","K92.201","K92.202","K92.203","K92.204","K92.205","K92.206","K92.207","K92.208","K92.209","K92.210","K92.800x001","K92.800x002","K92.800x003","K92.800x004","K92.800x005","K92.800x007","K92.800x011","K92.901","M32.112+K93.8*","M32.115+K67.8*","M34.800x006+K23.8*","Q27.810","Q39.000x001","Q39.100","Q39.100x011","Q39.100x021","Q39.200x011","Q39.300","Q39.400","Q39.501","Q39.600","Q39.601","Q39.602","Q39.800x201","Q39.800x903","Q39.800x904","Q39.800x905","Q39.801","Q39.802","Q39.803","Q39.900","Q40.000","Q40.002","Q40.003","Q40.100","Q40.200x004","Q40.200x005","Q40.200x010","Q40.201","Q40.202","Q40.203","Q40.204","Q40.205","Q40.206","Q40.207","Q40.208","Q40.209","Q40.300","Q40.800","Q40.900","Q41.001","Q41.002","Q41.003","Q41.101","Q41.102","Q41.103","Q41.104","Q41.201","Q41.202","Q41.203","Q41.800","Q41.901","Q41.902","Q41.903","Q42.000x101","Q42.000x201","Q42.000x301","Q42.000x401","Q42.000x501","Q42.001","Q42.002","Q42.101","Q42.102","Q42.200x901","Q42.200x902","Q42.200x903","Q42.200x904","Q42.200x905","Q42.201","Q42.202","Q42.301","Q42.302","Q42.800x002","Q42.800x003","Q42.801","Q42.802","Q42.803","Q42.901","Q42.902","Q42.903","Q43.000","Q43.001","Q43.002","Q43.003","Q43.004","Q43.100","Q43.101","Q43.102","Q43.103","Q43.104","Q43.105","Q43.106","Q43.200","Q43.200x002","Q43.200x003","Q43.201","Q43.300x201","Q43.300x901","Q43.301","Q43.401","Q43.402","Q43.403","Q43.404","Q43.500","Q43.601","Q43.602","Q43.700","Q43.800x006","Q43.800x008","Q43.800x009","Q43.800x012","Q43.800x014","Q43.800x015","Q43.800x017","Q43.800x018","Q43.800x019","Q43.801","Q43.802","Q43.803","Q43.804","Q43.805","Q43.806","Q43.807","Q43.808","Q43.809","Q43.810","Q43.811","Q43.812","Q43.900","Q43.901","Q44.500x008","Q45.300x102","Q45.300x103","Q45.300x104","Q45.300x105","Q45.801","Q45.900","Q51.702","Q79.200","Q79.201","Q79.300","Q79.301","Q79.400","Q79.500","Q79.501","Q85.900x002","Q85.900x036","Q85.902","Q85.906","Q85.913","Q89.300","Q89.300x001","Q89.301","Q89.302","R10.000","R10.000x004","R10.101","R10.102","R10.103","R10.301","R10.400x002","R10.400x004","R10.401","R10.402","R12.x00","R12.x00x002","R14.x00x001","R14.x00x002","R14.x00x003","R14.x00x006","R14.x00x007","R15.x00","R19.000x005","R19.100","R19.100x001","R19.100x002","R19.200","R19.200x002","R19.300","R19.400","R19.500x002","R19.500x003","R19.500x004","R19.501","R19.600","R19.800x001","R58.x01","R85.000","R85.100","R85.200","R85.300","R85.400","R85.500","R85.600","R85.700","R85.800","R93.300x001","R93.300x003","R93.300x004","R93.303","R93.500x001","S11.202","S30.102","S36.300","S36.301","S36.310","S36.400","S36.400x091","S36.400x093","S36.400x095","S36.401","S36.402","S36.403","S36.404","S36.405","S36.411","S36.412","S36.413","S36.414","S36.500","S36.500x011","S36.500x021","S36.500x031","S36.500x041","S36.500x091","S36.500x092","S36.500x093","S36.501","S36.511","S36.600","S36.600x003","S36.601","S36.611","S36.700","S36.701","S36.800x022","S36.801","S36.802","S36.803","S36.810","S36.811","S36.812","S36.813","S36.814","S36.900","S36.901","S36.910","S39.905","S39.909","T18.100","T18.200","T18.300","T18.300x003","T18.301","T18.400","T18.500x004","T18.501","T18.502","T18.801","T18.900","T28.100","T28.200x001","T28.200x002","T28.600","T28.700x002","T28.701","T28.702","T80.200x001","T98.300x001"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCG入组条件，匹配规则：主诊断匹配')

  result=GB1.group(record)
  if result:
    return result
  result=GB2.group(record)
  if result:
    return result
  result=GC1.group(record)
  if result:
    return result
  result=GC2.group(record)
  if result:
    return result
  result=GD1.group(record)
  if result:
    return result
  result=GD2.group(record)
  if result:
    return result
  result=GE1.group(record)
  if result:
    return result
  result=GE2.group(record)
  if result:
    return result
  result=GF1.group(record)
  if result:
    return result
  result=GF2.group(record)
  if result:
    return result
  result=GG1.group(record)
  if result:
    return result
  result=GJ1.group(record)
  if result:
    return result
  result=GK1.group(record)
  if result:
    return result
  result=GK2.group(record)
  if result:
    return result
  result=GK3.group(record)
  if result:
    return result

  if record.ssList and record.ssList[0] in SS_VALID:
    message('符合GQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'GQY'

  result=GR1.group(record)
  if result:
    return result

  result=GS1.group(record)
  if result:
    return result

  result=GT1.group(record)
  if result:
    return result

  result=GU1.group(record)
  if result:
    return result

  result=GU2.group(record)
  if result:
    return result

  result=GV1.group(record)
  if result:
    return result

  result=GW1.group(record)
  if result:
    return result

  result=GZ1.group(record)
  if result:
    return result

  message('不符合MDCG的ADRG入组条件')

