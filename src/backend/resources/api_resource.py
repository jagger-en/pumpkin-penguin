from flask_restful import Resource, request
from backend.utils.query import query_wrapper
from backend.utils.query import commit_wrapper
from backend.models.database import db

class ApiResource(Resource):

    NOT_FOUND = "Resource with id=%s not found"

    MODEL = None
    SCHEMA = None
    SCHEMA_MANY = None

    def get(self):
        form_data = dict(request.args)
        if form_data.get('id'):
            item = self.MODEL.query.get(form_data.get('id'))
            if item:
                return self.dump_one(item)
            return self.NOT_FOUND % form_data.get('id'), 404

        items, err = self._query_all()
        if not err is None:
            return err, 404

        return self.dump_many(items)

    def put(self):
        request_json = request.json
        self.MODEL.query.filter_by(id=request_json['id']).update(request_json)
        db.session.commit()
        return request_json, 201


    def post(self):
        request_json = request.json
        if type(request_json) == dict:
            return self.handle_single_entry(request_json)
        return "Failed to parse payload", 400

    def delete(self):
        form_data = dict(request.args)
        if form_data.get('id'):
            item = self.MODEL.query.get(form_data.get('id'))
            if item:
                db.session.delete(item)
                db.session.commit()
                return self.dump_one(item)
            return self.NOT_FOUND % form_data.get('id'), 404
        return "Resource id must be given", 400

    def handle_single_entry(self, payload):
        payload, err = self.extract_payload(payload)
        if not err is None:
            return err, 400

        new_record, err = self._add_new(payload)
        if not err is None:
            return err, 400

        new_record_from_db = self.MODEL.query.get(new_record.id)
        return self.dump_one(new_record_from_db, 201)

    def extract_payload(self, payload):
        '''Overrideable method'''
        return payload, None

    @commit_wrapper
    def _add_new(self, payload):
        from backend.models.database import db

        new_record = self._create_new_record(payload)

        # NOTE: We may need a context manager here.
        # This could cause some memory leakage.
        db.session.add(new_record)
        db.session.commit()
        return new_record

    def _create_new_record(self, payload):
        return self.MODEL(**payload)

    @query_wrapper
    def _query_all(self):
        return self.MODEL.query.all()

    def dump_one(self, item, code=200):
        form_data = dict(request.args)
        if form_data.get('nested') == "true":
            return self.SCHEMA_NESTED.dump(item), code
        return self.SCHEMA.dump(item), code

    def dump_many(self, items, code=200):
        form_data = dict(request.args)
        if form_data.get('nested') == "true":
            return self.SCHEMA_MANY_NESTED.dump(items), code
        return self.SCHEMA_MANY.dump(items), code
