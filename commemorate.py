# charset=utf8
from flask import Flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:cyx44322923.@localhost/mysql_demo?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
CORS(app)


class Commemorate(db.Model):
    __tablename__ = "commemorates"
    post_id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        dict_data = {
            'post_id': self.id,
            'body': self.body,
            'body_html': self.body_html,
            'timestamp': self.timestamp,
        }
        return dict_data

    def __repr__(self):
        return '<Test %r>' % self.id


    db.create_all()


@app.route('/', methods=["POST", "GET"])
def add_commemorate():
    if methods == "POST":
        data = {"post_id": request.json.get("id"),
                "body": request.json.get("body"),
                "body_html": request.json.grt("body_html"),
                "timestamp": request.json.get("timestamp")}
        commemorate = Commemorate(**data)
        db.session.add(commemorate)
        db.session.commit()
        return jsonify({
            "status": 1,
            "message": "操作成功",
            "data": ""})
    if methods == "GET":
        post_id = request.args.get("post_id")
        commemorates = Commemorate.query.filter_by(post_id=post_id).all()
        data = [commemorate.to_dict() for commemorate in commemorates]
        return jsonify({
            "status": 1,
            "message": "操作成功",
            "data": data})


@app.route('/', methods=["DELETE"])
def delete_commemorate():
    id_ = request.args.get("id")
    commemorate = Commemorate.query.get(id_)
    if not commemorate:
        return jsonify({
            "status": 1,
            "message": "操作成功",
            "data": ""
        })
    db.session.delete(commemorate)
    db.session.commit()
    return jsonify({
        "status": 1,
        "message": "操作成功",
        "data": ""
    })


if __name__ == '__main__':
    app.run(debug=True)
