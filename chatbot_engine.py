# chatbot_engine.py

from db_manager import get_db_connection
from ml_engine.learner import learn_new_knowledge
from nlp_engine.nlp_tools import clean_text

GOOGLE_MAPS_API_KEY = "AIzaSyAvxRo6DO02U-fiosqleHdUWn0ct7nVrok"

# To keep track of pending learn requests
pending_learning = {}

def get_answer(user_question):
    user_question_clean = clean_text(user_question)

    global pending_learning

    # Check if user is teaching the bot
    if pending_learning.get('waiting_for_answer'):
        # Save the previous question with this new answer
        learn_new_knowledge(pending_learning['question'], user_question)
        pending_learning = {}
        return "Thank you! I've learned this new information."

    # Detect Google Map requests
    if user_question_clean.startswith("show map of"):
        place = user_question_clean.replace("show map of", "").strip()
        map_url = f"https://www.google.com/maps/embed/v1/place?key={GOOGLE_MAPS_API_KEY}&q={place}+Sri+Lanka"
        iframe = f'<iframe width="100%" height="300" frameborder="0" style="border:0" src="{map_url}" allowfullscreen></iframe>'
        return iframe

    # Search in the knowledge base
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "SELECT answer FROM knowledge_base WHERE question LIKE %s"
    cursor.execute(query, ('%' + user_question_clean + '%',))
    result = cursor.fetchone()

    connection.close()

    if result:
        return result[0]
    else:
        # Start learning mode
        pending_learning = {
            'waiting_for_answer': True,
            'question': user_question_clean
        }
        return "I don't know the answer to that yet. Can you please teach me?"
