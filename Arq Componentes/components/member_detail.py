from pydispatch import dispatcher
from services.member_service import MemberService

class MemberDetailComponent:
    def __init__(self, member_service: MemberService):
        self.member_service = member_service
        dispatcher.connect(self.display_member_detail, signal='member_checked_in', sender=dispatcher.Any)

    def display_member_detail(self, member_id: int):
        member = self.member_service.get_member(member_id)
        if member:
            print("----------------------------------")
            print(f'Nombre: {member.name}')
            print(f'Tipo de membresia: {member.membership_type}')
            print(f'Hora de registro: {member.check_in_time}')
       
        else:
            print('El miembro no existe')
