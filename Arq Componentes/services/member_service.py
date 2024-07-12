from typing import List, Optional
from models.member import Member
from datetime import datetime

class MemberService:
    def __init__(self):
        self.members = [
            Member(id=1, name='Carlos Lopez', membership_type='Mensual'),
            Member(id=2, name='Juan Asprilla', membership_type='Anual'),
            Member(id=3, name='Carolina Velez', membership_type='Anual'),
        ]

    def get_members(self) -> List[Member]:
        return self.members

    def get_member(self, id: int) -> Optional[Member]:
        return next((member for member in self.members if member.id == id), None)

    def check_in_member(self, id: int) -> bool:
        member = self.get_member(id)
        if member:
            member.check_in_time = datetime.now()
            return True
        return False
