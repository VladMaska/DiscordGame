import game as g

def Up():
    if g.y != 0:
        g.area[ g.y ][ g.x ]  = "0"
        g.y -= 1
        g.area[ g.y ][ g.x ]  = "1"

def Left():
    if g.x != 0:
        g.area[ g.y ][ g.x ]  = "0"
        g.x -= 1
        g.area[ g.y ][ g.x ]  = "1"

def Down():
    if g.y != len( g.area ):
        g.area[ g.y ][ g.x ]  = "0"
        g.y += 1
        g.area[ g.y ][ g.x ]  = "1"

def Right():
    if g.x != len( g.area[ 0 ] ) - 1:
        g.area[ g.y ][ g.x ]  = "0"
        g.x += 1
        g.area[ g.y ][ g.x ]  = "1"