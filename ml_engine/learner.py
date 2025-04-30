# ml_engine/learner.py

from db_manager import get_db_connection

def learn_new_knowledge(new_question, new_answer):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = "INSERT INTO knowledge_base (question, answer) VALUES (%s, %s)"
        cursor.execute(query, (new_question.lower(), new_answer))
        connection.commit()

        cursor.close()
        connection.close()

        return True
    except Exception as e:
        print(f"Error while learning new knowledge: {e}")
        return False
