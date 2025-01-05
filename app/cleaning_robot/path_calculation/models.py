from sqlalchemy import Integer, Column, TIMESTAMP, FLOAT
from app.cleaning_robot.database import Base


class PathCalculationExecution(Base):
    __tablename__ = "executions"

    id = Column(Integer, primary_key=True)
    timestamp = Column(TIMESTAMP, nullable=False)
    commands = Column(Integer, nullable=False, default=0)
    result = Column(Integer, nullable=False, default=0)
    duration = Column(FLOAT, nullable=False, default=0.0)

    def __repr__(self) -> str:
        return (
            f"PathCalculationExecution(id={self.id!r}, timestamp={self.timestamp!r}, "
            f"commands={self.commands!r}, result={self.result!r}),"
            f"duration={self.duration!r})"
        )

    def as_dict(self) -> dict:
        return {
            "id": self.id,
            "timestamp": self.timestamp.isoformat(),
            "commands": self.commands,
            "result": self.result,
            "duration": "{:.6f}".format(self.duration),
        }
