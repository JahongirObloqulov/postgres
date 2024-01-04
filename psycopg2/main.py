import psycopg2

conn = psycopg2.connect("dbname=dvdrental user=postgres password=123456")
cursor = conn.cursor()
cursor.execute("""
        CREATE TABLE if not exists student(
            id bigserial primary key,
            first_name varchar(20) not null,
            last_name varchar(20) not null,
            age int not null)

""")
conn.commit()

cursor.execute("""
        insert into student (first_name, last_name, age)
        values('Yasmina', 'Saydulloyeva', 1),
        ('Jahongir', 'Obloqulov', 27)
""")
conn.commit()