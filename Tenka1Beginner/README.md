[Tasks](https://tenka1-2018-beginner.contest.atcoder.jp/assignments)
# Measure
construct reverse std::base_string using
```string name(v.rbegin(), v.rend());```
not work well

# Exchange
function out the exchange logic
decide player position by the odd/even of K

# Align
1. sorting
2. 
  - start from  min, pick max1, max2 to place left, right hand side, recur
  - start from max, ...
3. pick the larger one from 2
(not pass)

## Ref
1. sorting
2. (construction) put the max in the middle
3. 
  - pick min/max from the remain
  - calculate the increment of sum when put in the left/right of the chosen elements
  - recur to end
* first consider to construct a queue than sum
* but sum can be calculated on the fly, so one vector is enough
