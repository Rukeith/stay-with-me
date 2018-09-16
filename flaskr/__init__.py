import os
from flask import Flask

def create_app(test_config=None):
    """
        建立 Flask 的 Instance，傳入 __name__（為此模組的名稱）
        讓 Flask 可以設定相關的路徑和參數
        instance_relative_config=True 告訴 Flask，設定文件是相對於 Instance 目錄
    """
    app = Flask(__name__, instance_relative_config=True)
    # SECRET_KEY 用來保護資料安全
    # DATABASE 說明 SQLite 資料庫檔案會存放的位置
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        # 將可以複寫設定
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    # 因為 flask 不會自動建立目錄給資料庫
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app