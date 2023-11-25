from dataclasses import dataclass

@dataclass
class Item:
    name: str
    weight: int
    value: int
        
@dataclass
class Entry:
    value: int
    Items: list[Item]
    
Table = list[list[Entry]]

def solve(size: int, items: list[Item]) -> Table:
    table: Table = [[Entry(0,[]) for _ in range(size + 1)]
                    for _ in range(len(items))]
    for i in range(len(table)):
        for j in range(1,size + 1):
            compute_cell(items[i],table,i,j)
    return table

def compute_cell(item: Item, table: Table, i: int, j: int) -> None:
    if i == 0:
        if item.weight <= j:
            table[i][j] = Entry(item.value,[item])
    else:
        previous: Entry = table[i-1][j]
        table[i][j] = previous
        if item.weight <= j:
            remaining_space: Entry = table[i-1][j-item.weight]
            current: int = item.value + remaining_space.value
            if current > previous.value:
                table[i][j] = Entry(current,
                                    remaining_space.Items + [item])



if __name__ == '__main__':
    from pprint import pprint
    table: Table = solve(4,[Item('Guitar',1,1_500),
                            Item('Stereo',4,3_000),
                            Item('Laptop',3,2_000),
                            Item('Iphone',1,2_000),
                            Item('Jewelry',1,55000)])
    pprint(table)