import sqlite3

DB_PATH = "database/sop.db"


def add_sop(
    department,
    process_name,
    objective,
    roles,
    steps,
    kpis,
    risks,
    automation
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO sops(
        department,
        process_name,
        objective,
        roles,
        steps,
        kpis,
        risks,
        automation
    )
    VALUES(?,?,?,?,?,?,?,?)
    """,
    (
        department,
        process_name,
        objective,
        roles,
        steps,
        kpis,
        risks,
        automation
    ))

    conn.commit()
    conn.close()


def get_all_sops():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sops")

    rows = cursor.fetchall()

    conn.close()

    return rows

#get sop by id 
def get_sop_by_id(sop_id):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM sops WHERE id=?",
        (sop_id,)
    )

    sop = cursor.fetchone()

    conn.close()

    return sop

#delete existing SOP
def delete_sop(sop_id):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM sops WHERE id=?",
        (sop_id,)
    )

    conn.commit()
    conn.close()

#Update an SOP
def update_sop(
    sop_id,
    department,
    process_name,
    objective,
    roles,
    steps,
    kpis,
    risks,
    automation
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE sops
    SET
        department=?,
        process_name=?,
        objective=?,
        roles=?,
        steps=?,
        kpis=?,
        risks=?,
        automation=?
    WHERE id=?
    """,
    (
        department,
        process_name,
        objective,
        roles,
        steps,
        kpis,
        risks,
        automation,
        sop_id
    ))

    conn.commit()
    conn.close()

#Search an SOP
def search_sop(keyword):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM sops
    WHERE process_name LIKE ?
    """,
    (f"%{keyword}%",)
    )

    results = cursor.fetchall()

    conn.close()

    return results

