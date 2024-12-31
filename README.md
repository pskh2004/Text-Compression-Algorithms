Text Compression Algorithms Application
This is a Python-based GUI application that demonstrates various text compression algorithms, including Burrows-Wheeler Transform (BWT), Run-Length Encoding (RLE), Huffman Coding, Shannon-Fano Coding, and LZ77 Compression. The application allows users to encode a string using these algorithms or decode LZ77-compressed data.

Features

Encoding Mode:

Compresses an input string using the following algorithms:

Burrows-Wheeler Transform (BWT): Rearranges the string to make it more compressible.

Run-Length Encoding (RLE): Compresses consecutive repeated characters.

Huffman Coding: Builds a prefix-free code based on character frequencies.

Shannon-Fano Coding: Splits characters into groups based on frequencies.

LZ77 Compression: Finds repeated substrings and replaces them with references.

Decoding Mode:

Decodes LZ77-compressed data back to the original string.

User-Friendly Interface:

Provides step-by-step explanations and intermediate results for each algorithm.

Includes example inputs for decoding to guide the user.

How to Use

1. Running the Application
   
Ensure you have Python installed on your system.

Install the required libraries (if not already installed):

pip install tkinter

Run the script:

python compression_app.py

2. Using the Application

Choose Mode:

Select Encode to compress a string.

Select Decode to decompress LZ77-encoded data.

Input:

For Encoding: Enter a string in the input field (e.g., banana).

For Decoding: Enter LZ77-encoded data in the correct format (e.g., [(0, 0, 'b'), (0, 0, 'a'), (2, 1, 'n'), (3, 1, '')]).

Process:

Click the Process button to perform the selected operation.

Output:

The results will be displayed in the output frame, including intermediate steps and final output.

Algorithms Explained

1. Burrows-Wheeler Transform (BWT)
   
Purpose: Rearranges the input string to make it more compressible.

Steps:

Append a special character ($) to the string.

Generate all rotations of the string.

Sort the rotations lexicographically.

Extract the last column of the sorted rotations to get the BWT output.

2. Run-Length Encoding (RLE)
   
Purpose: Compresses consecutive repeated characters.

Steps:

Traverse the string and count consecutive repeated characters.

Replace repeated characters with the character followed by the count.

3. Huffman Coding
   
Purpose: Builds a prefix-free code based on character frequencies.

Steps:

Calculate the frequency of each character in the string.

Build a Huffman tree using a priority queue.

Traverse the tree to generate Huffman codes for each character.

Encode the string using the generated codes.

4. Shannon-Fano Coding
   
Purpose: Splits characters into groups based on frequencies.

Steps:

Calculate the frequency of each character in the string.

Sort characters by frequency in descending order.

Recursively split characters into two groups and assign binary codes.

5. LZ77 Compression
   
Purpose: Finds repeated substrings and replaces them with references.

Steps:

Traverse the string and search for the longest match in a sliding window.

Encode the match as a tuple (offset, length, next_char).

Repeat until the entire string is processed.

Example Inputs and Outputs

Encoding Example

Input: banana

Output:

BWT Output: annb$aa

RLE Output: a1n2b1$1a2

Huffman Encoded Output: 0110010110

Shannon-Fano Encoded Output: 010100110

LZ77 Encoded Output: [(0, 0, 'b'), (0, 0, 'a'), (2, 1, 'n'), (3, 1, '')]

Decoding Example

Input: [(0, 0, 'b'), (0, 0, 'a'), (2, 1, 'n'), (3, 1, '')]

Output: banana

Code Structure

1. Functions

bwt_transform(s): Applies BWT to the input string.

bwt_inverse(bwt_str): Reconstructs the original string from BWT output.

run_length_encoding(s): Applies RLE to the input string.

huffman_encode(s): Encodes the input string using Huffman Coding.

shannon_fano_encode(s): Encodes the input string using Shannon-Fano Coding.

lz77_encode(s): Compresses the input string using LZ77.

lz77_decode(encoded_data): Decodes LZ77-compressed data.

2. GUI Class
   
CompressionApp:

Handles the user interface and input/output.

Displays explanations and results in a Text widget.

Toggles between encoding and decoding modes using radio buttons.

Dependencies

Python 3.x

tkinter (included in Python standard library)

heapq, collections, ast (included in Python standard library)

Limitations

Decoding is only supported for LZ77-compressed data.

The application does not handle large inputs efficiently due to the nature of the algorithms.

Future Improvements

Add support for decoding other compression algorithms (e.g., Huffman, Shannon-Fano).

Optimize the algorithms for large inputs.

Add file compression/decompression functionality.

License

This project is open-source and available under the MIT License. Feel free to modify and distribute it as needed.

Author

pskh2004


