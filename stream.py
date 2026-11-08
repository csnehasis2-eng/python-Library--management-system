import json
import string
import random
from pathlib import Path
from datetime import datetime

import streamlit as st
import pandas as pd


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Library Management System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# CUSTOM CSS
# ==========================================

# ==========================================
# CUSTOM CSS - READABLE LIGHT THEME
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background-color: #f4f6fb;
    color: #172033;
    font-family: 'Inter', sans-serif;
}

/* Main text */
.stApp p,
.stApp label,
.stApp span,
.stApp li,
.stApp div[data-testid="stMarkdownContainer"] {
    color: #263449;
}

/* Main headings */
h1, h2, h3, h4 {
    color: #172554 !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #111827 !important;
}

[data-testid="stSidebar"] * {
    color: #f9fafb !important;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #cbd5e1 !important;
}

/* Input fields */
.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #ffffff !important;
    color: #172033 !important;
    border: 1px solid #cbd5e1 !important;
}

/* Select boxes */
.stSelectbox div[data-baseweb="select"] {
    background-color: #ffffff !important;
}

.stSelectbox div[data-baseweb="select"] * {
    color: #172033 !important;
}

/* Dropdown menu */
[data-baseweb="popover"],
[data-baseweb="menu"] {
    background-color: #ffffff !important;
}

[data-baseweb="menu"] * {
    color: #172033 !important;
}

/* Buttons */
.stButton button,
.stFormSubmitButton button {
    background-color: #2563eb !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 9px !important;
    font-weight: 600 !important;
}

/* Cards */
.metric-card {
    background: #ffffff;
    padding: 22px;
    border-radius: 14px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 3px 12px rgba(15,23,42,0.04);
}

.metric-label {
    color: #64748b !important;
    font-size: 13px;
    font-weight: 600;
}

.metric-value {
    color: #172554 !important;
    font-size: 30px;
    font-weight: 800;
}

/* Forms */
div[data-testid="stForm"] {
    background: #ffffff !important;
    padding: 22px;
    border-radius: 14px;
    border: 1px solid #e2e8f0;
}

/* Expander */
div[data-testid="stExpander"] {
    background: #ffffff !important;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
}

div[data-testid="stExpander"] summary,
div[data-testid="stExpander"] summary p {
    color: #172033 !important;
}

/* Dataframe */
div[data-testid="stDataFrame"] {
    background: #ffffff !important;
}

/* Main title */
.main-title {
    font-size: 32px;
    font-weight: 800;
    color: #172554 !important;
}

.subtitle {
    color: #64748b !important;
    font-size: 14px;
    margin-bottom: 25px;
}

