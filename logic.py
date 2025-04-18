def bestMove(cells: list) -> int:
    for i, cell in enumerate(cells, start=1):
        if cell.taken == "p":
            if i == 1 or i == 4 or i == 7:
                if cells[i + 1].taken == "f":
                    return cells[i + 1].num
                if i != 7 and cells[i + 3].taken == "f":
                    return cells[i + 3].num
                if i == 7 and cells[i - 3].taken == "f":
                    return cells[i - 3].num
            elif i == 2 or i == 5 or i == 8:
                if cells[i + 1].taken == "f":
                    return cells[i + 1].num
                if cells[i - 1].taken == "f":
                    return cells[i - 1].num
            elif i == 3 or i == 6 or i == 9:
                if i != 9 and cells[i + 3].taken == "f":
                    return cells[i + 3].num
                if i == 9 and cells[i - 3].taken == "f":
                    return cells[i - 3].num
                if cells[i - 1].taken == "f":
                    return cells[i - 1].num
            else:
                pass
        else:
            for cell in cells:
                if cell.taken == "f":
                    return cell.num
    return 0
