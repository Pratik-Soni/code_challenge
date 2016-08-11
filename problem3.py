'''
@author: Pratik Soni
'''

def max_value(coin):
    """
    function to calculate max exchange for coin
    parameter : coin
    return : total max exchange value
    """
    if coin%12 == 0:
        return coin/2 + coin/3 + coin/4 + \
            max_value(coin/2) + max_value(coin/3) + max_value(coin/4)

    else:
        return 0

if __name__ == '__main__':

    COIN = int(raw_input("Enter the Coin Value :"))
    print max_value(COIN)
    