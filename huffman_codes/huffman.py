"""
Python 3 implementation of greedy algorithm that constructs an optimal prefix
Huffman's codes.

Resources:
* "Introduction to Algorithms", T.H. Cormen et al.
* "Python Algorithms", M.L. Hetland
"""

from itertools import count
from heapq import heapify, heappush, heappop

def read_codes (inp="huffman.txt"):
    """
    Reads file containing frequencies/weigths of symbols. Returns list of tuples
    in which first element is symbol frequency/weight, second one is unique
    number (to brake ties in case of equal frequencies) and third one is a
    symbol itself. The input file has following format:
    [symbol][frequency]
    """
    codes = []
    ties_breaker = 1
    with open(inp) as inp:
        for line in inp:
            frequency = int(line.split()[1])
            symbol = line.split()[0]
            codes.append((frequency, ties_breaker, symbol))
            ties_breaker += 1
    return codes

def initialize_heap(codes):
    """
    Inserts all codes in the codes list into the heap.
    """
    trees = []
    for item in codes:
        heappush(trees, item)
    return trees

def huffman(codes):
    """
    Constructs Huffman Codes tree.
    """
    num = count(1000)
    num_of_steps = len(codes)
    trees = initialize_heap(codes)
    for step in range(num_of_steps-1):
        weight_l, _, left = heappop(trees)
        weight_r, _, right = heappop(trees)
        n = next(num)
        new = (weight_l+weight_r, n, [left, right])
        heappush(trees, new)
    return trees[0][-1]

def extract_codes(tree, prefix=''):
    """
    Extracts Huffman codes from Huffman tree.
    """
    if isinstance(tree, str) == 1:
        yield (tree, prefix)
        return
    for bit, child in zip("01", tree):
        for pair in extract_codes(child, prefix+bit):
            yield pair

def min_max_codes(binary_codes):
    """
    Returns the maximum and minimum length of a codeword among Huffman codes.
    """
    res = set([])
    for el in binary_codes:
        res.add(len(el[1]))
    results = list(res)
    smallest, biggest = min(results), max(results)
    return smallest, biggest

def print_encodings(encodings):
    """
    Print symbols and corresponding prefix free binary codes.
    """
    for encoding in sorted(encodings):
        print('{:<5} {:<10}'.format(encoding[0], encoding[1]))

def main():
    codes = read_codes()
    tree = huffman(codes)
    binary_codes = list(extract_codes(tree))
    print_encodings(binary_codes)
    print('Min encoding len: {}\nMax encoding len: {}'.format(min_max_codes(binary_codes)[0],
                                                              min_max_codes(binary_codes)[1]))
if __name__ == "__main__":
    main()
    
