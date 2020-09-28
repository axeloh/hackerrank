"""
Coin Change Problem from https://www.youtube.com/watch?v=HWW-jA6YjHk
"""



def num_coins(cents, coins):
    num_coins = 0
    # O(k)
    for coin in coins:
        num_coins += cents // coin
        cents = cents % coin
    if cents != 0:
        return -1
    return num_coins

def num_coins2(cents, coins):
    # Solution that works also when missing coins
    # For example not having nickels

    # k: number of coins
    # O(k^2)
    # k + (k-1) + (k-2) + (k-3) = O(k^2)
    min_coins = 1e8
    for i in range(len(coins)-1):
        c = cents
        coins = coins[i:]
        num_coins = 0
        for coin in coins:
            num_coins += c // coin
            c = c % coin
        if c != 0:
            continue
        if num_coins < min_coins:
            min_coins = num_coins
    if c != 0:
        return -1
    return min_coins




if __name__ == '__main__':
    cents = 31

    # quarter: 25, dime: 10, nickel: 5, pennies: 1
    coins = [25, 10, 5, 1]

    num_coins = num_coins(cents, coins)
    print(f'Found min coins: {num_coins}')
    print('-'*10)
    num_coins = num_coins2(cents, coins)
    print(f'Optimalnum_coins')