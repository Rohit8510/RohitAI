last_prompt = {}
last_response = {}


def save_last(user_id: int, prompt: str, response: str):
    last_prompt[user_id] = prompt
    last_response[user_id] = response


def get_last_prompt(user_id: int):
    return last_prompt.get(user_id)


def get_last_response(user_id: int):
    return last_response.get(user_id)


def clear_last(user_id: int):
    last_prompt.pop(user_id, None)
    last_response.pop(user_id, None)
