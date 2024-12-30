Text Compression Algorithms with Tkinter GUI
This repository implements various text compression algorithms, including Burrows-Wheeler Transform (BWT), Run-Length Encoding (RLE), Huffman Coding, Delta Encoding, and LZ77 Compression. These techniques are widely used in data compression and provide a foundation for understanding more advanced compression methods. Additionally, a Tkinter-based GUI is provided for an interactive user experience.

Features
1.Burrows-Wheeler Transform (BWT):

Transforms a string into a format that is more amenable to compression.

Includes both the transform and inverse transform functions.

2.Run-Length Encoding (RLE):

Compresses a string by replacing consecutive repeated characters with a single character and a count.

3.Huffman Coding:

Builds a Huffman tree based on character frequencies and generates optimal prefix codes for compression.

Includes encoding and decoding functions.

4.Delta Encoding:

Compresses a list of integers by encoding the differences between consecutive values.

5.LZ77 Compression:

A sliding window-based compression algorithm that replaces repeated sequences with references to previous occurrences.

6.Tkinter GUI:

Provides an interactive interface for inputting a string and viewing the results of BWT, RLE, Huffman Coding, Delta Encoding, and LZ77 Compression.

Displays the BWT output, decoded string, RLE output, Huffman-encoded output, Huffman codes, Delta-encoded output, and LZ77-encoded output.



How to Use

Prerequisites

1.Python 3.x: Ensure Python is installed on your system.

2.Tkinter: Usually included with Python.

If not, install it using your package manager.

3.Pillow: For image display (if needed).

Install it using pip:

pip install pillow

Running the Application

1.Clone the repository:

git clone https://github.com/pskh2004/Text-Compression-Algorithms.git

cd Text-Compression-Algorithms

2.Run the script:

python main.py

3.Use the GUI:

Enter a string in the input field.

Click the "Process" button to view the results:

BWT Output

Decoded String

RLE Output

Huffman Encoded Output

Huffman Codes

Delta Encoded Output

LZ77 Encoded Output

Click the "Quit" button to close the application.

Example Workflow

Enter a string (e.g., "banana").

Click "Process".

View the results:

BWT Output: annb$aa

Decoded String: banana

RLE Output: a1n2b1$1a2

Huffman Encoded Output: Binary representation.

Huffman Codes: Mapping of characters to binary codes.

Delta Encoded Output: List of delta values.

LZ77 Encoded Output: List of tuples representing LZ77 compression.

Code Structure

1.bwt_transform(s): Applies the Burrows-Wheeler Transform to the input string.

2.bwt_inverse(bwt_str): Reconstructs the original string from the BWT output.

3.run_length_encoding(s): Applies Run-Length Encoding to the input string.

4.HuffmanNode: Represents a node in the Huffman tree.

5.build_huffman_tree(freq_map): Builds the Huffman tree from the frequency map.

6.build_huffman_codes(node, prefix, code_map): Builds Huffman codes by traversing the Huffman tree.

7.huffman_encode(s): Encodes the input string using Huffman coding.

8.huffman_decode(encoded_output, huffman_codes): Decodes the Huffman-encoded string using the Huffman codes.

9.delta_encode(data): Applies Delta Encoding to the input data.

10.delta_decode(encoded_data): Decodes Delta-encoded data.

11.lz77_encode(s): Applies LZ77 Compression to the input string.

12.lz77_decode(encoded_data): Decodes LZ77-encoded data.

13.CompressionApp: Tkinter GUI class for interacting with the compression algorithms.

License:

This project is licensed under the MIT License. See the LICENSE file for details.

Contributing:

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

Author,
Pskh2004

