from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine


Base = declarative_base()
DBSession = sessionmaker()


class StickyRole(Base):
    __tablename__ = "StickyRoles"
    id = Column(Integer, primary_key=True)
    guild_id = Column(Integer, nullable=False)
    role_id = Column(Integer, nullable=False)


class AppliedRole(Base):
    __tablename__ = "AppliedRoles"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    role_id = Column(Integer, ForeignKey(StickyRole.id), nullable=False)
    role = relationship("StickyRole", foreign_keys=[role_id])


class Store(object):
    def __init__(self, directory: str):
        self.engine = create_engine("sqlite:///{0}StickyRoles.db".format(directory))
        Base.metadata.create_all(self.engine)
        DBSession.configure(bind=self.engine)

    def get_roles(self, guild_id: int):
        session = DBSession()
        roles = session.query(
            StickyRole
        ).filter(
            StickyRole.guild_id == guild_id
        ).all()

        return roles

    def get_user_roles(self, guild_id: int, user_id: int):
        session = DBSession()
        roles = session.query(
            AppliedRole
        ).join(
            StickyRole, AppliedRole.role_id == StickyRole.role_id
        ).filter(
            AppliedRole.user_id == user_id
        ).filter(
            StickyRole.guild_id == guild_id
        ).all()

        return roles

    def add_user_role(self, guild_id: int, user_id: int, role_id: int):
        try:
            session = DBSession()
            saved_roles = session.query(
                StickyRole
            ).filter(
                StickyRole.guild_id == guild_id
            ).filter(
                StickyRole.role_id == role_id
            ).all()

            if(len(saved_roles) > 0):
                role = AppliedRole()
                role.role_id = role_id
                role.user_id = user_id
                session.add(role)
                session.commit()

            return True
        except Exception as ex:
            print(ex)
            return False

    def delete_user_role(self, user_id: int, role_id: int):
        try:
            session = DBSession()
            saved_roles = session.query(
                AppliedRole
            ).filter(
                AppliedRole.role_id == role_id
            ).filter(
                AppliedRole.user_id == user_id
            ).all()

            if(len(saved_roles) != 0):
                for role in saved_roles:
                    session.delete(role)
                session.commit()

            return True
        except Exception as ex:
            print(ex)
            return False

    def add_role(self, guild_id: int, role_id: int) -> bool:
        try:
            session = DBSession()
            saved_roles = session.query(
                StickyRole
            ).filter(
                StickyRole.guild_id == guild_id
            ).filter(
                StickyRole.role_id == role_id
            ).all()

            if(len(saved_roles) == 0):
                role = StickyRole()
                role.role_id = role_id
                role.guild_id = guild_id
                session.add(role)
                session.commit()

            return True
        except Exception as ex:
            print(ex)
            return False

    def delete_role(self, guild_id: int, role_id: int) -> bool:
        try:
            session = DBSession()
            saved_roles = session.query(
                StickyRole
            ).filter(
                StickyRole.guild_id == guild_id
            ).filter(
                StickyRole.role_id == role_id
            ).all()

            if(len(saved_roles) != 0):
                for role in saved_roles:
                    session.delete(role)
                session.commit()

            return True
        except Exception as ex:
            print(ex)
            return False
