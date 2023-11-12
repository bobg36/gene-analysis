from gene_map import gene_map

def hexgene_to_genes(hexgene):
    parsed_gene = parseHex(hexgene)
    body_parts = ['mouth', 'eyes', 'ears', 'horn', 'back', 'tail']
    extracted_bins = {part: extract_bins(parsed_gene[part]) for part in body_parts}
    genes = convert_extracted_bins(extracted_bins)
    return genes

def parseHex(hexgene):
    hex_bin = bin(int(hexgene, 16)) # Convert hexadecimal to binary
    gene_bin_group = { # Slice the binary string into respective parts
        'cls': hex_bin[0:4],
        'region': hex_bin[8:13],
        'tag': hex_bin[13:18],
        'bodySkin': hex_bin[18:22],
        'xMas': hex_bin[22:34],
        'pattern': hex_bin[34:52],
        'color': hex_bin[52:64],
        'eyes': hex_bin[64:96],
        'mouth': hex_bin[96:128],
        'ears': hex_bin[128:160],
        'horn': hex_bin[160:192],
        'back': hex_bin[192:224],
        'tail': hex_bin[224:256]}
    return gene_bin_group

def extract_bins(part_bin):
    d_class = part_bin[2:6]
    d_bin = part_bin[6:12]
    r1_class = part_bin[12:16]
    r1_bin = part_bin[16:22]
    r2_class = part_bin[22:26]
    r2_bin = part_bin[26:32]
    return d_class, d_bin, r1_class, r1_bin, r2_class, r2_bin

def convert_extracted_bins(extracted_bins):

    class_map = { # Mapping for binary to class
        "0000": "beast",
        "0001": "bug",
        "0010": "bird",
        "0011": "plant",
        "0100": "aquatic",
        "0101": "reptile"
    }
    converted = {}
    for part, bins in extracted_bins.items(): # Convert the extracted_bins
        d_class = class_map[bins[0]]
        d_part = bins[1]
        r1_class = class_map[bins[2]]
        r1_part = bins[3]
        r2_class = class_map[bins[4]]
        r2_part = bins[5]
        d_global = gene_map[d_class][part].get(d_part, {}).get('global', 'Unknown')# Fetch the global name for each class+part combination
        r1_global = gene_map[r1_class][part].get(r1_part, {}).get('global', 'Unknown')
        r2_global = gene_map[r2_class][part].get(r2_part, {}).get('global', 'Unknown')
        converted[part] = (d_global, r1_global, r2_global) # Combine the results in a tuple
    return converted