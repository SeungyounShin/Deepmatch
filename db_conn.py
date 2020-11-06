import sqlite3

class submit_table:
    def __init__(self):
        self.conn = sqlite3.connect('deepmatch_db.sqlite')

    def insert(self,task):

        sql = ''' INSERT INTO submit(date,age,sex,kakao_id,
                                height,body_type,is_student,
                                expect_height,expect_body_type,
                                q1,q2,q3,q4,q5,q6,q7,q8)
                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        cur = self.conn.cursor()
        cur.execute(sql, task)
        self.conn.commit()

        return cur.lastrowid

    def search_by_kakao(self,kakao_id):
        try:
            sql = "SELECT * FROM submit where kakao_id='{}'".format(kakao_id)
            cur = self.conn.cursor()
            rows = cur.execute(sql).fetchall()
            return rows
        except:
            return None

    def clear(self):
        sql = "DELETE FROM submit"
        try:
            cur = self.conn.cursor()
            rows = cur.execute(sql).fetchall()
            self.conn.commit()
        except:
            print("[ERROR] -> submit table clear")

    def show(self):
        sql = ''' SELECT * FROM submit'''
        try:
            cur = self.conn.cursor()
            rows = cur.execute(sql).fetchall()
            self.conn.commit()
        except:
            print("[ERROR] -> submit table show")
        for i in rows:
            print(i)

if __name__=="__main__":
    #파일을 직접 실행하면 submit table show
    print("SUBMIT TABLE SHOWS")

    submit = submit_table()
    #submit.clear()
    submit.show()
    print("="*10)
    print(submit.search_by_kakao('ssy10011218'))
