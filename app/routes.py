# app/routes.py

from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from .models import db, Episode, Guest, Appearance

# Create blueprint and attach Api to it
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# GET /episodes
class EpisodesResource(Resource):
    def get(self):
        episodes = Episode.query.all()
        return [e.short_dict() for e in episodes], 200

# GET /episodes/<id> and DELETE
class EpisodeByIdResource(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404
        return episode.to_dict(), 200

    def delete(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404
        db.session.delete(episode)
        db.session.commit()
        return {}, 204

# GET /guests
class GuestsResource(Resource):
    def get(self):
        guests = Guest.query.all()
        return [g.to_dict() for g in guests], 200

# POST /appearances
class AppearanceResource(Resource):
    def post(self):
        from flask import request

        data = request.get_json()
        try:
            rating = int(data.get("rating"))
            episode_id = int(data.get("episode_id"))
            guest_id = int(data.get("guest_id"))

            episode = Episode.query.get(episode_id)
            guest = Guest.query.get(guest_id)

            if not episode or not guest:
                return {"errors": ["Invalid episode_id or guest_id"]}, 400

            appearance = Appearance(
                rating=rating,
                episode_id=episode_id,
                guest_id=guest_id
            )

            db.session.add(appearance)
            db.session.commit()
            return appearance.to_dict(), 201

        except Exception as e:
            db.session.rollback()
            return {"errors": [str(e)]}, 400

# Register resources with Api
api.add_resource(EpisodesResource, '/episodes')
api.add_resource(EpisodeByIdResource, '/episodes/<int:id>')
api.add_resource(GuestsResource, '/guests')
api.add_resource(AppearanceResource, '/appearances')
