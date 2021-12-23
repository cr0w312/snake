print('\n'.join(' '.join(*zip(*row)) for row in ([["*" if row==0 and col%3!=0 or row==1 and col%3==0 or row-col==2 or row+col==8 else " " for col in range(7)] for row in range(6)])))
print(*[('* ' * i + '*').rjust(7 * 2 + i) for i in range(5)], *[('* ' * i + '*').rjust(7 * 2 + i) for i in range(1, 7)], *[('* ' * i + '*').rjust(7 * 2 + i) for i in range(1, 9)], sep='\n')
