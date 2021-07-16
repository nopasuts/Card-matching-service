from datetime import datetime

def generate_user_id():
  now = datetime.now()
  dt_string = now.strftime("USER-%d%m%YT%H%M%S")
  return dt_string