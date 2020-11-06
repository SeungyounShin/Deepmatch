body_type_list = ["마른","보통","통통"]

sex_map = {'남성':0, '여성':1}

q1_list = ["술 까지도 가능",
            "식사 정도는 할 수 있지 않나?",
            "둘이 만나는건 좀..."]

q2_list = ["연락을 꼬박 기다리는 스타일 입니다...(바빠도 자주!)",
            "각자 개인의 삶이 있으니 여유 있을 때",
            "연락 조금은 귀찮아..."]

q3_list = ["자만추(자보고 만남 추구)",
           "연인과 스킨십은 좋아요",
           "결혼 전 관계는 좀..."]

q4_list = ["연인이라면 럽스타는 필수",
           "스토리,카톡 등에 은근슬쩍은 가능",
           "사생활을 공개하고 싶지는 않음"]

q5_list = ["시간을 가지고 감정을 추스른 다음 이야기 하고 싶어요",
           "바로바로 해결했으면 좋겠어요"]

q6_list = ["일주일에 데이트 3세트 이상은 필수! 자주자주 보고싶어요",
           "평일에는 각자 일에 열중하고 주말에 재밌게 놀고 싶어요",
           "이주일에 한번 그 이상도 충분하다고 생각해요"]

q7_list = ["어느정도 사귀었다면 가족사와 같은 민감한 주제도 털어놓고 이야기하고 싶어요",
           "일상에서 힘들고 지쳤던 일 정도를 공유하고 이야기하고 싶어요",
           "상대가 힘들 수도 있기 때문에 혼자 해결하고 싶어요"]

q8_list = ["데이트 통장을 이용하는 것은 합리적 이에요",
           "각자 더치페이 하는 게 맞다고 생각해요",
           "돈 있는 사람이 조금 더 내는 것이 맞아요"]

def create_table(conn, create_table_sql):
    c = conn.cursor()
    c.execute(create_table_sql)
    return True

if __name__=="__main__":
    import sqlite3

    print("db setup start!")

    conn = sqlite3.connect('deepmatch_db.sqlite')

    db_columns=['age','sex','height','body_type','kakao_id','is_student',
              'expect_height','expect_body_type',
              'q1','q2','q3','q4','q5','q6','q7','q8']

    sql_create_submit_table = """CREATE TABLE IF NOT EXISTS submit (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        date text NOT NULL,
                                        age tinyint,
                                        sex tinyint,
                                        kakao_id text,
                                        height integer,
                                        body_type text,
                                        is_student text,
                                        expect_height text,
                                        expect_body_type text,
                                        q1 tinyint,
                                        q2 tinyint,
                                        q3 tinyint,
                                        q4 tinyint,
                                        q5 tinyint,
                                        q6 tinyint,
                                        q7 tinyint,
                                        q8 tinyint
                                    );"""

    if conn is not None:
        if create_table(conn, sql_create_submit_table):
            print("successfully create table submit")

    #c.close
    conn.close()
