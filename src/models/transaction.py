from datetime import datetime
from typing import List, Optional

from .tag import Tag


class Transaction:
    def __init__(
        self,
        id: int,
        date: datetime,
        amount: float,
        transaction_type: str,
        tags: Optional[List[Tag]] = [],
    ) -> None:
        self.id = id
        self.date = date
        self.amount = amount
        self.transaction_type = transaction_type
        self.tags = tags if tags else []

    def add_tag(self, tag: Tag) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

    def to_dict(self) -> dict:
        return {
            "date": self.date.isoformat(),
            "amount": self.amount,
            "transaction_type": self.transaction_type,
            "tags": [tag.to_dict() for tag in self.tags],
        }

    @classmethod
    def from_dict(cls, id: int, data: dict) -> "Transaction":
        return cls(
            id=id,
            date=datetime.fromisoformat(data["date"]),
            amount=data["amount"],
            transaction_type=data["transaction_type"],
            tags=[
                Tag.from_dict(tag_id, tag_data)
                for tag_id, tag_data in enumerate(data.get("tags", []))
            ],
        )
