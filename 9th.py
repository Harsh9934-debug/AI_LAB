def puramid(n):
    for i in range(n):
        print(*list(range(i+1,n+1))
              +list(range(1,i+1))
              )
puramid(5)