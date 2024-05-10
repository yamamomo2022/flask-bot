from flask import Flask, render_template, request
from Chatcompletions import get_completion


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
  # ユーザーが入力したメッセージを取得
  message = request.form['message']

  # 応答メッセージを作成
  response =get_completion(message)

  # 応答メッセージをテンプレートに渡す
  return render_template('index.html', message=message, response=response)

if __name__ == '__main__':
  app.run(debug=True, host="127.0.0.1", port=8888)
