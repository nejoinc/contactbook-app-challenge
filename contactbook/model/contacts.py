from dataclasses import dataclass, field


@dataclass
class ContactBook:
    contacts: dict[str, Contact] = field(default_factory=dict)

    def add_contact(self, name: str, phone: str, email: str, tags: list[str]):
        new_object = Contact(name, phone, email, tags)
        self.contacts[new_object.phone] = new_object

    def delete_contact(self, phone: str):
        del self.contacts[phone]
