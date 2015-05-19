def digit_sum(n):
    result = 0
    for x in str(n):
        result += int(x)
    print(result)
  
  
digit_sum(4)