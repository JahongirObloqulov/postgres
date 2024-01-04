import psycopg

with psycopg.connect("dbname=dvdrental user=postgres password=123456") as conn:
    conn.execute("""
            CREATE TABLE if not exists student(
                id bigserial primary key,
                first_name varchar(20) not null,
                last_name varchar(20) not null,
                age int not null)

    """)
    conn.commit()
    conn.execute("""
            insert into student (first_name, last_name, age)
            values ('Ali', 'Valiyev', 20),
            ('Saydullo', 'Xodiyev', 55)
    """)
    conn.commit()
