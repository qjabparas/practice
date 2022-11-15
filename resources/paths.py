from flask import Response, request
from database.models import Path
from flask_restful import Resource
from flask_jwt_extended import jwt_required

class PathsApi(Resource):

    def get(self):
        paths = Path.objects().to_json()
        return Response(paths, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):
        body = request.get_json()
        path = Path(**body).save()
        id = path.id
        return {"id": str(id)}, 200

class PathApi(Resource):

    @jwt_required()
    def put(self, id):
        body = request.get_json()
        Path.objects.get(id=id).update(**body)
        return 'Path was successfully updated', 200

    @jwt_required()
    def delete(self, id):
        Path.objects.get(id=id).delete()
        return 'Path was successfully deleted', 200