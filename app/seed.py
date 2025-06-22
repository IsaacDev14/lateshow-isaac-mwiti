# app/seed.py

from app import app, db
from app.models import Episode, Guest, Appearance

def seed_data():
    with app.app_context():
        print("🔄 Clearing existing data...")
        Appearance.query.delete()
        Guest.query.delete()
        Episode.query.delete()

        print("🌱 Seeding episodes...")
        e1 = Episode(date="1/11/99", number=1)
        e2 = Episode(date="1/12/99", number=2)

        print("🌱 Seeding guests...")
        g1 = Guest(name="Michael J. Fox", occupation="actor")
        g2 = Guest(name="Sandra Bernhard", occupation="Comedian")
        g3 = Guest(name="Tracey Ullman", occupation="television actress")

        print("🌱 Seeding appearances...")
        a1 = Appearance(rating=4, episode=e1, guest=g1)
        a2 = Appearance(rating=5, episode=e2, guest=g3)

        db.session.add_all([e1, e2, g1, g2, g3, a1, a2])
        db.session.commit()
        print("✅ Database seeded!")

if __name__ == '__main__':
    seed_data()
