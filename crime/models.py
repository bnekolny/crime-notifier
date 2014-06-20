from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class PoliceDepartmentRegistry(Base):
    """
    This is the table that holds the registered police department
    data sources, their name, location, and url
    """
    __tablename__ = 'policedepartment_registry'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    city = Column(String(10))
    state = Column(String(2))
    data_source_url = Column(String(20))


class Crimes(Base):
    """
    Crimes table, this is the imported data from various PD Registry objects
    """
    __tablename__ = 'crimes'
    id = Column(Integer, primary_key=True)
    pd_id = Column(Integer, ForeignKey("policedepartment_registry.id"))

    pd_incident = Column(Integer)
    pd_offense = Column(Integer)
    offense_code_id = Column(Integer)
    offense_code_ext_id = Column(Integer)
    offense_type = Column(String(20))
    offense_category = Column(String(20))
    first_occurrence = Column(DateTime)
    last_occurrence = Column(DateTime, nullable=True)
    reported_date = Column(DateTime)
    address = Column(String(20))
    geo_x = Column(Float)
    geo_y = Column(Float)
    longitude = Column(Float)
    latitude = Column(Float)
    pd_district = Column(Integer)
    pd_precinct = Column(Integer)
    neighborhood = Column(String(20))
