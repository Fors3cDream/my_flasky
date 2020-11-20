from my_app import app, db
from my_app.catalog.models import User, Role

# 注册shell上下文处理器 - 返回一个字典，包含数据库实例和模型
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

if __name__ == "__main__":
    app.run(port=8080, debug=True)