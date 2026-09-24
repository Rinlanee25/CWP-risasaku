def checkmate(board):

    rows = board.split("\n")

    # หา King
    for r in range(len(rows)):
        for c in range(len(rows[r])):
            if rows[r][c] == "K":
                king_r = r
                king_c = c

    # ตรวจ Pawn
    for r in range(len(rows)):
        for c in range(len(rows[r])):
            if rows[r][c] == "P":

                # Pawn โจมตีเฉียงขึ้น 1 ช่อง
                if r - 1 == king_r and abs(c - king_c) == 1:
                    print("Success")
                    return

    # ตรวจ Bishop
    if check_bishop(rows, king_r, king_c):
        print("Success")
        return

    # ตรวจ Rook
    if check_rook(rows, king_r, king_c):
        print("Success")
        return

    # ตรวจ Queen
    if check_queen(rows, king_r, king_c):
        print("Success")
        return

    # ไม่มีตัวไหนโจมตี King
    print("Fail")


def check_bishop(board, kr, kc):

    # Bishop เดินทแยง 4 ทิศ
    directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for dr, dc in directions:

        r = kr + dr
        c = kc + dc

        while 0 <= r < len(board) and 0 <= c < len(board[r]):

            # เจอตัวหมาก
            if board[r][c] != ".":

                # ตัวแรกเป็น Bishop
                if board[r][c] == "B":
                    return True

                # ตัวอื่นขวางทาง
                break

            r += dr
            c += dc

    return False


def check_rook(board, kr, kc):

    # Rook เดินขึ้น ลง ซ้าย ขวา
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in directions:

        r = kr + dr
        c = kc + dc

        while 0 <= r < len(board) and 0 <= c < len(board[r]):

            if board[r][c] != ".":

                # ตัวแรกเป็น Rook
                if board[r][c] == "R":
                    return True

                # มีตัวอื่นขวาง
                break

            r += dr
            c += dc

    return False


def check_queen(board, kr, kc):

    # Queen เดินได้ทั้งแนวตรงและแนวทแยง
    directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in directions:

        r = kr + dr
        c = kc + dc

        while 0 <= r < len(board) and 0 <= c < len(board[r]):

            if board[r][c] != ".":

                # ตัวแรกเป็น Queen
                if board[r][c] == "Q":
                    return True

                # มีตัวอื่นขวาง
                break

            r += dr
            c += dc

    return False