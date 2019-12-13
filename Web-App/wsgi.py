from aplicacion_demo import create_app
from dotenv import load_dotenv
from logging import FileHandler

file_log = FileHandler('systemlog.txt')


load_dotenv()
app = create_app()
app.config['SECRET_KEY'] = 'altosecreto'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
    