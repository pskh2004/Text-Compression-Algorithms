Text Compression Algorithms

This repository implements various text compression algorithms, including Burrows-Wheeler Transform (BWT), Run-Length Encoding (RLE), and Huffman Coding. These techniques are widely used in data compression and provide a foundation for understanding more advanced compression methods. Additionally, a Tkinter-based GUI is provided for an interactive user experience.

Features

Burrows-Wheeler Transform (BWT):

Transforms a string into a format that is more amenable to compression.

Includes both the transform and inverse transform functions.

Run-Length Encoding (RLE):

Compresses a string by replacing consecutive repeated characters with a single character and a count.

Huffman Coding:

Builds a Huffman tree based on character frequencies and generates optimal prefix codes for compression.

Includes encoding and decoding functions.

Tkinter GUI:

Provides an interactive interface for inputting a string and viewing the results of BWT, RLE, and Huffman Coding.

Displays the BWT output, RLE output, Huffman-encoded output, Huffman codes, and the decoded string.

How to Use

Command-Line Version

Clone the repository:

git clone https://github.com/pskh2004/Text-Compression-Algorithms.git

cd Text-Compression-Algorithms

Run the script:

python main.py

Enter a string when prompted. 

The program will:

Apply BWT to the input string.

Encode the BWT output using RLE.

Encode the BWT output using Huffman Coding.

Decode the Huffman-encoded output.

Reconstruct the original string using the inverse BWT.

Example:

Input:


Please enter your string : banana

Output:


BWT Output: annb$aa

Decoded String: banana

RLE Output: a1n2b1$1a2

Huffman Encoded Output: 1101111000

Huffman Codes: {'a': '11', 'n': '01', 'b': '10', '$': '00'}

Huffman Decoded Output: annb$aa

Tkinter GUI Version

Clone the repository (if not already done):



git clone https://github.com/pskh2004/Text-Compression-Algorithms.git

cd Text-Compression-Algorithms

Run the GUI script:



python tkinter_gui.py

Use the GUI:

Enter a string in the input field.

Click the "Process" button to view the results:

BWT Output

RLE Output

Huffman Encoded Output

Huffman Codes

Decoded Output

Example:

Input:

banana

Output in GUI:


BWT Output: annb$aa

RLE Output: a1n2b1$1a2

Huffman Encoded Output: 1101111000

Huffman Codes: {'a': '11', 'n': '01', 'b': '10', '$': '00'}

Decoded Output: banana

Requirements:

Python 3.x

Tkinter (usually included with Python)

License:

This project is licensed under the MIT License. See the LICENSE file for details.

Contributing:

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

Author
Pskh2004
