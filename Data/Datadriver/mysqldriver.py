import pymysql
import sys
class SQLDBdriver(object):
    # 基础属性，加入一个驱动版本的值，self._dver
    def __init__(self,host,uname,upwd,basedb):
        self._hst  = host
        self._unm  = uname
        self._pwd  = upwd
        self._odb  = basedb
        self._conn  = None
        self._ReConnect()
    def _ReConnect(self):
        if not self._conn:
            try:
                self._conn = pymysql.connect(host=self._hst, database=self._odb, user=self._unm,password=self._pwd,charset='utf8')
            except Exception as ex:
                ex_type, ex_val, ex_stack = sys.exc_info()
                return ex_val
        else:
                pass
    def __del__(self):
        if self._conn:
            self._conn.close()
            self._conn = None
    def _NewCursor(self):
        if self._conn is None:
            return False
        else:
            cur = self._conn.cursor()
            if cur:
                return cur
            else:
                print("#Error# Get New Cursor Failed")
                return False
    def _DelCursor(self, cur):
        if cur:
            cur.close()
        # 检查sql语句
    def PermitedUpdateSql(self, sql):
        rt = True
        lrsql = sql.lower()
        sql_elems = lrsql.strip().split()
        # 判断sql单词个数
        if len(sql_elems) < 3:
            rt = False
        elif sql_elems[0] == 'update':
            if 'set' not in sql_elems:
                rt = False
            else:
                rt = True
        elif sql_elems[0] == 'delete':
            if 'from' not in sql_elems:
                rt = False
            else:
                rt = True
        elif sql_elems[0] == 'insert':
            if sql_elems[1] != 'into':
                rt = False
            else:
                rt = True
        return rt
    # 导出结果
    def Export(self, sql, file_name, colfg='||'):
        rt = self.Query(sql)
        if rt:
            with open(file_name, 'a') as fd:
                for row in rt:
                    ln_info = ''
                    for col in row:
                        ln_info += str(col) + colfg
                    ln_info += '\n'
                    fd.write(ln_info)
    # 查询
    def Query(self, sql, nStart=0, nNum=-1):
        rt = []
        cur = self._NewCursor()
        if not cur:
            return False
        cur.execute(sql)
        if (nStart == 0) and (nNum == 1):
            rt.append(cur.fetchone())
        else:
            rs = cur.fetchall()
            if nNum == -1:
                rt.extend(rs[nStart:])
            else:
                rt.extend(rs[nStart:nStart + nNum])
        self._DelCursor(cur)
        return rt
    # 更新
    def Exec(self, sql):
        rt = None
        cur = self._NewCursor()
        conn = self._conn
        if not cur:
            return rt
        if SQLDBdriver.PermitedUpdateSql(self, sql) == False:
            return rt
        try:
            cur.execute(sql)
            conn.commit()
            # row = cur.rowcount
        except Exception as ex:
            ex_type, ex_val, ex_stack = sys.exc_info()
            return ex_val
        self._DelCursor(cur)
        # print('ok') 调试语句是否成功用的标记
        # print(cur.rowcount)
        if cur.rowcount > 0:
            return True
        elif cur.rowcount == 0 and ('update' in sql or 'insert' in sql):
            return False
        else:
            return True
    # 关闭游标
    def Exit(self):
        con = self._conn
        con.close()
    def SQLcon(self):
        try:
            con = pymysql.connect(host=self._hst, database=self._odb, user=self._unm, password=self._pwd,charset='utf8')
            return True
        except Exception as e:
            return False


if __name__ =='__main__':
    port = '3306'
    host = "127.0.0.1"
    user = 'root'
    pwd = "root"
    basedb = "jxbigdata"
    a = SQLDBdriver(host,user,pwd,basedb)
    sql  = "select pname from jx_person"
    # c = a.Query(sql)
    c = a.SQLcon()
    print(c)

