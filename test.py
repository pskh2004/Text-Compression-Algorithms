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
    return bwt_output, rotations, rotations_sorted

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
    return encoded_output, huffman_codes, freq_map

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
    return encoded_output, shannon_fano_codes, freq_map

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

# Tkinter UI
class CompressionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Compression Algorithms")
        self.root.geometry("1000x800")

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

        # Text widget to display explanations and steps
        self.explanation_text = tk.Text(self.output_frame, wrap="word", height=30)
        self.explanation_text.pack(padx=10, pady=10, fill="both", expand=True)

        self.q_button = ttk.Button(self.output_frame, text="Quit", command=self.root.destroy).pack(pady=10)

    def process_input(self):
        """Process the input string and display the results."""
        input_string = self.input_entry.get()
        if not input_string:
            messagebox.showerror("Error", "Please enter a string.")
            return

        # Clear previous explanations
        self.explanation_text.delete(1.0, tk.END)

        # Step 1: BWT
        self.explanation_text.insert(tk.END, "=== Burrows-Wheeler Transform (BWT) ===\n")
        self.explanation_text.insert(tk.END, "BWT rearranges the input string by sorting all its rotations.\n")
        bwt_result, rotations, rotations_sorted = bwt_transform(input_string)
        self.explanation_text.insert(tk.END, f"Rotations:\n{rotations}\n")
        self.explanation_text.insert(tk.END, f"Sorted Rotations:\n{rotations_sorted}\n")
        self.explanation_text.insert(tk.END, f"BWT Output: {bwt_result}\n\n")

        # Step 2: Huffman Coding
        self.explanation_text.insert(tk.END, "=== Huffman Coding ===\n")
        self.explanation_text.insert(tk.END, "Huffman Coding builds a prefix-free code based on character frequencies.\n")
        huffman_encoded, huffman_codes, freq_map = huffman_encode(input_string)
        self.explanation_text.insert(tk.END, f"Frequency Map: {freq_map}\n")
        self.explanation_text.insert(tk.END, f"Huffman Codes: {huffman_codes}\n")
        self.explanation_text.insert(tk.END, f"Encoded Output: {huffman_encoded}\n\n")

        # Step 3: Shannon-Fano Coding
        self.explanation_text.insert(tk.END, "=== Shannon-Fano Coding ===\n")
        self.explanation_text.insert(tk.END, "Shannon-Fano Coding splits characters into groups based on frequencies.\n")
        shannon_fano_encoded, shannon_fano_codes, freq_map = shannon_fano_encode(input_string)
        self.explanation_text.insert(tk.END, f"Frequency Map: {freq_map}\n")
        self.explanation_text.insert(tk.END, f"Shannon-Fano Codes: {shannon_fano_codes}\n")
        self.explanation_text.insert(tk.END, f"Encoded Output: {shannon_fano_encoded}\n\n")

        # Step 4: LZ77 Compression
        self.explanation_text.insert(tk.END, "=== LZ77 Compression ===\n")
        self.explanation_text.insert(tk.END, "LZ77 finds repeated substrings and replaces them with references.\n")
        lz77_encoded = lz77_encode(input_string)
        self.explanation_text.insert(tk.END, f"Encoded Output: {lz77_encoded}\n\n")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CompressionApp(root)
    root.mainloop()


