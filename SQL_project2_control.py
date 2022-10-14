from SQL_project2_models import (
    Questions,
    Answers,
    QuestionHistory,
    AnswerHistory,
    Player,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from SQL_project2_models import engine
import random

Session = sessionmaker(bind=engine)
session = Session()


def get_questions_list():
    questions = []
    listas = session.query(Questions.question).all()
    for i in listas:
        questions.append(i[0])
    return questions


def get_answers_list():
    answers = []
    listas = session.query(Questions.choices).all()
    for i in listas:
        answers.append(i[0])
    return answers


def shuffle_questions_answers():
    answers = get_answers_list()
    questions = get_questions_list()
    shuf = list(zip(answers, questions))
    random.shuffle(shuf)
    answers, questions = zip(*shuf)
    return answers, questions


def register_player(name, last_name, date):
    player = Player(name=name, last_name=last_name, date=date)
    session.add(player)
    session.commit()


def get_question_id(question):
    result = session.query(Questions).filter(Questions.question == question).first()
    return result.id


def get_last_player_id():
    result = session.query(Player).order_by(Player.id.desc()).first()
    return result.id


def write_answer_history(player_id, question_id, answer):
    answer = AnswerHistory(player_id=player_id, questions_id=question_id, answer=answer)
    session.add(answer)
    session.commit()


def write_questions_history(player_id, question_id, score):
    question = QuestionHistory(
        player_id=player_id, questions_id=question_id, score=score
    )
    session.add(question)
    session.commit()


def get_correct_answer(question_id):
    result = session.query(Answers).get(question_id)
    return result.correct_answer


def get_final_score(player_id):
    result = (
        session.query(func.sum(QuestionHistory.score))
        .filter(QuestionHistory.player_id == player_id)
        .first()
    )
    return result[0]


def last_player_score(player_id):
    data = (
        session.query(AnswerHistory).filter(AnswerHistory.player_id == player_id).all()
    )
    result = []
    for i in data:
        inter = [i.questions.question, i.answer, i.questions.answers.correct_answer]
        result.append(inter)
    return result


def top_10_scores():
    data = (
        session.query(
            Player.date,
            Player.name,
            Player.last_name,
            func.sum(QuestionHistory.score).label("score"),
        )
        .join(Player)
        .group_by(Player.id)
        .order_by(func.sum(QuestionHistory.score).desc())
        .all()
    )
    result = []
    for i in data:
        inter = [i.date, i.name, i.last_name, i.score]
        result.append(inter)
    return result


def get_date_range(start, end):
    data = (
        session.query(
            Player.date,
            Player.name,
            Player.last_name,
            func.sum(QuestionHistory.score).label("score"),
        )
        .join(Player)
        .filter(Player.date.between(start, end))
        .group_by(Player.id)
        .all()
    )
    result = []
    for i in data:
        inter = [i.date, i.name, i.last_name, i.score]
        result.append(inter)
    return result
