import json
def choose():
    while True:
        choice=input('请输入操作: 0.添加用户 1.登录 2.修改用户 3.退出')
        if choice=='1':
            login()
        elif choice=='0':
            add_user()
        elif choice=='2':
            modify_user()
        elif choice=='3':
            pass
        else:
            print('无效选项')
            continue
        break

def login():
    m=3
    while True:
        with open("密码存储.json", 'r', encoding='UTF-8') as f:
            file=json.load(f)
        print('你还有',m,'次机会')
        a = input('请输入用户名称')
        b = input('请输入用户密码')
        k=0
        for i in range(len(file["user"])):
            if a==file['user'][i] and b==file['pwd'][i]:
                k=1
        if k==1:
            print('登陆成功!')
            break
        else:
            print('错误!')
            m-=1
            if m==0:
                print('系统已被锁定!请联系管理员以解锁!')
                with open("锁定程序.json", 'w', encoding='UTF-8') as f:
                    json.dump({'result': 'True'}, f)
                break
def modify_user():
    m = 3
    while True:
        print('你还有', m, '次机会')
        a = input('请输入用户名称')
        b = input('请输入用户密码')
        with open("密码存储.json", 'r', encoding='UTF-8') as f:
            file=json.load(f)
        k = 0
        j=0
        for i in range(len(file["user"])):
            if a == file['user'][i] and b == file['pwd'][i]:
                j=i
                k = 1
        if k == 1:
            print('验证成功!')
            with open("管理员.json", 'r', encoding='UTF-8') as f:
                file1 = json.load(f)
            if file['user'][j]==file1['user'][0]:
                print('管理员身份登录')
                while True:
                    c=input('请输入要对用户执行的操作:1.修改用户名 2.修改密码 3.删除用户 4.退出')
                    if c=='1':
                        d=input('请输入新用户名')
                        file['user'].pop(j)
                        file['user'].insert(j,d)
                        file1['user'].pop()
                        file1['user'].insert(0,d)
                        with open("密码存储.json", 'w', encoding='UTF-8') as f2,open("管理员.json", 'w', encoding='UTF-8') as f1:
                            json.dump(file, f2)
                            json.dump(file1,f1)
                        print('操作成功!')
                    elif c=='2':
                        d = input('请输入新密码')
                        file['pwd'].pop(j)
                        file['pwd'].insert(j, d)
                        file1['pwd'].pop()
                        file1['pwd'].insert(0, d)
                        with open("密码存储.json", 'w', encoding='UTF-8') as f2, open("管理员.json", 'w',encoding='UTF-8') as f1:
                            json.dump(file, f2)
                            json.dump(file1, f1)
                        print('操作成功!')
                    elif c=='3':
                        q=input('是否删除用户?输入y以删除,输入其他键以撤销')
                        if q=='y':
                            file['user'].pop(j)
                            file1['user'].pop()
                            file['pwd'].pop(j)
                            file1['pwd'].pop()
                            with open("密码存储.json", 'w', encoding='UTF-8') as f2, open("管理员.json", 'w',encoding='UTF-8') as f1:
                                json.dump(file, f2)
                                json.dump(file1, f1)
                            print('操作成功!')
                        else:
                            continue
                    elif c=='4':
                        pass
                    else:
                        print('无效选项')
                        continue
                    break
            else:
                while True:
                    c=input('请输入要对用户执行的操作:1.修改用户名 2.修改密码 3.删除用户 4.退出')
                    if c=='1':
                        d=input('请输入新用户名')
                        file['user'].pop(j)
                        file['user'].insert(j,d)
                        with open("密码存储.json", 'w', encoding='UTF-8') as f:
                            json.dump(file, f)
                        print('操作成功!')
                    elif c == '2':
                        d = input('请输入新密码')
                        file['pwd'].pop(j)
                        file['pwd'].insert(j, d)
                        with open("密码存储.json", 'w', encoding='UTF-8') as f2:
                            json.dump(file, f2)
                        print('操作成功!')
                    elif c == '3':
                        q = input('是否删除用户?输入y以删除,输入其他键以撤销')
                        if q == 'y':
                            file['user'].pop(j)
                            file['pwd'].pop(j)
                            with open("密码存储.json", 'w', encoding='UTF-8') as f2:
                                json.dump(file, f2)
                            print('操作成功!')
                        else:
                            continue
                    elif c == '4':
                        pass
                    else:
                        print('无效选项')
                        continue
                    break
            break
        else:
            print('错误!')
            m -= 1
            if m == 0:
                print('系统已被锁定!请联系管理员以解锁!')
                with open("锁定程序.json", 'w', encoding='UTF-8') as f:
                    json.dump({'result': 'True'}, f)
                break

def add_user():
    a=check_admin()
    if a==1:
        a = input('请输入用户名称')
        b = input('请输入用户密码')
        with open("密码存储.json", 'r', encoding='UTF-8') as f:
            file=json.load(f)
        file['user'].append(a)
        file['pwd'].append(b)
        with open("密码存储.json", 'w', encoding='UTF-8') as f1:
            json.dump(file, f1)
        print('操作成功!')
def check_admin():
    print('请验证管理员身份!')
    with open("管理员.json", 'r', encoding='UTF-8') as f:
        file=json.load(f)
    a = input('请输入管理员名称')
    b = input('请输入管理员密码')
    k = 0
    for i in range(len(file["user"])):
        if a == file['user'][i] and b == file['pwd'][i]:
            k = 1
    if k == 1:
        print('验证成功!')
    else:
        print('错误!')
    return k



def unlock():
    with open("管理员.json", 'r', encoding='UTF-8') as f:
        file=json.load(f)
    a = input('请输入管理员名称')
    b = input('请输入管理员密码')
    k = 0
    for i in range(len(file["user"])):
        if a == file['user'][i] and b == file['pwd'][i]:
            k = 1
    if k == 1:
        print('解锁成功!')
        with open("锁定程序.json", 'w', encoding='UTF-8') as f:
            json.dump({'result':'False'},f)
    else:
        print('错误!')



def check():
    with open("锁定程序.json", 'r', encoding='UTF-8') as f:
        file=json.load(f)
    if file['result']=='False':
        choose()
    else:
        print('锁定中,请验证管理员身份以解锁!')
        unlock()

def admin():
    a=input('请输入管理员名称')
    b=input('请输入管理员密码')
    with open("管理员.json", 'r', encoding='UTF-8') as f1,open("密码存储.json", 'r', encoding='UTF-8') as f2:
        file1=json.load(f1)
        file2 =json.load(f2)
    file1['user'].append(a)
    file1['pwd'].append(b)
    file2['user'].append(a)
    file2['pwd'].append(b)
    with open("管理员.json", 'w', encoding='UTF-8') as f1,open("密码存储.json", 'w', encoding='UTF-8') as f2:
        json.dump({"user":[a],"pwd":[b]},f1)
        json.dump({"user":[a],"pwd":[b]},f2)
    print('操作成功!')


def main():
    with open("管理员.json", 'r', encoding='UTF-8') as f:
        file=json.load(f)
    if len(file['user'])==0:
        print('请先添加管理员!')
        admin()
    else:
        check()
if __name__ == '__main__':
    main()