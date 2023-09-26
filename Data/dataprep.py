import pandas as pd
# Reading the data 

crop_data_path = 'C:/Users/chandana/Desktop/Harvestify/Data-raw/cpdata.csv'
fertilizer_data_path = 'C:/Users/chandana/Desktop/Harvestify/Data-raw/Fertilizer.csv'

crop = pd.read_csv(crop_data_path)
fert = pd.read_csv(fertilizer_data_path)
crop.head()
fert.head()
# Function for lowering the cases
def change_case(i):
    i = i.replace(" ", "")
    i = i.lower()
    return i
fert['Crop'] = fert['Crop'].apply(change_case)
crop['label'] = crop['label'].apply(change_case)

for i in crop_names_from_fert:
    print(crop[crop['label'] == i])
    crop['label']
    extract_labels = []
for i in crop_names_from_fert:
    if i in crop_names:
        extract_labels.append(i)
        # using extract labesl on crop to get all the data related to those labels
new_crop = pd.DataFrame(columns = crop.columns)
new_fert = pd.DataFrame(columns = fert.columns)
for label in extract_labels:
    new_crop = new_crop._append(crop[crop['label'] == label])
for label in extract_labels:
    new_fert = new_fert._append(fert[fert['Crop'] == label].iloc[0])
new_crop
new_fert
new_crop.to_csv('C:/Users/chandana/Desktop/Harvestify/Data-raw/MergeFileCrop.csv')
new_fert.to_csv('C:/Users/chandana/Desktop/Harvestify/Data-raw/FertilizerData.csv')

