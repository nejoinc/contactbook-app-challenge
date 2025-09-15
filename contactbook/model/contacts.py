from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class Contact:
    name: str = field
    phone: str = field
    email: str = field
    tags: List[str] = field(default_factory=list)
    creation_date: datetime = field(default_factory=datetime.now)

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)



    def __str__(self) -> str:
        tags = ", ".join(self.tags)
        return f'Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nTags: {tags}\nCreated on: {self.creation_date}'



