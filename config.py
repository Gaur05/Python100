# Database Connectivity
DB_USER = 'asset_management'
DB_PASSWORD = 'qwer1234'
DB_HOST = 'localhost'
DB_NAME = 'Asset_Management'

# DB_HOST = "localhost"
# DB_NAME = "Asset_Management"
# DB_USER = "asset_management"
# DB_PASS = "qwer1234"


SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

        
        
        
# import psycopg2
# from datetime import datetime

# log_file = "db_error_log.txt"

# try:
#     connection = psycopg2.connect(
#         user="asset_management",
#         password="qwer1234",
#         host="localhost",
#         port="5432",
#         database="Asset_Management"
#     )
#     cursor = connection.cursor()
#     cursor.execute("SELECT version();")
#     db_version = cursor.fetchone()
#     print("Connected to PostgreSQL database successfully!")
#     print("Database version:", db_version)

# except Exception as error:
#     print("Error connecting to database:", error)
#     # Log the error to a txt file
#     with open(log_file, "a") as f:
#         f.write(f"[{datetime.now()}] Error: {error}\n")

# finally:
#     if 'connection' in locals() and connection:
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection closed")