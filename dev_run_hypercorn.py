import uvicorn
from main.views import main


if __name__ == "__main__":
    uvicorn.run(main, port=8000, host='127.0.0.1', use_colors=True)
