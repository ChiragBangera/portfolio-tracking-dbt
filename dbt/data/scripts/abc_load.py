import duckdb

with duckdb.connect(database="dev.duckdb") as conn:
    conn.execute(
        query="""
        create schema if not exists positions;

        create or replace table positions.ABC_BANK_POSITIONS as
        select *
        from read_csv_auto('data/ABC_Bank_PORTFOLIO__2021-04-09.csv');
    """
    )
    print("Data load complete....")
    print("Testing load")
    test_data = conn.execute(query="select * from positions.ABC_BANK_POSITIONS")
    print(test_data.fetchall())
    print("Test complete")
