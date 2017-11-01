# Copyright 2017 mengxi wang wmx@bu.edu
# Copyright 2017 rui chen ruirui@bu.edu
#Earth's mass is approximately 5.97×10^24 kg (5,970 Yg). 
#It is composed mostly of 
#iron (32.1%), molar_mass=56g/mol, ele_num=26
#oxygen (30.1%), molar_mass=16g/mol, ele_num=8
#silicon (15.1%), 14g/mol,14
#magnesium (13.9%), 24g/mol,12
#sulfur (2.9%), 32g/mol,16
#nickel (1.8%), 59g/mol,28
#calcium (1.5%), 40g/mol,20
#aluminium (1.4%),27g/mol,13
#NA=6.02e23 mol-1


element_prop=[0.321,0.301,0.151,0.139,0.029,0.018,0.015,0.014]
molar_mass=[56,16,14,12,16,28,20,13]
elec_num=[26,8,14,12,16,28,20,13]
NA=6.02e23
total_molar_mass=0
total=0
total_elec_num=0

for i in range (0,8):
	total_molar_mass+=element_prop[i]*molar_mass[i]
	total_elec_num+=element_prop[i]*elec_num[i]
	total+=element_prop[i]

average_molar_mass=total_molar_mass/total
average_elec_num=total_elec_num/total

elec_num_est=(5.97e24/(average_molar_mass/1000))*NA*average_elec_num/8/1.1e12
elec_num_low=(5.97e24*0.7/(average_molar_mass*1.3/1000))*NA*(average_elec_num*0.7)/8/1.1e12
elec_num_hi=(5.97e24*1.3/(average_molar_mass*0.7/1000))*NA*(average_elec_num*1.3)/8/1.1e12

print(elec_num_est)
print(elec_num_low)
print(elec_num_hi)