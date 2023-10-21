import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # Calculate character frequencies
    char_freq = Counter(text)
    # Create a priority queue (min-heap)
    priority_queue = [HuffmanNode(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(priority_queue)

    # Build Huffman tree
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def build_huffman_codes(node, current_code, huffman_codes):
    if node is None:
        return

    if node.char is not None:
        huffman_codes[node.char] = current_code
        return

    build_huffman_codes(node.left, current_code + '0', huffman_codes)
    build_huffman_codes(node.right, current_code + '1', huffman_codes)

def huffman_encoding(text):
    root = build_huffman_tree(text)
    huffman_codes = {}
    build_huffman_codes(root, '', huffman_codes)
    encoded_text = ''.join(huffman_codes[char] for char in text)
    return encoded_text, root

def huffman_decoding(encoded_text, root):
    decoded_text = []
    current_node = root
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text.append(current_node.char)
            current_node = root

    return ''.join(decoded_text)

if __name__ == "__main__":
    input_text = input("Enter a string of text: ")

    # Encoding
    encoded_text, huffman_tree = huffman_encoding(input_text)

    # Decoding
    decoded_text = huffman_decoding(encoded_text, huffman_tree)

    # Display results
    print("Original text:", input_text)
    print("Encoded text:", encoded_text)
    print("Decoded text:", decoded_text)

    # Check if the compression worked
    if input_text == decoded_text:
        print("Compression is successful.")
    else:
        print("Compression is not successful.")