from flet import Colors

from utils import COLOR_HEX_MAP


class Tag:
    def __init__(self, id: int, name: str, color: Colors) -> None:
        self.id = id
        self.name = name
        self.color = color
        self.text_color = self._get_text_color()

    def _get_text_color(self) -> Colors:
        hex_color = COLOR_HEX_MAP[self.color.lower()].lstrip("#")

        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        luminance = 0.299 * r + 0.587 * g + 0.114 * b

        return Colors.WHITE if luminance < 128 else Colors.BLACK

    def __eq__(self, other) -> bool:
        if not isinstance(other, Tag):
            return False
        return self.name == other.name and self.color == other.color

    def to_dict(self) -> dict[str, str]:
        return {"name": self.name, "color": self.color}

    @classmethod
    def from_dict(cls, id: int, data: dict) -> "Tag":
        return cls(id=id, name=data["name"], color=data["color"])
