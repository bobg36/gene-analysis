import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('all_axies.csv')

# Filter out rows where either matronId or sireId is not present
df = df.dropna(subset=['matronId', 'sireId'])

# Ensure matronId and sireId are integers so they can be matched properly
df['matronId'] = df['matronId'].astype(int)
df['sireId'] = df['sireId'].astype(int)

# Create a dictionary for genes lookup
genes_lookup = df.set_index('axieId')['genes'].to_dict()

# Define a function to get genes by axieId
def get_genes_by_id(axie_id):
    return genes_lookup.get(axie_id, None)

# Create the new dataframe with the required columns
childparentgenes_df = pd.DataFrame({
    'childId': df['axieId'],
    'childGenes': df['genes'],
    'matronId': df['matronId'],
    'matronGenes': df['matronId'].apply(get_genes_by_id),
    'sireId': df['sireId'],
    'sireGenes': df['sireId'].apply(get_genes_by_id)
})

# Filter out rows where matronGenes or sireGenes is None
childparentgenes_df = childparentgenes_df.dropna(subset=['matronGenes', 'sireGenes'])

# Save the new dataframe to a CSV file
output_file_path = 'childparentgenes.csv'
childparentgenes_df.to_csv(output_file_path, index=False)

output_file_path