class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
    {
        "id": self._generate_id(),
        "first_name": "Tommy",  # Cambiado aquí para que coincida con el test
        "last_name": last_name,
        "age": 5,
        "lucky_numbers": [1]
    },
    {
        "id": self._generate_id(),
        "first_name": "Jane",
        "last_name": last_name,
        "age": 35,
        "lucky_numbers": [10, 14, 3]
    },
    {
        "id": self._generate_id(),
        "first_name": "Jimmy",
        "last_name": last_name,
        "age": 33,
        "lucky_numbers": [7, 13, 22]
    }
]

    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        self._members.append(member)

        return member

    def delete_member(self, id):
        for m in self._members:
            if m["id"] == id:
                self._members.remove(m)
                return m  # importante para el test_delete_response
        return None

    def get_member(self, id):
        for m in self._members:
            if m["id"] == id:
                return m
        return None

    def get_all_members(self):
        return self._members
