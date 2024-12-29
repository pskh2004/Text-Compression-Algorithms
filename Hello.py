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

# Tkinter UI
class BWTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BWT, RLE, and Huffman Coding")
        self.root.geometry("600x400")

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

        self.rle_label = ttk.Label(self.output_frame, text="RLE Output:")
        self.rle_label.pack(anchor="w", padx=10, pady=5)

        self.huffman_label = ttk.Label(self.output_frame, text="Huffman Encoded Output:")
        self.huffman_label.pack(anchor="w", padx=10, pady=5)

        self.huffman_codes_label = ttk.Label(self.output_frame, text="Huffman Codes:")
        self.huffman_codes_label.pack(anchor="w", padx=10, pady=5)

        self.decoded_label = ttk.Label(self.output_frame, text="Decoded Output:")
        self.decoded_label.pack(anchor="w", padx=10, pady=5)

        self.quit = ttk.Button(self.output_frame, text="Quit", command=self.root.destroy)
        self.quit.pack(pady=10)

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
        self.decoded_label.config(text=f"Decoded Output: {decoded_string}")

        # Apply Run-Length Encoding
        rle_result = run_length_encoding(bwt_result)
        self.rle_label.config(text=f"RLE Output: {rle_result}")

        # Apply Huffman Coding
        huffman_encoded, huffman_codes = huffman_encode(bwt_result)
        self.huffman_label.config(text=f"Huffman Encoded Output: {huffman_encoded}")
        self.huffman_codes_label.config(text=f"Huffman Codes: {huffman_codes}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BWTApp(root)
    root.mainloop()