from app import app
from flask_apscheduler import APScheduler
from utils import db_clear

import views

if __name__ == "__main__":
    # Scheduler init
    scheduler = APScheduler()
    scheduler.init_app(app)

    # Scheduler add
    scheduler.start()
    scheduler.add_job(id='clear DB', func = db_clear, trigger = 'interval', seconds = 5)

    # Start whole app
    app.run()