"""
Step 1: Set Up Database Connection
- Import SQLite library
- Create cached database connection
- Initialize database table
"""

import streamlit as st
import sqlite3

st.set_page_config(page_title="Database Integration", page_icon="🗄️", layout="wide")

st.title("🗄️ Database Integration")

# STEP 1: Create cached database connection
# @st.cache_resource ensures the connection is reused, not recreated each time
@st.cache_resource
def get_connection():
    """Create and return a SQLite database connection"""
    # check_same_thread=False allows the connection to be used across threads
    conn = sqlite3.connect('app_database.db', check_same_thread=False)
    return conn

# STEP 2: Get the connection
conn = get_connection()

# STEP 3: Create table if it doesn't exist
def create_table():
    """Initialize the users table"""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER
        )
    ''')
    conn.commit()

# STEP 4: Initialize the table
create_table()

# STEP 5: Show connection status
st.success("✅ Database connected successfully!")

st.markdown("""
### Database Information

**Database Type:** SQLite
**Database File:** `app_database.db`
**Table:** `users`

#### Table Schema:
- `id` - Primary key (auto-increment)
- `name` - User name (TEXT)
- `email` - User email (TEXT)
- `age` - User age (INTEGER)

### What is CRUD?

CRUD stands for:
- **C**reate - Add new records
- **R**ead - Retrieve records
- **U**pdate - Modify existing records
- **D**elete - Remove records

In the next steps, we'll implement all CRUD operations!
""")

# STEP 6: Explain caching the connection
with st.expander("💡 Why Cache the Database Connection?"):
    st.markdown("""
    ### Caching Database Connections

    We use `@st.cache_resource` for the database connection because:

    1. **Performance**: Creating connections is expensive
    2. **Resource management**: Avoids connection pool exhaustion
    3. **Consistency**: Same connection across all operations
    4. **Best practice**: Recommended for all database connections

    ```python
    @st.cache_resource
    def get_connection():
        return sqlite3.connect('database.db')
    ```

    This ensures the connection is created once and reused!
    """)

st.divider()
st.caption("Built with Streamlit 🎈")
