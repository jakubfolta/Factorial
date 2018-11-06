def factor(num):
  if num == 0:
    return 1
  firstDig = 1
  while num > 0:
    firstDig = firstDig * num
    num = num - 1
  return firstDig

print(factor(6))
