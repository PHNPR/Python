import heapq
from collections import defaultdict

class BinaryTreeNode:
    def __init__(self, data, char=''):
        self.data = data
        self.char = char
        self.is_leaf = char != ''
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.data < other.data

def take_input():
    print("# ENTER TEXT : ")
    return input()

def freq_array(s):
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    return freq

def fill_map(root, char_to_code, code_to_char, code):
    if not root:
        return
    if root.is_leaf:
        char_to_code[root.char] = code
        code_to_char[code] = root.char
        return
    fill_map(root.left, char_to_code, code_to_char, code + "0")
    fill_map(root.right, char_to_code, code_to_char, code + "1")

def get_code(s):
    for char in s:
        print(ord(char) - 48, end='')

def encode(text, char_to_code):
    print("encoded code: ", end='')
    missing_chars = []
    for char in text:
        if char not in char_to_code:
            missing_chars.append(char)
            continue
        get_code(char_to_code[char])
    print()
    if missing_chars:
        print(f"Letters: {', '.join(missing_chars)} are not available.")
    print("\n")

def decode(text, code_to_char):
    print("decoded text: ", end='')
    j = 0
    for i in range(len(text)):
        code = text[j:i+1]
        if code in code_to_char:
            print(code_to_char[code], end='')
            j = i + 1
    print()

def huffman_code():
    while True:
        text = take_input()
        freq = freq_array(text)

        heap = []
        for char, count in freq.items():
            heapq.heappush(heap, BinaryTreeNode(count, char))

        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)
            root = BinaryTreeNode(node1.data + node2.data)
            root.left = node1
            root.right = node2
            heapq.heappush(heap, root)

        root = heapq.heappop(heap)
        char_to_code = {}
        code_to_char = {}
        fill_map(root, char_to_code, code_to_char, "")

        encode(text, char_to_code)

        print("code for each character: ")
        for char, code in char_to_code.items():
            print(f"{char} : {code}")
        print()

        while True:
            print("Enter 1 to encode, 2 to decode & -1 to stop : ", end='')
            try:
                k = int(input())
                if k == -1:
                    print("\n\n")
                    break
                elif k not in [1, 2]:
                    print("Enter appropriate value ")
                    continue
            except ValueError:
                print("Enter appropriate value ")
                continue

            print("Enter text: ", end='')
            input_text = input()

            if k == 1:
                encode(input_text, char_to_code)
            elif k == 2:
                decode(input_text, code_to_char)

if __name__ == "__main__":
    huffman_code()