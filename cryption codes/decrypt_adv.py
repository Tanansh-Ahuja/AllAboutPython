a={'<': '$', 'o': 'v', ' ': 'Y', 'Z': '0', 'i': 'F', 'r': '?', '\\': '5', 'X': 'V', 'M': '(', ')': 'B', 'z': 'e', 'e': 'S', '@': ':', '6': 'b', 'P': 'C', '|': 'A', 'C': 'P', 'v': '=', '_': '{', 'a': '<', "'": ',', 'J': '9', '5': '+', 'H': '7', '3': '&', '&': '@', '~': '!',
   'T': '2', '{': '"', 'D': '3', 'j': "'", 'm': 'p', 'I': '^', 's': 'Z', 'F': '[', 'L': 'W', 'w': 'T', 'h': '%', 'p': '#', '9': 'l', '=': 'R', 'S': '\\', 'y': 'g', '+': '|', '%': '1', 'O': 'U', 'u': '*', '(': '>', 'Q': 'N', '7': 'y', 'B': 'h', 'd': 'z', 'Y': 'M', 'f': ']', 't': '8',
   '8': ';', 'c': '4', 'N': 'I', '[': 'q', 'U': 'a', '`': 'E', ',': 'n', '^': 'G', '4': 'f', '?': 's', '1': 'i', '*': 'O', '-': ')', 'l': '/', '}': '6', '2': 'K', 'q': ' ', 'K': '~', '!': '.', 'E': 'Q', 'k': 'L', '#': 'k', ':': 'H', 'g': 'J', '>': 'c', 'n': '`', 'b': 'o', '/': 'D', 'A': 't',
   ';': 'x', 'W': '-', 'R': '}', 'x': 'u', 'G': 'j', 'V': 'm', '0': 'r', '"': 'w', '.': 'd', ']': 'X', '$': '_'}
while 1:
    b=input("Enter: ")
    c=""
    for i in b:
        c=c+a.get(i)
    print(c)