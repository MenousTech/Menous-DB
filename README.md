<!-- ![test](assets/logo-full.png)


## Introduction
Menous DB is a simple and elegant key value database. It uses a structured file system to store key values. The database is written in python and can be used directly in python using the menousdb library that you can install from pip using the pypi repositories. 

## Installation
### 1) Mac
To install menousdb on Mac OS, you need to install the installer from the official repository releases. You can download it [here](https://github.com/MenousTech/Menous-DB/releases/tag/1.0.2) To use the menousdb just use the following command:

```
$ sudo menousdb --start
```

### 2) Linux
To install menousdb on any linux distro, you need to manually build the project
```
$ sudo apt-get install git
$ git clone https://github.com/MenousTech/Menous-DB
$ cd Menous-DB 
$ sudo apt-get install python3-pip
$ sudo python3 -m  pip install -r requirements.txt
$ sudo python3 -m pip install pyinstaller
$ cd src
$ sudo python3 -m PyInstaller --onefile api.py
$ sudo mv dist/api /usr/bin/menousdb
$ sudo menousdb --newuser
```

### 3) Windows
To install menousdb for Windows, you can use curl to download the latest exe from the github releases page. You can do this by running the following command

```
curl -o menousdb.exe https://github.com/MenousTech/Menous-DB/releases/download/1.0.2/menousdb.exe
```

After doing this, add the folder you have curled the file in to your environment path variables

## Release History
1) Version 0.1.0: https://github.com/MenousTech/Menous-DB/releases/tag/0.1.0
2) Version 0.0.1: https://github.com/MenousTech/Menous-DB/releases/tag/0.0.1 -->
# Menous DB Documentation
![test](assets/logo-full.png)
## Table of Contents
1. Introduction
2. System Requirements
3. Installation
4. Usage
5. API Endpoints
6. Examples
7. License
8. Author Information

---

## 1. Introduction

**Menous DB** is a lightweight, open-source database management system designed for simplicity and ease of use. It provides a RESTful API for managing databases and tables, making it suitable for a variety of applications. This documentation provides an overview of Menous DB, including system requirements, installation instructions, and usage guidelines.

### Features:
- Create, read, update, and delete databases and tables.
- Execute SQL-like queries using simple API endpoints.
- User authentication and authorization.
- JSON and SQL database modes.
- Cross-platform support (macOS, Windows, Linux).

---

## 2. System Requirements

To run Menous DB, you need the following software and dependencies installed on your system:

