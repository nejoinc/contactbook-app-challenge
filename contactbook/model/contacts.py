from dataclasses import dataclass, field


@dataclass
class ContactBook:
    contacts: dict[str, Contact] = field(default_factory=dict)

    def add_contact(self, name: str, phone: str, email: str, tags: list[str]):
        new_object = Contact(name, phone, email, tags)
        self.contacts[new_object.phone] = new_object

    def delete_contact(self, phone: str):
        del self.contacts[phone]

    def list_contacts(self) -> list[Contact]:
        contacts_list = []
        for contact in self.contacts.values():
            contacts_list.append(contact)

        return contacts_list

    def contacts_by_tag(self, tag: str) -> list[Contact]:
        contacts_with_tag = []
        for contact in self.contacts.values():
            if self.contacts[tag] in contact.tags:
                contacts_with_tag.append(contact)
        return contacts_with_tag

    def search_by_criteria(self, name: str, phone: str, email: str) -> list[Contact]:
        result = []

        for contact in self.contacts.values():
            match = True

            if name:
                if name.lower() not in contact.name.lower():
                    match = False

            if phone:
                if phone.lower() not in contact.phone.lower():
                    match = False

            if email:
                if email.lower() not in contact.email.lower():
                    match = False

            if match:
                result.append(contact)

        return result

