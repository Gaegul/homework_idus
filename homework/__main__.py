import os

from homework.model import Base, engine
from homework.app import create_app

Base.metadata.create_all(engine)


if __name__ == '__main__':

    if os.getenv('ENV') == 'TEST':
        app = create_app()
        app.run(port=8080, debug=True)
    elif os.getenv('ENV') == 'PROD':
        app = create_app()
        app.run(host="0.0.0.0", port=8080, debug=False)
