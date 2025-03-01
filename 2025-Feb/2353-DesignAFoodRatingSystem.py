# https://leetcode.cn/problems/design-a-food-rating-system/


from typing import List
from collections import defaultdict
import heapq
from sortedcontainers import SortedList

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_map = {}
        self.cuisine_map = defaultdict(SortedList)  # sortedcontainers
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_map[food] = [rating, cuisine]
            # 取负号，保证 rating 相同时，字典序更小的 food 排在前面
            self.cuisine_map[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        rating, cuisine = self.food_map[food]
        sl = self.cuisine_map[cuisine]
        sl.discard((-rating, food))  # 移除旧数据
        sl.add((-newRating, food))  # 添加新数据
        self.food_map[food][0] = newRating  # 更新 food 的 rating

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_map[cuisine][0][1]
    

class FoodRatings2:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_map = {}
        self.cuisine_map = defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_map[food] = [rating, cuisine]
            self.cuisine_map[cuisine].append((-rating, food))
        # 这样可以保证初始化是线性复杂度
        for h in self.cuisine_map.values():
            heapq.heapify(h)

    def changeRating(self, food: str, newRating: int) -> None:
        p = self.food_map[food]
        # 直接添加新数据，后面 highestRated 再删除旧的
        heapq.heappush(self.cuisine_map[p[1]], (-newRating, food))
        p[0] = newRating

    def highestRated(self, cuisine: str) -> str:
        h = self.cuisine_map[cuisine]
        # 堆顶的食物评分不等于其实际值
        while -h[0][0] != self.food_map[h[0][1]][0]:
            heapq.heappop(h)
        return h[0][1]
