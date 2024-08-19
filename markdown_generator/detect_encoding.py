# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:26:42 2024

@author: matil
"""

import chardet

def detect_file_encoding(file_path):
    # Read a portion of the file to detect encoding
    with open(file_path, 'rb') as file:
        raw_data = file.read(10000)  # Read first 10 KB
        result = chardet.detect(raw_data)
        
    encoding = result['encoding']
    confidence = result['confidence']

    return encoding, confidence

def main():
    tsv_file = 'talks.tsv'  # Replace with your TSV file path
    encoding, confidence = detect_file_encoding(tsv_file)

    if encoding:
        print(f"Detected encoding: {encoding} with {confidence*100:.2f}% confidence.")
    else:
        print("Could not detect encoding.")

if __name__ == "__main__":
    main()
