import heapq
from collections import defaultdict, Counter
import tkinter as tk
from tkinter import ttk, messagebox

# BWT Transform
def bwt_transform(s):
    """Apply Burrows-Wheeler Transform to the input string."""
    s = s + '$'
    rotations = [s[i:] + s[:i] for i in range(len(s))]
    rotations_sorted = sorted(rotations)
    bwt_output = ''.join([rotation[-1] for rotation in rotations_sorted])
    return bwt_output

# BWT Inverse
def bwt_inverse(bwt_str):
    """Reconstruct the original string from the BWT output."""
    table = [''] * len(bwt_str)
    for _ in range(len(bwt_str)):
        table = sorted([bwt_str[i] + table[i] for i in range(len(bwt_str))])
    for row in table:
        if row.endswith('$'):
            return row.rstrip('$')

# Run-Length Encoding
def run_length_encoding(s):
    """Apply Run-Length Encoding to the input string."""
    if not s:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    return ''.join(compressed)

# Huffman Coding
class HuffmanNode:
    """Class to represent a node in the Huffman tree."""
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_map):
    """Build the Huffman tree from the frequency map."""
    heap = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]

def build_huffman_codes(node, prefix="", code_map=None):
    """Build Huffman codes by traversing the Huffman tree."""
    if code_map is None:
        code_map = {}
    if node:
        if node.char is not None:
            code_map[node.char] = prefix
        build_huffman_codes(node.left, prefix + "0", code_map)
        build_huffman_codes(node.right, prefix + "1", code_map)
    return code_map

def huffman_encode(s):
    """Encode the input string using Huffman coding."""
    if not s:
        return "", {}
    freq_map = Counter(s)
    huffman_tree = build_huffman_tree(freq_map)
    huffman_codes = build_huffman_codes(huffman_tree)
    encoded_output = ''.join([huffman_codes[char] for char in s])
    return encoded_output, huffman_codes

def huffman_decode(encoded_output, huffman_codes):
    """Decode the Huffman-encoded string using the Huffman codes."""
    reverse_codes = {code: char for char, code in huffman_codes.items()}
    current_code = ""
    decoded_output = ""
    for bit in encoded_output:
        current_code += bit
        if current_code in reverse_codes:
            decoded_output += reverse_codes[current_code]
            current_code = ""
    return decoded_output

# Shannon-Fano Coding
def shannon_fano_encode(s):
    """Encode the input string using Shannon-Fano coding."""
    if not s:
        return "", {}

    # Calculate character frequencies
    freq_map = Counter(s)
    sorted_chars = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True)

    # Build Shannon-Fano codes
    def build_shannon_fano_codes(characters, prefix=""):
        if len(characters) == 1:
            return {characters[0]: prefix}
        mid = len(characters) // 2
        left_codes = build_shannon_fano_codes(characters[:mid], prefix + "0")
        right_codes = build_shannon_fano_codes(characters[mid:], prefix + "1")
        return {**left_codes, **right_codes}

    shannon_fano_codes = build_shannon_fano_codes(sorted_chars)
    encoded_output = ''.join([shannon_fano_codes[char] for char in s])
    return encoded_output, shannon_fano_codes

def shannon_fano_decode(encoded_output, shannon_fano_codes):
    """Decode the Shannon-Fano-encoded string using the Shannon-Fano codes."""
    reverse_codes = {code: char for char, code in shannon_fano_codes.items()}
    current_code = ""
    decoded_output = ""
    for bit in encoded_output:
        current_code += bit
        if current_code in reverse_codes:
            decoded_output += reverse_codes[current_code]
            current_code = ""
    return decoded_output

# LZ77 Compression
def lz77_encode(s):
    """Apply LZ77 Compression to the input string."""
    encoded = []
    buffer_size = 100
    i = 0
    while i < len(s):
        match = (0, 0, s[i])
        for j in range(max(0, i - buffer_size), i):
            k = 0
            while i + k < len(s) and s[j + k] == s[i + k]:
                k += 1
            if k > match[1]:
                match = (i - j, k, s[i + k] if i + k < len(s) else '')
        encoded.append(match)
        i += match[1] + 1
    return encoded

