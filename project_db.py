from sqlalchemy import String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import create_engine

PGUSER = "Ваші значення"
PGPASSWORD = "Ваші значення"

engine = create_engine(f"sqlite:///database.db", echo=True)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    def create_db(self):
        Base.metadata.create_all(engine)

    def drop_db(self):
        Base.metadata.drop_all(engine)

class Conversion(Base):
    __tablename__ = 'conversions'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    from_currency: Mapped[str] = mapped_column(String(3))
    to_currency: Mapped[str] = mapped_column(String(3))

    # Сума, яку користувач хоче конвертувати
    amount: Mapped[float] = mapped_column(Float)

    result: Mapped[float] = mapped_column(Float)

base = Base()
base.create_db()


from sqlalchemy import String, Float, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

engine = create_engine("sqlite:///database.db")

Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Conversion(Base):
    __tablename__ = "conversions"

    id: Mapped[int] = mapped_column(primary_key=True)
    from_currency: Mapped[str] = mapped_column(String(3))
    to_currency: Mapped[str] = mapped_column(String(3))
    amount: Mapped[float] = mapped_column(Float)
    result: Mapped[float] = mapped_column(Float)


Base.metadata.create_all(engine)