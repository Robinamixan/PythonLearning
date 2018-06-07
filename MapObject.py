from GameObject import *


class MapObject:
    title = ''
    x = 0
    y = 0
    cell_size = 0
    cells = []
    width_cells = 0
    height_cells = 0
    screen = None
    color = (0, 0, 0)

    def __init__(self, title, screen, position, cell_size, width_cells, height_cells):
        self.title = title
        self.screen = screen
        self.x = position[0]
        self.y = position[1]
        self.cell_size = cell_size
        self.width_cells = width_cells
        self.height_cells = height_cells
        self.cells = [0] * width_cells
        for i in range(0, width_cells):
            self.cells[i] = [None] * height_cells
            for j in range(0, height_cells):
                self.cells[i][j] = CellObject(self.x + self.cell_size * i, self.x + self.cell_size * j)

    def draw_field(self, tool):
        self.screen.fill(white)

        end_x = self.x + self.cell_size * self.width_cells
        end_y = self.y + self.cell_size * self.height_cells

        for x, row in enumerate(self.cells):
            for y, cell in enumerate(row):
                rectangle = [
                    cell.x,
                    cell.y,
                    cell.size + 1,
                    cell.size + 1
                ]
                tool.rect(self.screen, black, rectangle, 1)

        tool.line(self.screen, red, (self.x, self.y), (self.x, end_y), 2)
        tool.line(self.screen, red, (self.x, self.y), (end_x, self.y), 2)
        tool.line(self.screen, red, (end_x, self.y), (end_x, end_y), 2)
        tool.line(self.screen, red, (end_x, end_y), (self.x, end_y), 2)

    def update_cells(self):
        for x, row in enumerate(self.cells):
            for y, cell in enumerate(row):
                if not cell.is_empty():
                    map_object = cell.get_object()
                    map_object.update()

    def draw_cells(self):
        for x, row in enumerate(self.cells):
            for y, cell in enumerate(row):
                if not cell.is_empty():
                    map_object = cell.get_object()
                    map_object.draw(self.cell_size)

    def create_wall(self, point):
        StaticObject('second', self.screen, self, point, (1, 1), brow)

    def get_cell(self, x, y):
        return self.cells[x][y]

    def get_cell_by_coord(self, x, y):
        pos = [int((x - self.x) / self.cell_size), int((y - self.y) / self.cell_size)]

        if pos[0] >= self.width_cells:
            pos[0] = self.width_cells - 1

        if pos[1] >= self.height_cells:
            pos[1] = self.height_cells - 1

        if pos[0] < 0:
            pos[0] = 0

        if pos[1] < 0:
            pos[1] = 0

        return pos


class CellObject:
    empty = True
    contain = None
    x = 0
    y = 0
    size = map_cell_size

    def __init__(self, x, y):
        self.empty = True
        self.x = x
        self.y = y

    def is_empty(self):
        return self.empty

    def get_object(self):
        return self.contain

    def set_object(self, map_object):
        self.contain = map_object
        self.empty = False

    def clear(self):
        self.contain = None
        self.empty = True