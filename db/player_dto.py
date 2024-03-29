from enum import unique
from sqlalchemy import Column, Integer, String, UniqueConstraint, create_engine
from sqlalchemy.orm import relationship

from base import Base


class Player(Base):
    __tablename__ = "Players"

    id = Column(Integer, primary_key=True)
    espn_player_name = Column(String, nullable=False)
    position = Column(String)
    espn_id = Column(Integer, unique=True, nullable=False)

    draftpicks = relationship("Draftpick", back_populates="player")
    stats = relationship("Stat", back_populates="player")

    def __repr__(self):
        return (
            f"Player(id={self.id!r}"
            f", espn_player_name={self.espn_player_name!r}"
            f", position={self.position!r}"
            f", espn_id={self.espn_id!r})"
        )


if __name__ == "__main__":
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
    Base.metadata.create_all(engine)