.section-title {
    color: #172554 !important;
    font-size: 21px;
    font-weight: 700;
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# LIBRARY CLASS
# ==========================================

class Library:

    database = "library.json"

    data = {
        "book": [],
        "member": []
    }

    # Load existing database
    if Path(database).exists():

        with open(database, "r", encoding="utf-8") as f:

            content = f.read().strip()

            if content:
                data = json.loads(content)

    else:

        with open(database, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)


    # Fix old database key mistakes
    for book in data.get("book", []):

        if "available_copies" not in book:
            book["available_copies"] = book.pop(
                "avaivale_copies",
                book.get("copies", 0)
            )

    for member in data.get("member", []):

        for borrowed in member.get("borrowed", []):

            if "id" not in borrowed and "id " in borrowed:
                borrowed["id"] = borrowed.pop("id ")


    @classmethod
    def save_data(cls):

        with open(cls.database, "w", encoding="utf-8") as f:

            json.dump(
                cls.data,
                f,
                indent=4,
                ensure_ascii=False
            )


    @staticmethod
    def gen_id(prefix="B"):

        while True:

            random_id = ""

            for i in range(5):
                random_id += random.choice(
                    string.ascii_uppercase + string.digits
                )

            new_id = prefix + "-" + random_id

            existing_ids = [
                item["id"]
                for item in (
                    Library.data["book"] + Library.data["member"]
                )
            ]

            if new_id not in existing_ids:
                return new_id


    # --------------------------------------
    # BOOK MANAGEMENT
    # --------------------------------------

    @classmethod
    def add_books(cls, title, author, copies):

        book = {

            "id": cls.gen_id(),

            "title": title,

            "author": author,

            "copies": copies,

            "available_copies": copies,

            "added_on": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }

        cls.data["book"].append(book)

        cls.save_data()


    @classmethod
    def get_books(cls):

        return cls.data["book"]


    # --------------------------------------
    # MEMBER MANAGEMENT
    # --------------------------------------

    @classmethod
    def add_members(cls, name, email):

        member = {

            "id": cls.gen_id("M"),

            "name": name,

            "email": email,

            "borrowed": [],

            "added_on": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }

        cls.data["member"].append(member)

        cls.save_data()


    @classmethod
    def get_members(cls):

        return cls.data["member"]


    # --------------------------------------
    # BORROW BOOK
    # --------------------------------------

    @classmethod
    def borrow_book(cls, member_id, book_id):

        member = next(
            (m for m in cls.data["member"]
             if m["id"] == member_id),
            None
        )

        book = next(
            (b for b in cls.data["book"]
             if b["id"] == book_id),
            None
        )

        if member is None:
            return False, "Member not found."

        if book is None:
            return False, "Book not found."

        if book["available_copies"] <= 0:
            return False, "No copies available."

        borrow_entry = {

            "id": book["id"],

            "title": book["title"],

            "borrowed-on": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }

        member["borrowed"].append(borrow_entry)

        book["available_copies"] -= 1

        cls.save_data()

        return True, "Book borrowed successfully!"


    # --------------------------------------
    # RETURN BOOK
    # --------------------------------------

    @classmethod
    def return_book(cls, member_id, borrow_index):

        member = next(
            (m for m in cls.data["member"]
             if m["id"] == member_id),
            None
        )

        if member is None:
            return False, "Member not found."

        if borrow_index < 0 or borrow_index >= len(member["borrowed"]):
            return False, "Invalid borrowed book."

        selected = member["borrowed"][borrow_index]

        book = next(
            (b for b in cls.data["book"]
             if b["id"] == selected["id"]),
            None
        )

        if book is None:
            return False, "Book record not found."

        member["borrowed"].pop(borrow_index)

        book["available_copies"] += 1

        cls.save_data()

        return True, "Book returned successfully!"


# ==========================================
# DASHBOARD DATA
# ==========================================

books = Library.get_books()
members = Library.get_members()

total_books = sum(b["copies"] for b in books)

available_books = sum(
    b["available_copies"] for b in books
)

borrowed_books = sum(
    len(m["borrowed"]) for m in members
)

total_members = len(members)


# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

with st.sidebar:

    st.markdown("# 📚 BookSpace")

    st.caption("LIBRARY MANAGEMENT")

    st.divider()

    page = st.radio(

        "NAVIGATION",

        [
            "Dashboard",
            "Manage Books",
            "Manage Members",
            "Borrow Books",
            "Return Books"
        ],

        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("### 📖 BookSpace")

    st.caption("Smart Library Management")

    st.caption("Built with Python & Streamlit")


# ==========================================
# DASHBOARD
# ==========================================

if page == "Dashboard":

    st.markdown(
        '<div class="main-title">Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Welcome back! Here is your library overview.</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    metrics = [

        (col1, "📚", "Total Books", total_books),

        (col2, "👥", "Total Members", total_members),

        (col3, "✅", "Available Copies", available_books),

        (col4, "📖", "Borrowed Books", borrowed_books)

    ]

    for col, icon, label, value in metrics:

        with col:

            st.markdown(f"""
            <div class="metric-card">

                <div class="metric-icon">{icon}</div>

                <div class="metric-label">{label}</div>

                <div class="metric-value">{value}</div>

            </div>
            """, unsafe_allow_html=True)


    st.markdown(
        '<div class="section-title">Recent Books</div>',
        unsafe_allow_html=True
    )

    if books:

        recent = books[-5:][::-1]

        df = pd.DataFrame(recent)

        df = df[
            ["id", "title", "author", "copies", "available_copies"]
        ]

        df.columns = [
            "Book ID",
            "Title",
            "Author",
            "Total Copies",
            "Available Copies"
        ]

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("No books available. Add your first book!")

    st.markdown(
        '<div class="section-title">Library Statistics</div>',
        unsafe_allow_html=True
    )

    if books:

        chart_data = pd.DataFrame({

            "Book": [b["title"] for b in books],

            "Available": [
                b["available_copies"] for b in books
            ],

            "Borrowed": [
                b["copies"] - b["available_copies"]
                for b in books
            ]

        })

        st.bar_chart(
            chart_data.set_index("Book"),
            use_container_width=True
        )


# ==========================================
# MANAGE BOOKS
# ==========================================

elif page == "Manage Books":

    st.markdown(
        '<div class="main-title">Manage Books</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Add and explore your library collection.</div>',
        unsafe_allow_html=True
    )

    with st.expander("➕ Add a New Book", expanded=True):

        with st.form("add_book_form"):

            title = st.text_input("Book Title")

            author = st.text_input("Author Name")

            copies = st.number_input(
                "Number of Copies",
                min_value=1,
                step=1
            )

            submitted = st.form_submit_button(
                "Add Book",
                type="primary",
                use_container_width=True
            )

            if submitted:

                if not title.strip() or not author.strip():

                    st.error("Please fill all the fields.")

                else:

                    Library.add_books(
                        title.strip(),
                        author.strip(),
                        int(copies)
                    )

                    st.success("Book added successfully!")


    st.markdown("### 📚 Book Collection")

    search = st.text_input(
        "🔍 Search books",
        placeholder="Search by title, author or book ID..."
    )

    filtered_books = [

        b for b in Library.get_books()

        if search.lower() in (
            b["title"] + b["author"] + b["id"]
        ).lower()

    ]

    if filtered_books:

        df = pd.DataFrame(filtered_books)

        df = df[
            ["id", "title", "author", "copies", "available_copies"]
        ]

        df.columns = [
            "Book ID",
            "Title",
            "Author",
            "Total Copies",
            "Available Copies"
        ]

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("No matching books found.")


# ==========================================
# MANAGE MEMBERS
# ==========================================

elif page == "Manage Members":

    st.markdown(
        '<div class="main-title">Manage Members</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Register and manage library members.</div>',
        unsafe_allow_html=True
    )

    with st.expander("➕ Register New Member", expanded=True):

        with st.form("add_member_form"):

            name = st.text_input("Full Name")

            email = st.text_input("Email Address")

            submitted = st.form_submit_button(
                "Register Member",
                type="primary",
                use_container_width=True
            )

            if submitted:

                if not name.strip() or not email.strip():

                    st.error("Please fill all the fields.")

                elif "@" not in email or "." not in email:

                    st.error("Please enter a valid email address.")

                else:

                    Library.add_members(
                        name.strip(),
                        email.strip()
                    )

                    st.success("Member registered successfully!")


    st.markdown("### 👥 Registered Members")

    if Library.get_members():

        for member in Library.get_members():

            with st.expander(
                f"👤 {member['name']}  |  {member['id']}"
            ):

                st.write("**Email:**", member["email"])

                st.write(
                    "**Borrowed Books:**",
                    len(member["borrowed"])
                )

                if member["borrowed"]:

                    for book in member["borrowed"]:

                        st.write(
                            f"📖 {book['title']} ({book['id']})"
                        )

                else:

                    st.caption("No books borrowed currently.")

    else:

        st.info("No members registered yet.")


# ==========================================
# BORROW BOOKS
# ==========================================

elif page == "Borrow Books":

    st.markdown(
        '<div class="main-title">Borrow Books</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Issue books to registered library members.</div>',
        unsafe_allow_html=True
    )

    available = [
        b for b in Library.get_books()
        if b["available_copies"] > 0
    ]

    all_members = Library.get_members()

    if not all_members:

        st.warning("Please register a member first.")

    elif not available:

        st.warning("No books are currently available.")

    else:

        member_map = {
            m["id"]: m for m in all_members
        }

        book_map = {
            b["id"]: b for b in available
        }

        with st.form("borrow_form"):

            member_id = st.selectbox(
                "Select Member",
                list(member_map.keys()),
                format_func=lambda x: (
                    f"{member_map[x]['name']} ({x})"
                )
            )

            book_id = st.selectbox(
                "Select Book",
                list(book_map.keys()),
                format_func=lambda x: (
                    f"{book_map[x]['title']} | "
                    f"Available: {book_map[x]['available_copies']}"
                )
            )

            submitted = st.form_submit_button(
                "📖 Borrow Book",
                type="primary",
                use_container_width=True
            )

            if submitted:

                success, message = Library.borrow_book(
                    member_id,
                    book_id
                )

                if success:
                    st.success(message)
                else:
                    st.error(message)


# ==========================================
# RETURN BOOKS
# ==========================================

elif page == "Return Books":

    st.markdown(
        '<div class="main-title">Return Books</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Manage borrowed books and update inventory.</div>',
        unsafe_allow_html=True
    )

    members = Library.get_members()

    member_map = {
        m["id"]: m for m in members
    }

    if not members:

        st.warning("No members registered.")

    else:

        member_id = st.selectbox(
            "Select Member",
            list(member_map.keys()),
            format_func=lambda x: (
                f"{member_map[x]['name']} ({x})"
            )
        )

        selected_member = member_map[member_id]

        borrowed = selected_member["borrowed"]

        if not borrowed:

            st.info("This member has no borrowed books.")

        else:

            st.markdown("### 📚 Currently Borrowed Books")

            book_map = {
                i: b for i, b in enumerate(borrowed)
            }

            with st.form("return_form"):

                borrow_index = st.selectbox(
                    "Select Book to Return",
                    list(book_map.keys()),
                    format_func=lambda x: (
                        f"{book_map[x]['title']} "
                        f"({book_map[x]['id']})"
                    )
                )

                submitted = st.form_submit_button(
                    "↩️ Return Book",
                    type="primary",
                    use_container_width=True
                )

                if submitted:

                    success, message = Library.return_book(
                        member_id,
                        borrow_index
                    )

                    if success:
                        st.success(message)
                    else:
                        st.error(message)


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.markdown(
    "<center style='color:#64748b;'>"
    "📚 BookSpace | Built with Python & Streamlit"
    "</center>",
    unsafe_allow_html=True
)
