def count ( denominations , price ):
    if price == 0 :
        return 1
    elif price < 0 :
        return 0

    ways = 0
    for index in denominations : ways += count ( denominations , price - index )
    return ways

denominations = [ 1, 2, 5 ]
price = 20
print('ways =', count ( denominations , price ) )