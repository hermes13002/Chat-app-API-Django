import psycopg2


def main():
    conn = psycopg2.connect('postgres://avnadmin:AVNS_M8uej_XeNUFv87FReXH@pg-1409a7a7-soaresayoigbala-aa54.h.aivencloud.com:20226/defaultdb?sslmode=require')

    query_sql = 'SELECT VERSION()'

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()[0]
    print(version)


if __name__ == "__main__":
    main()