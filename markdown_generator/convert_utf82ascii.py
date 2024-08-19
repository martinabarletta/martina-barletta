# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:26:42 2024

@author: matil
"""

def convert_utf8_to_ascii(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='ascii') as infile, open(output_file, 'w', encoding='utf-8', errors='replace') as outfile:
            for line in infile:
                # Write the line to the output file, non-ASCII characters will be replaced
                outfile.write(line)
        print(f"Conversion complete. Output saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    input_tsv = 'publications.tsv'  # Replace with your UTF-8 TSV file path
    output_tsv = 'publications.tsv'  # Replace with the desired output file path
    convert_utf8_to_ascii(input_tsv, output_tsv)

if __name__ == "__main__":
    main()
