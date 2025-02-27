# https://leetcode.cn/problems/design-a-text-editor/description/


class TextEditor:

    def __init__(self):
        self.left = ''
        self.right = ''
        self.cursor = 0

    def addText(self, text: str) -> None:
        self.left += text
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        word_del = min(k, self.cursor)
        self.cursor = max(0, self.cursor-k)
        self.left = self.left[:self.cursor]

        return word_del
        

    def cursorLeft(self, k: int) -> str:
        self.cursor = max(0, self.cursor-k)
        self.right = self.left[self.cursor:] + self.right
        self.left = self.left[:self.cursor]

        return self.left[max(0, self.cursor-10):self.cursor]
        

    def cursorRight(self, k: int) -> str:
        self.cursor += min(k, len(self.right))
        self.left += self.right[:min(k, len(self.right))]
        self.right = self.right[min(k, len(self.right)):]
        
        return self.left[max(0, self.cursor-10):self.cursor]


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)