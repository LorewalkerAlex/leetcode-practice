# https://leetcode.cn/problems/design-browser-history/description/


class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        self.urls = self.urls[:self.idx+1]
        self.urls.append(url)
        self.idx += 1

    def back(self, steps: int) -> str:
        self.idx = max(0, self.idx-steps)
        return self.urls[self.idx]

    def forward(self, steps: int) -> str:
        self.idx = min(self.idx+steps, len(self.urls)-1)
        return self.urls[self.idx]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)