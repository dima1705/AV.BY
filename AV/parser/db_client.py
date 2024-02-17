import psycopg2

conn = psycopg2.connect(
        host='localhost',
        database='auto_s_probegom',
        user='postgres',
        password='postgres'
    )

cursor = conn.cursor()


def save_brand(mark):
    insert_query = """INSERT INTO "auto_brand" (brand) VALUES (%s);"""
    cursor.execute(insert_query, (mark,))
    conn.commit()


def save_model(model, brand_id):
    insert_query = """INSERT INTO "auto_model" (model, brand_id) VALUES (%s, %s);"""
    cursor.execute(insert_query, (model, brand_id))
    conn.commit()


def save_generation(generation, model_id):
    insert_query = """INSERT INTO "auto_gen" (generation, model_id) VALUES (%s, %s);"""
    cursor.execute(insert_query, (generation, model_id))
    conn.commit()


def save_auto(*params):
    insert_query = """INSERT INTO "Used_auto" (
                                                    name,
                                                    price_for_bel_rub,
                                                    price_for_usd,
                                                    year,
                                                    kpp,
                                                    volume,
                                                    type_engine,
                                                    probeg,
                                                    kyzov,
                                                    privod,
                                                    color,
                                                    power,
                                                    comment,
                                                    addcat_id
                                                    )
                                                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(insert_query, (params[:]))
    conn.commit()


def save_photo(s_photo, m_photo, b_photo, auto_id):
    insert_query = """INSERT INTO "auto_photo" (s_photo, m_photo, b_photo, auto_id) VALUES (%s, %s, %s, %s);"""
    cursor.execute(insert_query, (s_photo, m_photo, b_photo, auto_id))
    conn.commit()