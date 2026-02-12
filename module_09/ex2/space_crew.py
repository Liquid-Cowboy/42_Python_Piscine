from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Self


class Rank(Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(ge=0, le=50)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(ge=1, le=10000)

    @model_validator(mode='after')
    def check(self) -> Self:
        in_charge: bool = False
        experienced: int = 0
        crew_count: int = 0

        if self.mission_id[0] != 'M':
            raise ValueError('Mission ID must start with "M"')
        for member in self.crew:
            crew_count += 1
            if member.rank == Rank.COMMANDER or member.rank == Rank.CAPTAIN:
                in_charge = True
            if member.years_experience > 5:
                experienced += 1
            if not member.is_active:
                raise ValueError('All crew members must be active')
        if not in_charge:
            raise ValueError('Mission must have at least one '
                             'Commander or Captain')
        if self.duration_days > 365 and experienced < (crew_count / 2):
            raise ValueError('Long missions (> 365 days) need 50% '
                             'experienced crew (5+ years)')
        return self


def print_data(mission: SpaceMission) -> None:
    i: int = 0
    for member in mission.crew:
        i += 1
    print(
        'Valid mission created:\n'
        f'Mission: {mission.mission_name}\n'
        f'ID: {mission.mission_id}\n'
        f'Destination: {mission.destination}\n'
        f'Duration: {mission.duration_days} days\n'
        f'Budget: ${mission.budget_millions:.1f}M\n'
        f'Crew size: {i}'
    )
    for member in mission.crew:
        print(
            f'- {member.name} ({member.rank.value}) - {member.specialization}'
        )


def main() -> None:
    try:
        print('Space Mission Crew Validation\n'
              '=========================================')
        crew: list[CrewMember] = [
            CrewMember(
                member_id='00001',
                name='Sarah Connor',
                rank=Rank.COMMANDER,
                age=35,
                specialization='Mission Command',
                years_experience=6,
            ),
            CrewMember(
                member_id='00002',
                name='John Smith',
                rank=Rank.LIEUTENANT,
                age=37,
                specialization='Navigation',
                years_experience=20,
            ),
            CrewMember(
                member_id='00003',
                name='Alice Johnson',
                rank=Rank.OFFICER,
                age=35,
                specialization='Engineering',
                years_experience=2,
            )
        ]

        mission: SpaceMission = SpaceMission(
            mission_id='M2024_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            launch_date='2026-02-12',
            duration_days=900,
            crew=crew,
            budget_millions=2500,
        )
        print_data(mission)
        print('\n=========================================\n'
              'Expected validation error:')
        crew = [crew[2]]
        mission: SpaceMission = SpaceMission(
            mission_id='M2024_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            launch_date='2026-02-12',
            duration_days=900,
            crew=crew,
            budget_millions=2500,
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'][13:])


if __name__ == '__main__':
    main()
