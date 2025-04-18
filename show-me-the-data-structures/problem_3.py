import heapq
from collections import defaultdict
from typing import Optional

    
# Huffman Tree Node
class HuffmanNode:
    """
    A class to represent a node in the Huffman Tree.

    Attributes:
    -----------
    char : Optional[str]
        The character stored in the node.
    freq : int
        The frequency of the character.
    left : Optional[HuffmanNode]
        The left child node.
    right : Optional[HuffmanNode]
        The right child node.
    """

    def __init__(self, freq: int, char: Optional[str]=None) -> None:
        """
        Constructs all the necessary attributes for the HuffmanNode object.

        Parameters:
        -----------
        char : Optional[str]
            The character stored in the node.
        freq : int
            The frequency of the character.
        """
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        """
        Less-than comparison operator for HuffmanNode.

        Parameters:
        -----------
        other : HuffmanNode
            The other HuffmanNode to compare with.

        Returns:
        --------
        bool
            True if the frequency of this node is less than the other node, False otherwise.
        """
        return self.freq < other.freq
            

def calculate_frequencies(data: str) -> dict[str, int]:
    """
    Calculate the frequency of each character in the given data.

    Parameters:
    -----------
    data : str
        The input string for which frequencies are calculated.

    Returns:
    --------
    Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.
    """
    freq_str = defaultdict(int)
    data = data.strip()
    for i in data:
        freq_str[i]= freq_str[i] + 1
    return freq_str

def build_huffman_tree(frequency: dict[str, int]) -> HuffmanNode:
    """
    Build the Huffman Tree based on the character frequencies.

    Parameters:
    -----------
    frequency : Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.

    Returns:
    --------
    HuffmanNode
        The root node of the constructed Huffman Tree.
    """
    priority_queue = []
    for key, freq in frequency.items():
        heapq.heappush(priority_queue, HuffmanNode(freq, key))
    
    if len(priority_queue) < 2:
        return priority_queue[0]
    node = None
    while priority_queue:
        first = heapq.heappop(priority_queue)
        if priority_queue:
            second = heapq.heappop(priority_queue)
            freq = first.freq + second.freq
            node = HuffmanNode(freq)
            node.left = first
            node.right = second
            heapq.heappush(priority_queue, node)
        else:
            node = first
    return node




def generate_huffman_codes(node: Optional[HuffmanNode], code: str, huffman_codes: dict[str, str]) -> None:
    """
    Generate Huffman codes for each character by traversing the Huffman Tree.

    Parameters:
    -----------
    node : Optional[HuffmanNode]
        The current node in the Huffman Tree.
    code : str
        The current Huffman code being generated.
    huffman_codes : Dict[str, str]
        A dictionary to store the generated Huffman codes.
    """
    if node is None:
        return None
    
    if node.left is None and node.right is None:
        huffman_codes[node.char] = code
        return

    generate_huffman_codes(node.left, code=code+"0", huffman_codes=huffman_codes)
    generate_huffman_codes(node.right,code=code+"1", huffman_codes=huffman_codes)   

def huffman_encoding(data: str) -> tuple[str, Optional[HuffmanNode]]:
    """
    Encode the given data using Huffman coding.

    Parameters:
    -----------
    data : str
        The input string to be encoded.

    Returns:
    --------
    Tuple[str, Optional[HuffmanNode]]
        A tuple containing the encoded string and the root of the Huffman Tree.
    """
    freq = calculate_frequencies(data)
    node = build_huffman_tree(freq)
    coded = ""
    huffman_codes = {}
    generate_huffman_codes(node,coded,huffman_codes)
    s = ""
    for x in data:
        s += huffman_codes[x]
    return (s, node)

def huffman_decoding(encoded_data: str, tree: Optional[HuffmanNode]) -> str:
    """
    Decode the given encoded data using the Huffman Tree.

    Parameters:
    -----------
    encoded_data : str
        The encoded string to be decoded.
    tree : Optional[HuffmanNode]
        The root of the Huffman Tree used for decoding.

    Returns:
    --------
    str
        The decoded string.
    """
    if not tree:
        return ""
    decoded_data = []
    current_node = tree
    for digit in encoded_data:
        current_node = current_node.left if digit == "0" else current_node.right
        if current_node.left is None and current_node.right is None:
            # we append the data and start from the root
            decoded_data.append(current_node.char)
            current_node = tree
    # this is more efficient than   
    return "".join(decoded_data)  
        


# Main Function
if __name__ == "__main__":
    # Test Case 1: Standard test case
    print("\nTest Case 1: Standard sentence")
    sentence = "Huffman coding is fun!"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 2
    pass

    # Test Case 3
    pass

