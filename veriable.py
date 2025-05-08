import os
from dotenv import load_dotenv

load_dotenv()



songs = {
    "skyfall": "https://www.youtube.com/watch?v=DeumyOzKqgI",
    "glory": "https://www.youtube.com/watch?v=HUZOKvYcx_o",
    "aura": "https://www.youtube.com/watch?v=m7Bc3pLyij0",
    "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA",
    "on my way": "https://www.youtube.com/watch?v=dhYOPzcsbGM",
    "neon blade": "https://www.youtube.com/watch?v=yiQ7S38nKog",
    "blinding lights": "https://www.youtube.com/watch?v=4NRXx6U8ABQ",
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "bad guy": "https://www.youtube.com/watch?v=DyDfgMOUjCI",
    "sunflower": "https://www.youtube.com/watch?v=ApXoWvfEYVU",
    "rockstar": "https://www.youtube.com/watch?v=U6h3vu5i8t4"
}
ai_api =os.getenv("AI_API_KEY")
news_api = os.getenv("NEWS")
weather_api = os.getenv("Weather")



