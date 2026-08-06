import sqlite3


class DatabaseAgent:

    def __init__(self):
        self.connection = sqlite3.connect("database/database.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales_history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            total_sales REAL,
            average_sales REAL,
            highest_sale REAL,
            lowest_sale REAL,
            prediction REAL
        )
        """)

        self.connection.commit()

    def save_analysis(self, analysis, prediction):

        self.cursor.execute("""
        INSERT INTO sales_history
        (total_sales, average_sales, highest_sale, lowest_sale, prediction)
        VALUES (?, ?, ?, ?, ?)
        """, (
            float(analysis["Total Sales"]),
            float(analysis["Average Sales"]),
            float(analysis["Highest Sale"]),
            float(analysis["Lowest Sale"]),
            float(prediction)
        ))

        self.connection.commit()

    def close(self):
        self.connection.close()