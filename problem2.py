'''
Created on 11-Aug-2016

@author: pratiksoni
'''

MAIN_ROAD = []
SIDE_ROAD = []


def check_sequence_status(values):
    """
    Parameters : list of truck sequence that are coming
    return : True - if Turcks are in sequence in garage
             False - if Turcks are not in sequence in garage
    """
    for value in values:
        #print MAIN_ROAD, SIDE_ROAD
        if value == 1:
            MAIN_ROAD.append(value)

        if SIDE_ROAD and MAIN_ROAD:
            i = True
            while i:

                if SIDE_ROAD:

                    if (SIDE_ROAD[-1]-1) == MAIN_ROAD[-1]:
                        MAIN_ROAD.append(SIDE_ROAD[-1])
                        SIDE_ROAD.remove(SIDE_ROAD[-1])

                    else:
                        break

                else:
                    i = False

        if MAIN_ROAD  and MAIN_ROAD[-1] == value-1:
            MAIN_ROAD.append(value)

        else:
            SIDE_ROAD.append(value)

    if len(VALUES) == len(MAIN_ROAD):
        return True
    else:
        return False

if __name__ == '__main__':
    VALUES = raw_input("Enter the String :")
    VALUES = map(int, list(VALUES))
    VALUES.reverse()
    print check_sequence_status(VALUES)
    print MAIN_ROAD, SIDE_ROAD
