import csv

# Function to check if the genes are 66 characters long
def check_gene_length(gene):
    return len(gene) == 66

# Read the CSV file and check the length of the genes
def process_genes(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            # Check the length of each gene
            if (check_gene_length(row['childGenes']) and
                check_gene_length(row['matronGenes']) and
                check_gene_length(row['sireGenes'])):
                writer.writerow(row)

# Define input and output file names
input_filename = 'childparentgenes.csv'
output_filename = 'goodcpgenes.csv'

# Process the genes
process_genes(input_filename, output_filename)

output_filename
