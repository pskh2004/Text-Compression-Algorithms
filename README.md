Text Compression Algorithms

This repository contains a Python-based GUI application for exploring various text compression algorithms. The project demonstrates the implementation and use of popular text compression techniques, enabling users to visualize how these algorithms transform and compress data.

Repository Overview

GUI Application: A Tkinter-based GUI to process text inputs and display outputs for each compression algorithm.

Algorithms Implemented:

Burrows-Wheeler Transform (BWT)

Run-Length Encoding (RLE)

Huffman Coding

Shannon-Fano Coding

LZ77 Compression

Features

1. Burrows-Wheeler Transform (BWT)

Description: Rearranges a string into a permutation that is more amenable to compression.

Usage:

Transforms an input string.

Reconstructs the original string from the transformed data.

2. Run-Length Encoding (RLE)

Description: Compresses data by replacing consecutive repeating characters with a single character and a count.

Usage:

Compresses the output of the BWT for further space optimization.

3. Huffman Coding

Description: Uses a frequency-based binary tree to encode characters in a string, achieving optimal compression.

Usage:

Encodes the string into a binary representation.

Generates a dictionary of Huffman codes for decoding.

4. Shannon-Fano Coding

Description: An early entropy encoding algorithm that assigns binary codes based on character frequency.

Usage:

Encodes the string using Shannon-Fano rules.

Provides a map of character codes for decoding.

5. LZ77 Compression

Description: Uses a sliding window to identify and encode repeating substrings.

Usage:

Compresses the input string using offset-length pairs.

6. Graphical User Interface

Built With: Tkinter

Features:

Input text field for user data.

Buttons to process and quit the application.

Display area for the output of each algorithm.

Installation

1.Clone the repository:

git clone https://github.com/pskh2004/Text-Compression-Algorithms.git

cd Text-Compression-Algorithms

2.Ensure Python 3.x is installed on your system.

3.Install dependencies (if necessary):

pip install tk

Usage

1.Run the application:

python main.py

2.Enter your desired text in the input field.

3.Click Process to view:

Burrows-Wheeler Transform results.

Run-Length Encoded string.

Huffman-encoded binary string and codes.

Shannon-Fano-encoded binary string and codes.

LZ77 Encoded data.

Observe the outputs displayed in the output section.

4.To exit, click Quit.


Code Details

File: main.py

Algorithm Implementations:

BWT Transform: Functions bwt_transform and bwt_inverse.

Run-Length Encoding: Function run_length_encoding.

Huffman Coding:

Functions huffman_encode and huffman_decode.

Tree construction using HuffmanNode and build_huffman_tree.

Shannon-Fano Coding: Functions shannon_fano_encode and shannon_fano_decode.

LZ77 Compression:

Functions lz77_encode and lz77_decode.

GUI Components:

Built using the Tkinter library.

Input and output are organized using frames and labels.

Buttons for interaction.

Example Outputs

Input: abracadabra

Outputs

BWT Output: ard$rcaaaabb

Decoded String: abracadabra

RLE Output: a1r1d1$1r1c1a3b2

Huffman Encoded Output: 101011011... (varies by input frequency)

Shannon-Fano Encoded Output: 010110110... (varies by input frequency)

LZ77 Encoded Output: [(0, 0, 'a'), (0, 0, 'b'), ...]


Contributing

Contributions are welcome! If you'd like to contribute:

1.Fork this repository.

2.Create a feature branch:
 
git checkout -b feature/your-feature

3.Commit your changes:
 
git commit -m "Add your feature"

4.Push to your branch:
 
git push origin feature/your-feature

5.Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.
