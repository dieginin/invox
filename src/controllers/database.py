from datetime import datetime
from typing import List, Optional

from tinydb import Query, TinyDB
from tinydb.table import Table

from models import Tag, Transaction


class _Database:
    def __init__(self) -> None:
        self.db = TinyDB("db.json")

    @staticmethod
    def get_next_id(table: Table) -> int:
        if not table.all():
            return 1
        return len(table.all()) + 1

    @staticmethod
    def check_existence(table: Table, **kwargs) -> Optional[str]:
        for key, value in kwargs.items():
            if table.search(Query()[key] == value):
                return (
                    f"{table.name[:-1].capitalize()} with {key} {value} already exists."
                )


class Tags:
    def __init__(self) -> None:
        self.__table = _Database().db.table("tags")

    @property
    def list(self) -> list[Tag]:
        return sorted(
            [Tag.from_dict(tag.doc_id, tag) for tag in self.__table.all()],
            key=lambda tag: tag.name,
        )

    def get(self, id: int) -> Optional[Tag]:
        tag = self.__table.get(Query().id == id)
        if not tag or not isinstance(tag, dict):
            return None
        return Tag.from_dict(tag.doc_id, tag)

    def add(self, name: str, color: str) -> str:
        if existing_tag := _Database.check_existence(
            self.__table, name=name, color=color
        ):
            return existing_tag

        self.__table.insert({"name": name, "color": color})
        return f"Tag {name} added."

    def edit(self, tag: Tag) -> str:
        if existing_tag := _Database.check_existence(self.__table, **tag.to_dict()):
            return existing_tag

        self.__table.update(tag.to_dict(), Query().id == tag.id)
        return f"Tag {tag.name} updated."

    def remove(self, tag: Tag) -> str:
        if self.__table.remove(Query().id == tag.id):
            return f"Tag {tag.name} removed."
        else:
            return f"Tag not found."


class Transactions:
    def __init__(self) -> None:
        self.__table = _Database().db.table("transactions")

    @property
    def list(self) -> list[Transaction]:
        return sorted(
            [Transaction.from_dict(txn.doc_id, txn) for txn in self.__table.all()],
            key=lambda txn: txn.date,
        )

    def get(self, id: int) -> Optional[Transaction]:
        txn = self.__table.get(Query().id == id)
        if not txn or not isinstance(txn, dict):
            return None
        return Transaction.from_dict(txn.doc_id, txn)

    def get_by_date_range(
        self, start_date: datetime, end_date: datetime
    ) -> List[Transaction]:
        return sorted(
            [
                Transaction.from_dict(txn.doc_id, txn)
                for txn in self.__table.search(
                    (Query().date >= start_date.isoformat())
                    & (Query().date <= end_date.isoformat())
                )
            ],
            key=lambda txn: txn.date,
        )

    def add(
        self, date: datetime, amount: float, transaction_type: str, tags: List[Tag]
    ) -> str:
        self.__table.insert(
            {
                "date": date.isoformat(),
                "amount": amount,
                "transaction_type": transaction_type,
                "tags": [tag.to_dict() for tag in tags],
            }
        )
        return f"Transaction on {date.strftime("%B, %d %Y")} added."

    def edit(self, transaction: Transaction) -> str:
        self.__table.update(transaction.to_dict(), Query().id == transaction.id)
        return f"Transaction {transaction.id} updated."

    def remove(self, transaction: Transaction) -> str:
        if self.__table.remove(Query().id == transaction.id):
            return f"Transaction {transaction.id} removed."
        else:
            return f"Transaction not found."
