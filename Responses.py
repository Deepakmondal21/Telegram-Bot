from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup", "hii"):
        return "Hello!! I'm Mr. Bot. How can I assist you!"

    if user_message in ("who are you", "who are you?"):
        return "I'm Mr. Bot!"

    if user_message in ("how are you", "How are you?"):
        return "I am great!!! What about you?"

    if user_message in ("Who created you", "who created you", "who create you?"):
        return "Deepak Kumar Mondal created me."

    if user_message in ("time", "time?", "date","date?"):
        now  = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "I don't understand you. I'm Still learning. You can search it on Google!"