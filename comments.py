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


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer)
    post_id = db.Column(db.Integer)

    def to_dict(self):
        dict_data = {
            'id': self.id,
            'body': self.body,
            'author_id': self.author_id,
            'post_id': self.post_id,
            'timestamp': self.timestamp,
        }
        return dict_data

    def __repr__(self):
        return '<Test %r>' % self.id


db.create_all()


@app.route('/students/append', methods=["POST", "GET"])
def append_comment():
    # name = request.json.get("name")
    # clazz = request.json.get("clazz")
    # description = request.json.get("description")
    # id_card = request.json.get("id_card")
    if methods == "POST":
        data = {"id": request.json.get("id"),
                "body": request.json.get("body"),
                "body_html": request.json.get("body_html"),
                "timestamp": request.json.get("timestamp"),
                "author_id": request.json.get("author_id"),
                "post_id": request.json.get("post_id")}
        comment = Comment(**data)
        db.session.add(comment)
        db.session.commit()
        return jsonify({
            "status": 1,
            "message": "操作成功",
            "data": ""})
    if methods == "GET":
        post_id = request.args.get("post_id")
        comments = Comment.query.filter_by(post_id=post_id).all()
        data = [comment.to_dict() for comment in comments]

        return jsonify({
            "status": 1,
            "message": "操作成功",
            "data": data})


@app.route('/student', methods=["DELETE"])
def delete_comment():
    id_ = request.args.get("id")
    comment = comments.query.get(id_)
    if not comment:
        return jsonify({
            "status": 1,
            "message": "操作成功",
            "data": ""
        })
    db.session.delete(comment)
    db.session.commit()
    return jsonify({
        "status": 1,
        "message": "操作成功",
        "data": ""
    })


if __name__ == '__main__':
    app.run(debug=True)