def lz77_decode(encoded_data):
    """Decode LZ77-encoded data."""
    decoded = []
    for item in encoded_data:
        offset, length, char = item
        if length > 0:
            start = len(decoded) - offset
            for i in range(length):
                decoded.append(decoded[start + i])
        decoded.append(char)
    return decoded

# Tkinter UI
class CompressionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Compression Algorithms")
        self.root.geometry("800x600")

        # Input Frame
        self.input_frame = ttk.LabelFrame(root, text="Input String")
        self.input_frame.pack(padx=10, pady=10, fill="x")

        self.input_entry = ttk.Entry(self.input_frame, width=50)
        self.input_entry.pack(padx=10, pady=10)

        self.process_button = ttk.Button(self.input_frame, text="Process", command=self.process_input)
        self.process_button.pack(pady=10)

        # Output Frame
        self.output_frame = ttk.LabelFrame(root, text="Output")
        self.output_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.bwt_label = ttk.Label(self.output_frame, text="BWT Output:")
        self.bwt_label.pack(anchor="w", padx=10, pady=5)

        self.decoded_label = ttk.Label(self.output_frame, text="Decoded String:")
        self.decoded_label.pack(anchor="w", padx=10, pady=5)

        self.rle_label = ttk.Label(self.output_frame, text="RLE Output:")
        self.rle_label.pack(anchor="w", padx=10, pady=5)

        self.huffman_label = ttk.Label(self.output_frame, text="Huffman Encoded Output:")
        self.huffman_label.pack(anchor="w", padx=10, pady=5)

        self.huffman_codes_label = ttk.Label(self.output_frame, text="Huffman Codes:")
        self.huffman_codes_label.pack(anchor="w", padx=10, pady=5)

        self.shannon_fano_label = ttk.Label(self.output_frame, text="Shannon-Fano Encoded Output:")
        self.shannon_fano_label.pack(anchor="w", padx=10, pady=5)

        self.shannon_fano_codes_label = ttk.Label(self.output_frame, text="Shannon-Fano Codes:")
        self.shannon_fano_codes_label.pack(anchor="w", padx=10, pady=5)

        self.lz77_label = ttk.Label(self.output_frame, text="LZ77 Encoded Output:")
        self.lz77_label.pack(anchor="w", padx=10, pady=5)

        self.q_button = ttk.Button(self.output_frame, text="Quit", command=self.root.destroy).pack(pady=10)

    def process_input(self):
        """Process the input string and display the results."""
        input_string = self.input_entry.get()
        if not input_string:
            messagebox.showerror("Error", "Please enter a string.")
            return

        # Apply BWT
        bwt_result = bwt_transform(input_string)
        self.bwt_label.config(text=f"BWT Output: {bwt_result}")

        # Decode BWT
        decoded_string = bwt_inverse(bwt_result)
        self.decoded_label.config(text=f"Decoded String: {decoded_string}")

        # Apply Run-Length Encoding
        rle_result = run_length_encoding(bwt_result)
        self.rle_label.config(text=f"RLE Output: {rle_result}")

        # Apply Huffman Coding
        huffman_encoded, huffman_codes = huffman_encode(input_string)
        self.huffman_label.config(text=f"Huffman Encoded Output: {huffman_encoded}")
        self.huffman_codes_label.config(text=f"Huffman Codes: {huffman_codes}")

        # Apply Shannon-Fano Coding
        shannon_fano_encoded, shannon_fano_codes = shannon_fano_encode(input_string)
        self.shannon_fano_label.config(text=f"Shannon-Fano Encoded Output: {shannon_fano_encoded}")
        self.shannon_fano_codes_label.config(text=f"Shannon-Fano Codes: {shannon_fano_codes}")

        # Apply LZ77
        lz77_encoded = lz77_encode(input_string)
        self.lz77_label.config(text=f"LZ77 Encoded Output: {lz77_encoded}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CompressionApp(root)
    root.mainloop()