from services.member_service import MemberService
from components.check_in import CheckInComponent
from components.member_detail import MemberDetailComponent

def main():
    member_service = MemberService()
    check_in_component = CheckInComponent(member_service)
    member_detail_component = MemberDetailComponent(member_service)

    # Simulate checking in members
    check_in_component.check_in(1)
    check_in_component.check_in(2)
    check_in_component.check_in(3)
    check_in_component.check_in(4) 

if __name__ == '__main__':
    main()
