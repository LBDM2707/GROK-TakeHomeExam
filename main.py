import argparse


class World:
    class Box:
        def __init__(self, is_filled: bool = False) -> None:
            self.is_filled = is_filled

        def __str__(self) -> str:
            return f'[{"x" if self.is_filled else " "}]'

        def evolve_val(self, left_box_val: bool, right_box_val: bool):
            if (
                (self.is_filled == left_box_val and self.is_filled == right_box_val)
                or (left_box_val and self.is_filled)
                or (not self.is_filled and left_box_val and right_box_val)
            ):
                return False
            return True

    def __init__(self, size: int = 21) -> None:
        boxes = []
        for i in range(0, size):
            if i == int(size / 2):
                boxes.append(self.Box(True))
            else:
                boxes.append(self.Box(False))
        self.boxes = boxes
        self.gen = 0
        self.size = size

    def get_generation(self) -> int:
        return self.gen

    def evolve(self) -> None:
        new_boxes = []
        for i in range(self.size):
            left = False if i == 0 else self.boxes[i - 1].is_filled
            right = False if i == self.size - 1 else self.boxes[i + 1].is_filled
            new_boxes.append(self.Box(self.boxes[i].evolve_val(left, right)))
        self.boxes = new_boxes
        self.gen += 1

    def __str__(self) -> str:
        result = ""
        for box in self.boxes:
            result += str(box)
        return result


def main(args):
    if args.size:
        the_world = World(args.size)
    else:
        the_world = World()
    print(f"Start:\t{the_world}")
    for i in range(args.gen if args.gen else 10):
        the_world.evolve()
        print(f"Gen {the_world.gen}:\t{the_world}")

    pass


if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-s", "--size", type=int, help="World size")
    argParser.add_argument("-g", "--gen", type=int, help="Number of generation")
    args = argParser.parse_args()
    main(args)
