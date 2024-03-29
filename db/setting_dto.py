from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
    create_engine,
)
from sqlalchemy.orm import relationship

from base import Base


class Setting(Base):
    __tablename__ = "Settings"

    id = Column(Integer, primary_key=True)
    season_id = Column(Integer, ForeignKey("Seasons.id"), unique=True, nullable=False)

    reg_season_count = Column(Integer, nullable=False)
    veto_votes_required = Column(Integer)
    team_count = Column(Integer, nullable=False)
    playoff_team_count = Column(Integer, nullable=False)
    keeper_count = Column(Integer)
    tie_rule = Column(String, nullable=False)
    playoff_seed_tie_rule = Column(String, nullable=False)

    season = relationship("Season", back_populates="setting")

    def __repr__(self):
        return (
            f"Setting(id={self.id!r}, season_id={self.season_id!r}"
            f", reg_season_count={self.reg_season_count!r}"
            f", veto_votes_required={self.veto_votes_required!r}"
            f", team_count={self.team_count!r}"
            f", playoff_team_count={self.playoff_team_count!r}"
            f", keeper_count={self.keeper_count!r}"
            f", tie_rule={self.tie_rule!r}"
            f", playoff_seed_tie_rule={self.playoff_seed_tie_rule!r})"
        )


if __name__ == "__main__":
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
    Base.metadata.create_all(engine)
