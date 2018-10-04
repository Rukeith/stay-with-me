import sys
from flask import Flask, render_template, request, abort, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# from model import createData, queryData

# 第一個參數是此模組的名稱，此為必須讓 Flask 知道根目錄在哪
# 讓 Flask 可以找到靜態檔案和模版等
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:pass@shopee24-mysql:3306/shopee24_dev'
db = SQLAlchemy(app)
db.create_all()


class Demo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Demo %r>' % self.username


def createData():
    admin = Demo(username='admin', email='admin@example.com')
    db.session.add(admin)
    db.session.commit()


# 範例一：渲染模板
@app.route('/')
def index():
    return render_template('index.html', name='HaHa')


# 範例二：回傳文本
@app.route('/hello')
def hello():
    createData()
    return 'Hello, World'


# 範例三：讀取 params
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    try:
        result = Demo.query.all()
        print(result[0])
        print(str(result))
        sys.stdout.write(str(result))
        return 'User %s' % result
    except ValueError:
        return 'User %s' % ValueError
    


# string	（默認值）接受任何沒有斜杠的文本
# int	接受正整數
# float	接受正浮點值
# path	喜歡string但也接受斜線
# uuid	接受UUID字符串
# 範例四：在 params 加入 converter
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


# 範例五：在 params 讀取 /path 之後的路徑
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath


# 範例六：/projects redirect to /projects
@app.route('/projects/')
def projects():
    return 'The project page'


# 範例七：/about/ redirect to /about
@app.route('/about')
def about():
    return 'The about page'


# 範例八：判斷 REST 的 Methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'post login'
    else:
        return 'get login'


# 範例九：取讀 query
@app.route('/query', methods=['GET'])
def query():
    queryKey = request.args.get('key', '')
    if queryKey == 'vv':
        return 'Yes!'
    print('vasd f ==')
    print('vasd queryKey ==', queryKey)
    return 'Get query'


# 範例十：redirect
@app.route('/redirect', methods=['GET'])
def redirect_login():
    return redirect(url_for('login'))


# 範例十一：custom page not found
@app.errorhandler(404)
def page_not_found(error):
    return render_template('index.html', name="not found"), 404


# 範例十二：abort
@app.route('/abort', methods=['GET'])
def abort_page():
    abort(404)