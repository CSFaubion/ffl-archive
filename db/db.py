import json

import sqlalchemy
from sqlalchemy.orm import registry

from base import Base
from draftpick_dto import Draftpick
from owner_dto import Owner
from player_dto import Player
from roster_dto import Roster
from season_dto import Season
from setting_dto import Setting
from stat_dto import Stat
from team_dto import Team

engine = sqlalchemy.create_engine(
    "sqlite+pysqlite:///:memory:", echo=True, future=True)

# mapper_registry = registry()
# Base = mapper_registry.generate_base()


if __name__ == "__main__":
    Base.metadata.create_all(engine)
