# https://www.acmicpc.net/problem/5052

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head

        flag = True
        for char in string:
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
                flag = False
            cur_node = cur_node.children[char]
            if cur_node.data != None:
                return True
        if flag:
            return True
        cur_node.data = string
        return False

if __name__ == '__main__':
    from sys import stdin
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        trie = Trie()
        answer = "YES"
        for i in range(n):
            if trie.insert(stdin.readline().strip()):
                answer = "NO"
        print(answer)