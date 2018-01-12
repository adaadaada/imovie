# coding:utf8


from datetime import datetime
from app import db


# 用户
class User(db.Model):
    __tablename__ = "user"  # 在数据库中的表名
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名字
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号
    info = db.Column(db.Text)  # 个人简介
    icon = db.Column(db.String(255))  # 头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
    uuid = db.Column(db.String(100), unique=True)  # 唯一标识符
    userlogins = db.relationship("UserLogin", backref="user")  # 用户登录数据表外键关联
    comments = db.relationship("Comment", backref="user")  # 评论数据表外键关联
    moviecols = db.relationship("Moviecol", backref="user")  # 收藏数据表外键关联

    def __repr__(self):
        return "<User %r>" % self.name


# 用户登录日志
class UserLogin(db.Model):
    __tablename__ = "userlogin"  # 在数据库中的表名
    id = db.Column(db.Integer, primary_key=True)  # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属的用户编号
    ip = db.Column(db.String(100))  # 登录的IP
    logintime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间

    def __repr__(self):
        return "<UserLogin %r>" % self.id


# 标签
class Tag(db.Model):
    __tablename__ = "tag"  # 在数据库中的表名
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 标签名称
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    movies = db.relationship("Movie", backref="tag")  # 外键申明

    def __repr__(self):
        return "<Tag %r>" % self.name


# 电影
class Movie(db.Model):
    __tablename__ = "movie"  # 在数据库中的表名
    id = db.Column(db.Integer, primary_key=True)  # 电影编号
    title = db.Column(db.String(255), unique=True)  # 电影名称
    url = db.Column(db.String(255))  # 电影播放的url
    info = db.Column(db.Text)  # 电影简介
    logo = db.Column(db.String(255))  # 电影封面
    star = db.Column(db.SmallInteger)  # 电影星级
    playnum = db.Column(db.BigInteger)  # 电影的播放次数
    commentnum = db.Column(db.BigInteger)  # 电影的评论量
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))  # 所属标签编号
    area = db.Column(db.String(100))  # 上映地区
    releasetime = db.Column(db.Date)  # 上映时间
    length = db.Column(db.String(100))  # 电影时长
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    comments = db.relationship("Comment", backref="movie")  # 评论数据表外键关联
    moviecols = db.relationship("Moviecol", backref="movie")  # 收藏数据表外键关联

    def __repr__(self):
        return "<Movie %r>", self.title


# 预告

class Preview(db.Model):
    __tablename__ = "preview"  # 在数据库中的表名
    id = db.Column(db.Integer, primary_key=True)  # 预告编号
    title = db.Column(db.String(255), unique=True)  # 预告名称
    logo = db.Column(db.String(255))  # 预告封面
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 预告添加时间

    def __repr__(self):
        return "<Preview %r>", self.title


# 评论
class Comment(db.Model):
    __tablename__ = "comment"  # 在数据库中的表名
    id = db.Column(db.Integer, primary_key=True)  # 评论编号
    content = db.Column(db.Text)  # 评论内容
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 评论时间

    def __repr__(self):
        return "<Comment %r>", self.id


# 电影收藏
class Moviecol(db.Model):
    __tablename__ = 'moviecol'
    id = db.Column(db.Integer, primary_key=True)  # 收藏编号
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    def __repr__(self):
        return "<Moviecol %r>", self.id


# 权限
class Auth(db.Model):
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    url = db.Column(db.String(100))  # 地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    def __repr__(self):
        return "<Auth %r>", self.name


# 角色
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    auths = db.Column(db.String(600))  # 地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    admins = db.relationship("Admin", backref="role")  #管理员的外键关联
    def __repr__(self):
        return "<Role %r>", self.name

#管理员
class Admin(db.Model):
    __tablename__ = "admin"  # 在数据库中的表名
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 管理员账号
    pwd = db.Column(db.String(100))  # 管理员密码
    is_super = db.Column(db.SmallInteger) #是否是超级管理员，0为超级管理员
    role_id= db.Column(db.Integer, db.ForeignKey("role.id"))#所属角色
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    adminlogs = db.relationship("AdminLog", backref="admin")  #管理员登录的外键关联
    oplogs = db.relationship("OpLog", backref="admin")  #后台操作日志的外键关联
    def __repr__(self):
        return "<Admin %r>", self.name

#管理员登录日志
class AdminLog(db.Model):
    __tablename__ = "adminlog"  # 在数据库中的表名
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员
    ip = db.Column(db.String(100))  # 登录的IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间

    def __repr__(self):
        return "<AdminLog %r>" % self.id

#后台操作日志
class OpLog(db.Model):
    __tablename__ = "oplog"  # 在数据库中的表名
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员
    ip = db.Column(db.String(100))  # 登录的IP
    reason = db.Column(db.String(600))  #操作原因
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间

    def __repr__(self):
        return "<OpLog %r>" % self.id

if __name__ =="__main__":
    pass
    # db.create_all()
    # role = Role(
    #     name="超级管理员",
    #     auths=''
    # )
    # db.session.add(role)
    # db.session.commit()
    # from werkzeug.security import generate_password_hash
    # admin = Admin(
    #     name = 'owen',
    #     pwd=generate_password_hash('123456'),
    #     is_super = 0,
    #     role_id=1
    # )
    # db.session.add(admin)
    # db.session.commit()