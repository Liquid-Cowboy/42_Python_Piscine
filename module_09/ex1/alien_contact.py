from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional, Any, Self


class ContactType(Enum):
    RADIO: str = 'radio'
    VISUAL: str = 'visual'
    PHYSICAL: str = 'physical'
    TELEPATHIC: str = 'telephatic'


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(ge=0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check(self) -> Self:
        if self.contact_id[:2] != 'AC':
            raise ValueError('Contact ID must start with "AC" (Alien Contact)')
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError('Physical contact reports must be verified')
        if (
         self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3
         ):
            raise ValueError('Telepathic contact requires at '
                             'least 3 witnesses')
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError('Strong signals (> 7.0) should '
                             'include received messages')
        return self


def print_data(contact: AlienContact) -> None:
    print(
        'Valid contact report:\n'
        f'ID: {contact.contact_id}\n',
        f'Type: {contact.contact_type.value}\n',
        f'Location: {contact.location}\n',
        f'Signal: {contact.signal_strength:.1f}/10\n',
        f'Duration: {contact.duration_minutes} minutes\n',
        f'Witnesses: {contact.witness_count}\n',
        f'Message: \'{contact.message_received}\''
    )


def main() -> None:
    try:
        print('Alien Contact Log Validation\n'
              '======================================')
        contact_info: dict[str, Any] = {
            'contact_id': 'AC_2024_001',
            'timestamp': '2025-02-12',
            'location': 'Area 51, Nevada',
            'contact_type': ContactType.RADIO,
            'signal_strength': 8.5,
            'duration_minutes': 45,
            'witness_count': 5,
            'message_received': 'Greetings from Zeta Reticuli',
            'is_verified': True,
        }
        contact: AlienContact = AlienContact(**contact_info)
        print_data(contact)
        print(
            '\n======================================\n'
            'Expected validation error:')
        contact_info['contact_type'] = ContactType.TELEPATHIC
        contact_info['witness_count'] = 2
        contact = AlienContact(**contact_info)
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'][13:])


if __name__ == '__main__':
    main()
