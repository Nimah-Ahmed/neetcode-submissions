from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 1. Create a set of all words = wordList + beginWord
        wordList_set = set(wordList).union({beginWord})
        print(wordList_set)

        # 2. Create an undirected graph
        graph = {}
        letters = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
        for word in wordList_set:
            for i in range(len(word)):
                for letter in letters:
                    if word[:i] + letter + word[i+1:] in wordList_set:
                        if word in graph:
                            graph[word].add(word[:i] + letter + word[i+1:])
                        else:
                            graph[word] = {word[:i] + letter + word[i+1:]}
                        if word[:i] + letter + word[i+1:] in graph:
                            graph[word[:i] + letter + word[i+1:]].add(word)
                        else:
                            graph[word[:i] + letter + word[i+1:]] = {word}
        
        # 3. Run BFS on undirected graph
        visited = {beginWord:0}
        queue = deque([(beginWord, 0)])

        while queue:
            current_node, level_number = queue.popleft()
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited[neighbor] = level_number + 1
                    queue.append((neighbor, level_number + 1))
        
        # 4. Return minimum path length
        if endWord in visited:
            return visited[endWord] + 1
        else:
            return 0

