while True:
    try:
        r1, x1, y1, r2, x2, y2 = map(int, input().split())

        if r1 < r2:
            print("MORTO")
            continue

        dx = x1 - x2
        dy = y1 - y2

        distancia2 = dx*dx + dy*dy
        diff = r1 - r2

        if distancia2 <= diff*diff:
            print("RICO")
        else:
            print("MORTO")

    except EOFError:
        break
