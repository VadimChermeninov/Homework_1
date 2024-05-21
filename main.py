from json import JSONEncoder

from Models import post
from Models.storage import Storage
from flask import Flask, jsonify, request
from Models.post import Post

app=Flask(__name__)

my_storage = Storage()
class CUSTOMJSONEncoder(JSONEncoder):
    def default(self,obj):
        if isinstance(obj, Posts):
            return {'body': obj.body, 'author': obj.author}
        else:
            return super().default(obj)
app.json_encoder=CUSTOMJSONEncoder
@app.route('/ping',  methods=['GET'])
def ping():
    return jsonify({'responce':'pong'})

@app.route('/post/', methods=['POST'])## создаем пост
def create_post():
    post_json = request.get_json()
    post=Post(post_json('body')), post_json('author')
    my_storage.create_post(post)
    return jsonify({'status':'success'})

@ app.route('/post/<post_id>', methods=['GET'])## читаем пост по id
def get_post_by_id(post_id):
    return jsonify(my_storage.read_post(post_id))

@ app.route('/post/<post_id>', methods=['EDIT'])## редактируем пост
def update_post(post_id):
    post_json = request.get_json()
    post = Post(post_json('body')), post_json('author')
    my_storage.edit_post(post_id, post)
    return jsonify({'status':'success'})
@ app.route('/post/<post_id>', methods=['DELETE'])## удаляем пост
def delete_post(post_id):
    my_storage.delete_post(post_id)
    return jsonify({'status':'success'})
if __name__ == '__main__':
    app.run(debug=True)

