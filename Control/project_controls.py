from Models import Questions, QuestionHistory, Player, AnswerHistory, Answers
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from Models.DB_models import engine
import random

Session = sessionmaker(bind=engine)
session = Session()


def get_questions_list():
    """
    Iš Questions lentelės gauna klausimų sąrašą.
    Returns: Klausimų sąrašą

    """
    questions = []
    listas = session.query(Questions.question).all()
    for i in listas:
        questions.append(i[0])
    return questions


def get_answers_list():
    """
    Iš Questions lentelės gauna galimų atsakymų sąrašą.
    Returns: Galimų atsakymų sąrašą

    """
    answers = []
    listas = session.query(Questions.choices).all()
    for i in listas:
        answers.append(i[0])
    return answers


def shuffle_questions_answers():
    """
    Išmaišo klausimus ir atsakymus atsitiktine
    tvarka.
    Returns: Atsakymų ir klausimų sąrašus

    """
    answers = get_answers_list()
    questions = get_questions_list()
    shuf = list(zip(answers, questions))
    random.shuffle(shuf)
    answers, questions = zip(*shuf)
    return answers, questions


def register_player(name, last_name, date):
    """
    Užregistruoja naują žaidėją DB.
    Args:
        name: Žaidėjo vardas
        last_name: Žaidėjo pavardė
        date: Registracijos data

    Returns: None

    """
    player = Player(name=name, last_name=last_name, date=date)
    session.add(player)
    session.commit()


def get_question_id(question):
    """
    Gauna klausimo ID pagal klausimo stringą.
    Args:
        question: Klausimo stringas

    Returns: Klausimo ID

    """
    result = session.query(Questions).filter(Questions.question == question).first()
    return result.id


def get_last_player_id():
    """
    Gauna paskutinio žaidėjo ID.
    Returns: Paskutinio žaidėjo ID

    """
    result = session.query(Player).order_by(Player.id.desc()).first()
    return result.id


def write_answer_history(player_id, question_id, answer):
    """
    Įrašo žaidėjo atsakytą klausimą ir atsakymą į DB.
    Args:
        player_id: Žaidėjo ID
        question_id: Klausimo ID
        answer: Atsakymas

    Returns: None

    """
    answer = AnswerHistory(player_id=player_id, questions_id=question_id, answer=answer)
    session.add(answer)
    session.commit()


def write_questions_history(player_id, question_id, score):
    """
    Įrašo žaidėjui duotus klausimus ir jo surinktus taškus
    už klausimą į DB.
    Args:
        player_id: Žaidėjo ID
        question_id: Klausimo ID
        score: Taškai

    Returns: None

    """
    question = QuestionHistory(
        player_id=player_id, questions_id=question_id, score=score
    )
    session.add(question)
    session.commit()


def get_correct_answer(question_id):
    """
    Gauna teisingą atsakymą į klausimą pagal klausimo ID.
    Args:
        question_id: Klausimo ID.

    Returns: Teisingas atsakymas

    """
    result = session.query(Answers).get(question_id)
    return result.correct_answer


def get_final_score(player_id):
    """
    Gauna galutinį žaidėjo rezultatą po žaidimo pagal jo ID.
    Args:
        player_id: Žaidėjo ID.

    Returns: Žaidimo rezultatas

    """
    result = (
        session.query(func.sum(QuestionHistory.score))
        .filter(QuestionHistory.player_id == player_id)
        .first()
    )
    return result[0]


def last_player_score(player_id):
    """
    Gauna žaidėjo atasakytus klausimus, pasirinktus atsakymus ir
    teisingus atsakymus po žaidimo pagal žaidėjo ID.
    Args:
        player_id: Žaidėjo ID.

    Returns: Rezultatų sąrašas

    """
    data = (
        session.query(AnswerHistory).filter(AnswerHistory.player_id == player_id).all()
    )
    result = []
    for i in data:
        inter = [i.questions.question, i.answer, i.questions.answers.correct_answer]
        result.append(inter)
    return result


def top_10_scores():
    """
    Gauna Top 10 geriausiai sužaidusių žaidėjų rezultatus pagal
    surinktus taškus.
    Returns: Sąrašą su top 10 geriausiais rezultatais.

    """
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
        .limit(10)
    )
    result = []
    for i in data:
        inter = [i.date, i.name, i.last_name, i.score]
        result.append(inter)
    return result


def get_date_range(start, end):
    """
    Gauna visus rezultatus su žaidimo data, žaidėjo vardu bei pavarde
    tam tikrame datų intervale.
    Args:
        start: Pradinė data
        end: Galutinė data

    Returns: Rezultatų sąrašas

    """
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


def get_questions_answers():
    """
    Išmaišo ir iteruoja po vieną visus išmaišytus klausimus bei atsakymus.
    Returns: Vieną atsakymą ir vieną klausimą

    """
    answers, questions = shuffle_questions_answers()
    answer = iter(answers)
    question = iter(questions)
    return answer, question
