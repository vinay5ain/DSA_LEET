from collections import defaultdict


class Solution:

  def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
    n = len(items)
    min_price = min(price for _, price in items)

    factor_freq = [0] * (n + 1)
    for factor, _ in items:
      factor_freq[factor] += 1

    # multiples_count[f] = total items with factor a multiple of f
    multiples_count = [0] * (n + 1)
    for f in range(1, n + 1):
      if factor_freq[f]:
        for mult in range(f, n + 1, f):
          multiples_count[f] += factor_freq[mult]

    # Group max free items available by item price
    bonus_by_price = defaultdict(int)
    for factor, price in items:
      free_available = multiples_count[factor] - 1  # exclude self
      if free_available > 0 and price < 2 * min_price:
        bonus_by_price[price] += free_available

    total_items = 0
    for price in sorted(bonus_by_price):
      if budget < price:
        break
      max_bonus_copies = bonus_by_price[price]
      buy_cnt = min(max_bonus_copies, budget // price)
      total_items += buy_cnt * 2  # 1 purchased + 1 free per copy
      budget -= buy_cnt * price

    total_items += budget // min_price
    return total_items