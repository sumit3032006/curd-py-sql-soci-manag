# Society Maintenance Management System

A console-based **CRUD application** built with **Python** and **MySQL** to manage society members and their monthly maintenance payment status. The project uses a clean multi-file structure (config, model, controller) and parameterized SQL queries.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)
![Type](https://img.shields.io/badge/Interface-Console-lightgrey)

---

## Features

- **Add** a society member (name, flat number, phone, monthly maintenance, payment status)
- **View** all members in a formatted table
- **Search** a member by ID or by full / partial name
- **Update** member details (leave a field blank to keep the old value)
- **Delete** a member with Y/N confirmation
- Input validation for empty values, invalid numbers, negative amounts and invalid payment status
- Parameterized queries (SQL-injection safe) with commit / rollback on errors

## Tech Stack

| Technology | Use |
|---|---|
| Python 3 | Application logic |
| mysql-connector-python | Connect Python to MySQL |
| MySQL | Database |
| MySQL Workbench | Run the SQL script / view data |

## Project Structure

```
curd-py-sql-soci-manag/
├── main.py                       # Entry point
├── config/
│   └── db.py                     # MySQL connection settings
├── model/
│   └── SocietyModel.py           # Database operations (INSERT / SELECT / UPDATE / DELETE)
├── controller/
│   └── SocietyController.py      # Menus, input and validation
├── database/
│   └── society_db.sql            # Database and table creation script
└── screenshots/                  # Console screenshots used in this README
```

## Database

Database: `society_db12` | Table: `society_members`

| Field | Type | Constraints |
|---|---|---|
| member_id | INT | PRIMARY KEY, AUTO_INCREMENT |
| member_name | VARCHAR(100) | NOT NULL |
| flat_number | VARCHAR(20) | NOT NULL |
| phone | VARCHAR(15) | NOT NULL |
| monthly_maintenance | DECIMAL(10,2) | NOT NULL, DEFAULT 0.00 |
| payment_status | VARCHAR(20) | NOT NULL, DEFAULT 'Pending' |

## Setup and Run

**1. Clone the repository**

```bash
git clone https://github.com/sumit3032006/curd-py-sql-soci-manag.git
cd curd-py-sql-soci-manag
```

**2. Install the MySQL connector**

```bash
pip install mysql-connector-python
```

**3. Create the database and table**

Open `database/society_db.sql` in MySQL Workbench and execute it.

**4. Configure the connection**

Edit `config/db.py` and set your own MySQL details:

```python
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "your_mysql_password"
DB_NAME = "society_db12"
```

> Do not commit your real password to GitHub.

**5. Run the program**

```bash
python main.py
```

## Screenshots

### Main Menu
![Main Menu](screenshots/01-main-menu.png)

### Add Society Member
![Add Member](screenshots/02-add-member.png)

### View All Members
![View Members](screenshots/03-view-members.png)

### Search Member
![Search Member](screenshots/04-search-member.png)

### Update Member
![Update Member](screenshots/05-update-member.png)

### Delete Member
![Delete Member](screenshots/06-delete-member.png)

### Input Validation
![Input Validation](screenshots/07-input-validation.png)

> Screenshots show sample data.

## How It Works

```
User -> Console menu -> Controller (validation) -> Model function -> Parameterized SQL -> MySQL -> Result on screen
```

- `controller/SocietyController.py` shows the menu, reads and validates input, and prints results.
- `model/SocietyModel.py` opens a connection, runs the SQL query, commits or rolls back, and closes the connection.
- `config/db.py` holds the connection settings and returns a connection.

## Limitations

- Console interface only, single user, no login
- Only the current payment status is stored (no month-wise bills or payment history)
- Duplicate flat numbers are not blocked; phone number is not checked for a 10-digit format

## Future Enhancements

- Admin login and environment-variable based database password
- Month-wise bills and payment history table
- Phone and duplicate flat number validation
- Reports (pending dues, collection) and PDF / Excel export
- Graphical or web interface

## Author

**Sumit Ravindra Jadhav**
