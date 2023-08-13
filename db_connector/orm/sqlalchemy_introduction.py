from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import Session, declarative_base, relationship

Base = declarative_base()


class UserAccount(Base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    fullname = Column(String(100), nullable=True)

    # Build 1:M with Adress
    adresses = relationship("Address", back_populates="user")


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email_adress = Column(String(50))
    user_id = Column(Integer, ForeignKey("user_account.id"))

    # Build 1:M with UserAccount
    user = relationship("UserAccount", back_populates="adresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


engine = create_engine("sqlite:///introduction.sqlite")
Base.metadata.create_all(bind=engine)

with Session(engine) as session:
    test_user = UserAccount(
        name="test_user",
        fullname="test_user full name",
        adresses=[
            Address(email_adress="test1@test.com"),
            Address(email_adress="test2@test2.com"),
        ],
    )
    test_user_two = UserAccount(
        name="test_user_two",
        fullname="test_user_two full name",
        adresses=[
            Address(email_adress="test3@test.com"),
            Address(email_adress="test4@test.com"),
        ],
    )
    session.add_all([test_user, test_user_two])
    session.commit()
