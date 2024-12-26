import heapq
from collections import defaultdict, Counter

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

# Main Function
def main():
    # Example input
    original_string = str(input("Please enter your string : "))
    
    # Apply BWT
    bwt_result = bwt_transform(original_string)
    print(f"BWT Output: {bwt_result}")
    
    # Decode BWT
    decoded_string = bwt_inverse(bwt_result)
    print(f"Decoded String: {decoded_string}")
    
    # Apply Run-Length Encoding to BWT output
    rle_result = run_length_encoding(bwt_result)
    print(f"RLE Output: {rle_result}")
    
    # Apply Huffman Coding to BWT output
    huffman_encoded, huffman_codes = huffman_encode(bwt_result)
    print(f"Huffman Encoded Output: {huffman_encoded}")
    print(f"Huffman Codes: {huffman_codes}")
    
    # Decode Huffman Coding
    huffman_decoded = huffman_decode(huffman_encoded, huffman_codes)
    print(f"Huffman Decoded Output: {huffman_decoded}")

if __name__ == "__main__":
    main()