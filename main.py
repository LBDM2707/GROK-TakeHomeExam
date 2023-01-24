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
        for i in range(0, size + 2):
            if i == (size - 1) / 2 + 1:
                boxes.append(self.Box(True))
            else:
                boxes.append(self.Box(False))
        self.boxes = boxes
        self.gen = 0
        self.size = size

    def get_generation(self) -> int:
        return self.gen

    def evolve(self) -> None:
        new_boxes = [self.boxes[0]]
        for i in range(1, self.size + 1):
            new_boxes.append(
                self.Box(
                    self.boxes[i].evolve_val(
                        self.boxes[i - 1].is_filled, self.boxes[i + 1].is_filled
                    )
                )
            )
        new_boxes.append(self.boxes[self.size + 1])
        self.boxes = new_boxes
        self.gen += 1
        pass

    def __str__(self) -> str:
        result = ""
        for box in self.boxes[1:-1]:
            result += str(box)
        return result


def main():
    the_world = World(21)
    print(f"Start:\t{the_world}")
    for i in range(10):
        the_world.evolve()
        print(f"Gen {the_world.get_generation()}:\t{the_world}")

    pass


if __name__ == "__main__":
    main()
