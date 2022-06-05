import MySQLdb

def db_conn():
    db=MySQLdb.connect("localhost",'test','test@123','python_test')
    cursor=db.cursor()
    cursor.execute("INSERT into test_table_1 SET name='Your Name', email='your_email@gmail.com',reg_no='o_i_don_t_have_it'")
    db.commit()
    db.close()
db_conn()
