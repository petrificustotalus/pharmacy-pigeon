from medivisor import app
from flask_apscheduler import APScheduler
from jobs import db_clear, db_confirm

from medivisor import views

def scheduler_db_clear():
    with scheduler.app.app_context():
        db_clear()

def scheduler_db_confirm():
    with scheduler.app.app_context():
        db_confirm()

if __name__ == "__main__":
    # Scheduler init
    scheduler = APScheduler()
    scheduler.init_app(app)

    # Scheduler add
    scheduler.start()
    # scheduler.add_job(id='confirm orders', func = scheduler_db_confirm, trigger = 'interval', seconds = 60)
    # scheduler.add_job(id='clear DB', func = scheduler_db_clear, trigger = 'interval', seconds = 3600)

    # Start whole app
    app.run()