from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from ..database import Base


class Month(Base):

    __tablename__ = "Month"
    __table_args__ = {"schema": "Report_Main"}

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    mah_zarsh = Column(
        "ماه گزارش",
        String(255)
    )

    shmarh_mah = Column(
        "شماره ماه",
        String(255)
    )

    dvrh = Column(
        "دوره",
        String(255)
    )

    sal = Column(
        "سال",
        String(255)
    )

    unic_code = Column(
        "unic_code",
        String(255)
    )

    shmarh_mah_2 = Column(
        "شماره ماه 2",
        String(255)
    )