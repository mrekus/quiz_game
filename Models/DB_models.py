from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///quiz_game_db.db")
Base = declarative_base()


class Questions(Base):
    """
    Sukuria klausimų lentelę kurioje laikomi klausimai,
    galimi atsakymai, bei relationship į teisingus atsakymus.
    """
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    question = Column("question", String)
    choices = Column("choices", String)
    answers = relationship("Answers", back_populates="questions", uselist=False)

    # noinspection PyMissingConstructor
    def __init__(self, question, choices):
        self.question = question
        self.choices = choices

    def __repr__(self):
        return f"{self.id}) {self.question} - {self.choices}"


class Answers(Base):
    """
    Sukuria atskymų lentelę kurioje laikomi teisingi atsakymai į klausimus.
    """
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True)
    questions_id = Column("questions_id", Integer, ForeignKey("questions.id"))
    correct_answer = Column("correct_answer", String)
    questions = relationship("Questions", back_populates="answers", uselist=False)

    # noinspection PyMissingConstructor
    def __init__(self, questions_id, correct_answer):
        self.questions_id = questions_id
        self.correct_answer = correct_answer

    def __repr__(self):
        return f"{self.id}) {self.questions_id} - {self.correct_answer}"


class QuestionHistory(Base):
    """
    Sukuria lentelę kurioje laikoma žaidėjo klausimųu istorija.
    """
    __tablename__ = "question_history"
    id = Column(Integer, primary_key=True)
    player_id = Column("player_id", Integer, ForeignKey("player.id"))
    questions_id = Column("questions_id", Integer, ForeignKey("questions.id"))
    score = Column("score", Float)
    player = relationship("Player")
    questions = relationship("Questions")

    # noinspection PyMissingConstructor
    def __init__(self, player_id, questions_id, score):
        self.player_id = player_id
        self.questions_id = questions_id
        self.score = score

    def __repr__(self):
        return f"{self.player_id}) {self.questions_id} - {self.score}"


class AnswerHistory(Base):
    """
    Sukuria lentelę kurioje laikoma žaidėjo atsakymų istorija.
    """
    __tablename__ = "answer_history"
    id = Column(Integer, primary_key=True)
    player_id = Column("player_id", Integer, ForeignKey("player.id"))
    questions_id = Column("questions_id", Integer, ForeignKey("questions.id"))
    answer = Column("answer", String)
    player = relationship("Player")
    questions = relationship("Questions")

    # noinspection PyMissingConstructor
    def __init__(self, player_id, questions_id, answer):
        self.player_id = player_id
        self.questions_id = questions_id
        self.answer = answer

    def __repr__(self):
        return f"{self.id}) {self.player_id} - {self.questions_id} - {self.answer}"


class Player(Base):
    """
    Sukuria lentelę kurioje laikoma žaidėjo informacija.
    """
    __tablename__ = "player"
    id = Column(Integer, primary_key=True)
    name = Column("name", String)
    last_name = Column("last_name", String)
    date = Column("date", DateTime)

    # noinspection PyMissingConstructor
    def __init__(self, date, name, last_name):
        self.date = date
        self.name = name
        self.last_name = last_name

    def __repr__(self):
        return f"{self.id}) {self.date} - {self.name} {self.last_name}"


Base.metadata.create_all(engine)
