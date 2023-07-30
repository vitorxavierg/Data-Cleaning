# Deleting Url column
del df['Url']

# Removing all rows with 'Not Priced' value on 'Price' column, and removing '$' and ',' strings
df = df.drop(df.index[df['Price'] == 'Not Priced'])
df['Price'] = df['Price'].str.replace('$','')
df['Price'] = df['Price'].str.replace(',','')

# Converting Price to 'int' datatype 
df['Price'] = df['Price'].astype(int)

# Transforming Car column registers into sublists
reference = df['Car'].str.split(' ')

# Parsing Columns
# Year Column
year = []
def Extract(reference):
    return [item[0] for item in reference]
print(Extract(reference))
year = Extract(reference)
# Brand Column
brand = []
def Extract(reference):
    return [item[1] for item in reference]
brand = Extract(reference)
# Model and Trim Level Reference
model_and_trimlevel = []
def Extract(reference):
    return [item[2:] for item in reference]
model_and_trimlevel = Extract(reference)
# Model
model_beta = []
def Extract(model_and_trimlevel):
    return[item[:1] for item in model_and_trimlevel]
model_beta = Extract(model_and_trimlevel)
model = []
for x in model_beta:
    model1 = ' '.join(x)
    model.append(model1)
# Trim Level
trim_level_beta = []
def Extract(model_and_trimlevel):
    return[item[1:] for item in model_and_trimlevel]
trim_level_beta = Extract(model_and_trimlevel)
trim_level = []
for x in trim_level_beta:
    trim1 = ' '.join(x)
    trim_level.append(trim1)

# Inserting the new created columns into df, and deleting Car column
df.insert(1, 'Year', year, True)
df.insert(2, 'Brand', brand, True)
df.insert(3, 'Model', model, True)
df.insert(4, 'Trim Level', trim_level, True)
del df['Car']

# Getting Review mean value to insert on null registers
mean_value = df['Review'].mean()

# Filling null registers with the mean of review values
df['Review'] = df['Review'].fillna(value = mean_value)

# Droping duplicates
df = df.drop_duplicates()