from project.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            return

        result = room.take_room(people)
        if not result:
            self.guests += people

    def free_room(self, room_number: int) -> None:
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            return

        result = room.free_room()
        people = room.guests
        if not result:
            self.guests -= people

    def status(self) -> str:
        return f"Hotel {self.name} has {self.guests} total guests\n" \
                f"Free rooms: {', '.join([str(room.number) for room in self.rooms if not room.is_taken])}\n" \
                f"Taken rooms: {', '.join([str(room.number) for room in self.rooms if room.is_taken])}\n"
