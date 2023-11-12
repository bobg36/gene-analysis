visualise_id_distribution.ipynb
unrelated to gene analysis project, this notebook visualises distribution of id sold to see how much more often higher id axies are traded compared to lower id axies. we are interested in this information as we are looking for a way to fill in the 4 week gap where our axie sales scraper was offline.

genetest.js
testing hexgene convertion using .js package that we are reverse engineering

gene_map.py
this file contains mapping for binary genes, parts and part class

decode_genes.py
contains functions to decode genes. "hexgene_to_genes(hexgene)" converts hexgenes to gene dict

generate_childparentgenes.py
reads all_axies.csv (this file contains all axie details from 0 to highestId), outputs childparentgenes.csv, which contains genes of child and both parents (6 columns)

remove_badgenes.py
reads childparentgenes.csv, removes all rows containing genes that are NOT length=66 (2 for 0x prefix). we can only decode 64 bit genes. this script generates 'goodcpgenes.csv'

convertcsvgenes.js
reads goodcpgenes.csv and outputs updated_goodcpgenes.csv, which should have readable genes. updated_goodcpgenes.csv can be used for gene analysis

gene analysis.ipynb
we find out how r1 and r2 genes are inherited here