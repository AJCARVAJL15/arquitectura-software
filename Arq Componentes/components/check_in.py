from pydispatch import dispatcher
from services.member_service import MemberService

class CheckInComponent:
    def __init__(self, member_service: MemberService):
        self.member_service = member_service

    def check_in(self, member_id: int):
        if self.member_service.check_in_member(member_id):
            dispatcher.send(signal='member_checked_in', sender=self, member_id=member_id)
            print(f'Miembro con el Id: {member_id} registrado satisfactoriamente.')
        else:
            print("----------------------------------")
            print(f'Fallo en registrar el miembro {member_id}.')
