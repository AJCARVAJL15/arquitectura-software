from dataclasses import dataclass
from datetime import datetime

@dataclass
class Member:
    id: int
    name: str
    membership_type: str
    check_in_time: datetime = None
