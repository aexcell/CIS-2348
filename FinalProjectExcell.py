# Alexandra Excell
# 1595971

# import libraries
import pandas as pd
import numpy as np
import datetime as dt

# create needed column list & empty inventory
columns = ["ID","ManufacturerName","Type","Price","ServiceDate","Damaged"]
FULL_INVENTORY = pd.DataFrame(columns=columns)

# main function
def read_file(filename,FULL_INVENTORY=FULL_INVENTORY):

	df = pd.read_csv(filename,header=None)
	if "ManufacturerList" in filename:
		df.columns=["ID","ManufacturerName","Type","Damaged"]
	elif "PriceList" in filename:
		df.columns = ["ID", "Price"]
	elif "ServiceDatesList" in filename:
		df.columns = ["ID", "ServiceDate"]

	for idx in range(len(df)):
		if df["ID"][idx] not in FULL_INVENTORY["ID"]:
			cols = df.iloc[[idx]].columns
			for col in cols:
				FULL_INVENTORY.loc[idx, col] = df.loc[idx, col]

		else:
			print(df['ID'][idx], ": already include in inventory")
			print(df['ID'][idx], ": updating appropriate columns")
			for col in cols:
				FULL_INVENTORY.loc[idx, col] = df.loc[idx, col]
	return df,FULL_INVENTORY # may not need df

# load files
df,FULL_INVENTORY = read_file('ManufacturerList.csv',FULL_INVENTORY)
df,FULL_INVENTORY = read_file('PriceList.csv',FULL_INVENTORY)
df,FULL_INVENTORY = read_file('ServiceDatesList.csv',FULL_INVENTORY)
#remove any unneeded whitespace
FULL_INVENTORY['ManufacturerName'] = FULL_INVENTORY['ManufacturerName'].str.replace(" ","")

print(FULL_INVENTORY)

# Create output files
# create full_inventory file
full_inventory = FULL_INVENTORY.sort_values(by=['ManufacturerName'])
# print(full_inventory)
full_inventory.to_csv('FullInventory.csv', index=False)

# create item inventory file
phone_inventory = FULL_INVENTORY.loc[FULL_INVENTORY['Type']=='phone'].sort_values(by=['ID'])
laptop_inventory = FULL_INVENTORY.loc[FULL_INVENTORY['Type']=='laptop'].sort_values(by=['ID'])
tower_inventory = FULL_INVENTORY.loc[FULL_INVENTORY['Type']=='tower'].sort_values(by=['ID'])
# print(tower_inventory)
# save item files
phone_inventory.to_csv('PhoneInventory.csv', index=False)
laptop_inventory.to_csv('LaptopInventory.csv', index=False)
tower_inventory.to_csv('TowerInventory.csv', index=False)

# create past service inventory
today_date = dt.date.today()
today_date = today_date.strftime("%m/%d/%Y")

# convert servicedate column to datetime
FULL_INVENTORY['ServiceDate'] = pd.to_datetime(FULL_INVENTORY['ServiceDate'],format="%m/%d/%Y")
# print(FULL_INVENTORY)

past_due = FULL_INVENTORY.loc[FULL_INVENTORY['ServiceDate']<today_date].sort_values(by=['ServiceDate'])
# reformat ServiceDate Column
past_due['ServiceDate'] = past_due['ServiceDate'].dt.strftime('%m/%d/%Y')
past_due_inventory = past_due
past_due_inventory.to_csv('PastServiceDateInventory.csv', index=False)

# create damaged inventory file
damaged_inventory = FULL_INVENTORY.loc[FULL_INVENTORY['Damaged']=='damaged'].sort_values(by=['Price'])
damaged_inventory.to_csv('DamagedInventory.csv', index=False)

# Queries
# take single to multi-word string input
# test code
# manufacturer_select = "really nice apple"
# manufacturer_select = manufacturer_select.title().split()
# type_select = ["laptop"]
user_input = 'c'

while user_input != 'q':
	user_input = input("for continue press 'c' for quit press 'q")
	if user_input == 'q':
		break
	manufacturer_select = input("select Item Manufacturer").capitalize().split()
	type_select = input("select Item Type").split()

	manufacturer_list = list(FULL_INVENTORY['ManufacturerName'].unique())
	type_list = list(FULL_INVENTORY['Type'].unique())

	if set(manufacturer_select) & set(manufacturer_list) and set(type_select) & set(type_list):
		manufacturer = list(set(manufacturer_select) & set(manufacturer_list))[0]
		item_type = list(set(type_select) & set(type_list))[0]
		your_prodDF = FULL_INVENTORY.loc[(FULL_INVENTORY['ManufacturerName']==manufacturer)
										 & (FULL_INVENTORY['Type']==item_type)]
		your_prodDF = your_prodDF.loc[your_prodDF['ServiceDate']>today_date]
		your_prodDF = your_prodDF.loc[your_prodDF['Damaged']!="damaged"]
		if your_prodDF.empty:
			print("Your items are either damaged or past due for Service")
		else:
			your_prodDF = your_prodDF.sort_values(by=['Price'],ascending=False)
			your_prodDF = your_prodDF.iloc[0]

			print("Your item is: ", your_prodDF['ID'], your_prodDF['ManufacturerName'], your_prodDF['Type'],
				  your_prodDF['Price'])

			#suggested alternative product
			price_max = your_prodDF['Price'] + 200
			price_min = your_prodDF['Price'] - 200
			nearby_item = FULL_INVENTORY.loc[(FULL_INVENTORY['Type']==item_type) & (FULL_INVENTORY['Price']>price_min) &
											  (FULL_INVENTORY['Price']<price_max) &
											  (FULL_INVENTORY['Damaged']!="damaged") &
											  (FULL_INVENTORY['ServiceDate']>today_date) &
											 (FULL_INVENTORY['ManufacturerName']!=manufacturer)]
			if not nearby_item.empty:
				print("You may also consider: ", nearby_item['ID'], nearby_item['ManufacturerName'],
					  nearby_item['Type'], nearby_item['Price'])

	else:
		print("No such item in inventory")

