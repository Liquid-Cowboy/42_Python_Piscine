from pydantic import BaseModel, Field, ValidationError
from typing import Optional, Any
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)
    # Field is a validating function from the pydantic module
    # It has default parameters that constrain the user's input
    # It will validate said input according to the type hint specified


def print_data(station: SpaceStation) -> None:
    status: str = 'Operational' if station.is_operational else 'Out of order'
    print(
        'Valid station created:\n'
        f'ID: {station.station_id}\n',
        f'Name: {station.name}\n',
        f'Crew: {station.crew_size} people\n',
        f'Power: {station.power_level:.1f}%\n',
        f'Oxygen: {station.oxygen_level:.1f}%\n',
        f'Status: {status}'
    )


def main() -> None:
    station_info: dict[str, Any] = {
        'station_id': 'ISS001',
        'name': 'International Space Station',
        'crew_size': 6,
        'power_level': 85.5,
        'oxygen_level': 92.3,
        'last_maintenance': '2025-02-12',
        'is_operational': True,
        'notes': None,
    }
    try:
        print('Space Station Data Validation\n'
              '======================================')

        station: SpaceStation = SpaceStation(**station_info)  # dict unpacking
        print_data(station)
        station_info['crew_size'] = 21
        print(
            '\n======================================\n'
            'Expected validation error:')
        station = SpaceStation(**station_info)
        print_data(station)
    except ValidationError as e:
        for error in e.errors():  # accessing exception object attr
            print(error['msg'])  # accessing key in attr


if __name__ == '__main__':
    main()
