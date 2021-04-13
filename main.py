from app import create_app
import views

if __name__ == "__main__":
    create_app()
    # i tu powinno być with app.app_context():
    # reservation_annulation_scheduler()
    app.run()