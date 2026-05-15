import pandas as pd

def make_table(tables):
    rows = []
    for table in tables:
        rows.append({
            "統計名": table["STAT_NAME"]["$"],
            "タイトル": table["TITLE"],
            "調査年月": table.get("SURVEY_DATE", "不明"),
            "TABLE_ID": table.get("@id", "不明")
        })
    df = pd.DataFrame(rows)
    return df