
#* Let's learn about list comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n.
#TODO Here, 
#TODO: 0 <= i <= x;
#TODO: 0 <= j <= y;
#TODO: 0 <= k <= z;

# . Please use list comprehensions rather than multiple loops, as a learning exercise.

#* Example
#* x = 1
#* y = 1
#* z = 1
#* n = 2
#* Output
#* [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

def x(i,j,k,n):
    if(n != i+j+k):
        return
    
def compare(x,y,z,n):
    out = []
    arr = [[[out.append([i,j,k]) for k in range(z+1)]for j in range(y+1)]for i in range(x+1)]
    for a in out:
        if(sum(a) == n):
            out.remove(a)
    for a in out:
        if(sum(a) == n):
            out.remove(a)
    print(out)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    compare(x,y,z,n)
