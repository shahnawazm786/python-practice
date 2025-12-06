heights = [144, 167, 189, 170, 190, 150, 165, 178, 200, 130]
#h < 150 - S
#h >= 150 and h < 180 - M
#h >= 180 - L
def T_shirt_shize(n):
    if n>=180:
        return 'L'
    elif n>=150 and n<180:
        return 'M'
    else:
        return 'S'
    
size_list=list(map(T_shirt_shize,heights))
print(size_list)