- Python 3.7+
- Flask (Python web framework)
- [auth](#) (Authentication module)
- Operating System: macOS, Windows, or Linux

---

## 3. Installation

Follow these steps to install and run Menous DB on your system:

### From hombrew for mac
1.  First tap from the repository of Menous Technologies
    ```
    $ brew tap menoustech/tap
    ```
2. Second update hombrew for changes
    ```
    $ brew update
    ```
3. Install menousdb using homebrew
    ```
    $ brew install menousdb
    ```

### Manual Build
1. Clone the Menous DB repository from GitHub:
   ```
   git clone https://github.com/snehashish0902/Menous-Db.git
   cd Menous-Db
   ```

2. Install the required Python packages using pip:
   ```
   pip install Flask
   ```

3. Create the configuration file based on your operating system:
   - macOS: `/Library/Caches/.menousdb/config.json`
   - Windows: `%APPDATA%\MenoudDb\config.json`
   - Linux: `/usr/local/bin/menousdb/config.json`

   Sample Configuration (config.json):
   ```
   {
       "mode": "json",
       "port": 5555
   }
   ```

4. Start Menous DB:
   - For the default port (5555), run `python menousdb.py --start`.
   - To specify a custom port, run `python menousdb.py --port <port_number>`.

---

## 4. Usage

Once Menous DB is running, you can use its RESTful API to manage databases and tables. You can interact with the API using HTTP requests and the provided endpoints. Here are some common actions you can perform:

- Create a new database.
- Check if a database exists.
- Create tables within a database.
- Insert data into tables.
- Query tables with various conditions.
- Update table records.
- Delete tables and databases.
- Authenticate users for secure access.

---

## 5. API Endpoints

### Database Management:

- **Create a Database:**
  - Endpoint: `/create-db`
  - Method: POST
  - Parameters: `key` (API key), `database` (database name)
  - Description: Creates a new database.

- **Check if a Database Exists:**
  - Endpoint: `/check-db-exists`
  - Method: GET
  - Parameters: `key` (API key), `database` (database name)
  - Description: Checks if a database exists.

- **Delete a Database:**
  - Endpoint: `/del-database`
  - Method: DELETE
  - Parameters: `key` (API key), `database` (database name)
  - Description: Deletes a database.

### Table Management:

- **Create a Table:**
  - Endpoint: `/create-table`
  - Method: POST
  - Parameters: `key` (API key), `database` (database name), `table` (table name), `attributes` (table attributes)
  - Description: Creates a new table within a database.

- **Check if a Table Exists:**
  - Endpoint: `/check-table-exists`
  - Method: GET
  - Parameters: `key` (API key), `database` (database name), `table` (table name)
  - Description: Checks if a table exists within a database.

- **Insert Data into a Table:**
  - Endpoint: `/insert-into-table`
  - Method: POST
  - Parameters: `key` (API key), `database` (database name), `table` (table name), `values` (data to insert)
  - Description: Inserts data into a table.

- **Get Data from a Table:**
  - Endpoint: `/get-table`
  - Method: GET
  - Parameters: `key` (API key), `database` (database name), `table` (table name)
  - Description: Retrieves data from a table.

- **Query a Table with Conditions:**
  - Endpoint: `/select-where`
  - Method: GET
  - Parameters: `key` (API key), `database` (database name), `table` (table name), `conditions` (query conditions)
  - Description: Queries a table with specified conditions.

- **Select Specific Columns from a Table:**
  - Endpoint: `/select-columns`
  - Method: GET
  - Parameters: `key` (API key), `database` (database name), `table` (table name), `columns` (columns to select)
  - Description: Retrieves specific columns from a table.

- **Select Specific Columns with Conditions:**
  - Endpoint: `/select-columns-where`
  - Method: GET
  - Parameters: `key` (API key), `database` (database name), `table` (table name), `columns` (columns to select), `conditions` (query conditions)
  - Description: Retrieves specific columns with specified conditions.

- **Update Records in a Table:**
  - Endpoint: `/update-table`
  - Method: POST
  - Parameters: `key` (API key), `database` (database name), `table` (table name), `conditions` (query conditions), `values` (new values)
  - Description: Updates records in a table based on specified conditions.

- **Delete Records from a Table:**
  - Endpoint: `/delete-where`
  - Method: DELETE
  - Parameters: `key` (API key), `database` (database name), `table` (table name), `conditions` (query conditions)
  - Description: Deletes records from a table based on specified conditions.

- **Delete a Table:**
  - Endpoint: `/delete-table`
  - Method: DELETE
  - Parameters: `key` (API key), `database` (database name), `table` (table name)
  - Description: Deletes a table from a database.

### Authentication:

- **Check User Authentication:**
  - Endpoint: `/check-login`
  - Method: GET
  - Parameters: `username` (username), `password` (password)
  - Description: Validates user credentials.

- **Verify User Credentials:**
  - Endpoint: `/verify/<username>/<password>`
  - Method: GET
  - Parameters: `username` (username), `password` (password)
  - Description: Verifies user credentials and returns 'True' if valid.

- **Get User API Key:**
  - Endpoint: `/getuserkey`
  - Method: GET
  - Description: Retrieves the API key for the current user.

---

## 6. Examples

Here are some

 example use cases of Menous DB API:

**Create a Database:**
```
POST /create-db
Parameters: key=<API_KEY>, database=<DATABASE_NAME>
```

**Create a Table:**
```
POST /create-table
Parameters: key=<API_KEY>, database=<DATABASE_NAME>, table=<TABLE_NAME>, attributes=<TABLE_ATTRIBUTES>
```

**Insert Data into a Table:**
```
POST /insert-into-table
Parameters: key=<API_KEY>, database=<DATABASE_NAME>, table=<TABLE_NAME>, values=<DATA_TO_INSERT>
```

**Query Data from a Table:**
```
GET /select-where
Parameters: key=<API_KEY>, database=<DATABASE_NAME>, table=<TABLE_NAME>, conditions=<QUERY_CONDITIONS>
```

**Update Records in a Table:**
```
POST /update-table
Parameters: key=<API_KEY>, database=<DATABASE_NAME>, table=<TABLE_NAME>, conditions=<QUERY_CONDITIONS>, values=<NEW_VALUES>
```

**Delete Records from a Table:**
```
DELETE /delete-where
Parameters: key=<API_KEY>, database=<DATABASE_NAME>, table=<TABLE_NAME>, conditions=<QUERY_CONDITIONS>
```

**Check User Authentication:**
```
GET /check-login
Parameters: username=<USERNAME>, password=<PASSWORD>
```

**Verify User Credentials:**
```
GET /verify/<username>/<password>
```

**Get User API Key:**
```
GET /getuserkey
```

For more examples and detailed API usage, refer to the Menous DB documentation.

---

## 7. License

Menous DB is released under the MIT Open Source Software License. You can find the full license details in the LICENSE file included with the source code.

---

## 8. Author Information

- Author: Snehashish Laskar
- Start Date: 1st November 2022
- Current Version: 0.2.1
- Contact: snehashish@example.com

For any questions, feedback, or issues, please contact the author at the provided email address.

---