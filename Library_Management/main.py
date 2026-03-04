import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import sqlite3
import csv
from datetime import datetime, timedelta

# --- PROFESSIONAL DESIGN TOKENS ---
CLR_BG = "#f8f9fa"        # Light modern grey
CLR_SIDEBAR = "#212529"   # Dark Charcoal
CLR_ACCENT = "#0d6efd"    # Bootstrap Blue
CLR_CARD = "#ffffff"      # White
CLR_TEXT = "#343a40"      # Dark text
CLR_SUCCESS = "#198754"   # Success Green
CLR_WARNING = "#ffc107"   # Warning Gold
CLR_DANGER = "#dc3545"    # Danger Red

class LibraryProUltimate:
    def __init__(self, root):
        self.root = root
        self.root.title("Internboot Library  | Enterprise Edition")
        self.root.geometry("1280x800")
        self.root.configure(bg=CLR_BG)
        
        self.user_role = None
        self.logged_in_user = None
        
        self.init_db()
        self.apply_styles()
        self.show_login()

    # ================= DATABASE & SECURITY =================
    def init_db(self):
        conn = sqlite3.connect('library_v5.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS books 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, 
             genre TEXT, status TEXT DEFAULT 'Available')''')
        c.execute('''CREATE TABLE IF NOT EXISTS users 
            (username TEXT PRIMARY KEY, password TEXT, role TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS transactions 
            (id INTEGER PRIMARY KEY, book_id INTEGER, username TEXT, 
             issue_date TEXT, due_date TEXT, return_date TEXT, fine REAL DEFAULT 0, verified INTEGER DEFAULT 0)''')
        c.execute("INSERT OR IGNORE INTO users VALUES ('admin', 'admin123', 'Admin')")
        conn.commit()
        conn.close()

    def apply_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=40, fieldbackground=CLR_CARD)
        style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"), background="#e9ecef")

    # ================= AUTHENTICATION =================
    def show_login(self):
        for w in self.root.winfo_children(): w.destroy()
        frame = tk.Frame(self.root, bg=CLR_CARD, padx=50, pady=50, highlightthickness=1, highlightbackground="#dee2e6")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="LIB-PRO LOGIN", font=("Segoe UI", 24, "bold"), fg=CLR_ACCENT, bg=CLR_CARD).pack(pady=20)
        
        tk.Label(frame, text="Username", bg=CLR_CARD, font=("Segoe UI", 10)).pack(anchor="w")
        u_ent = tk.Entry(frame, font=("Segoe UI", 12), width=30, bd=1); u_ent.pack(pady=(5, 15))
        
        tk.Label(frame, text="Password", bg=CLR_CARD, font=("Segoe UI", 10)).pack(anchor="w")
        p_ent = tk.Entry(frame, font=("Segoe UI", 12), width=30, bd=1, show="*"); p_ent.pack(pady=(5, 20))

        def do_login():
            u, p = u_ent.get(), p_ent.get()
            conn = sqlite3.connect('library_v5.db')
            res = conn.execute("SELECT role FROM users WHERE username=? AND password=?", (u, p)).fetchone()
            if res:
                self.user_role, self.logged_in_user = res[0], u
                self.show_dashboard()
            else: messagebox.showerror("Error", "Invalid Credentials")
            conn.close()

        tk.Button(frame, text="LOGIN", command=do_login, bg=CLR_ACCENT, fg="white", font=("Segoe UI", 11, "bold"), width=25, pady=8, bd=0).pack()
        tk.Button(frame, text="Create Student Account", command=self.show_register, bg=CLR_CARD, fg=CLR_ACCENT, bd=0, font=("Segoe UI", 9, "underline")).pack(pady=10)

    def show_register(self):
        win = tk.Toplevel(self.root); win.geometry("350x400"); win.title("Register")
        tk.Label(win, text="Student Registration", font=("Segoe UI", 14, "bold")).pack(pady=20)
        u_reg = tk.Entry(win, width=25); u_reg.pack(pady=5)
        p_reg = tk.Entry(win, width=25, show="*"); p_reg.pack(pady=5)
        def reg():
            conn = sqlite3.connect('library_v5.db')
            try:
                conn.execute("INSERT INTO users VALUES (?,?,'User')", (u_reg.get(), p_reg.get()))
                conn.commit(); messagebox.showinfo("Success", "Registered!"); win.destroy()
            except: messagebox.showerror("Error", "Username exists")
            finally: conn.close()
        tk.Button(win, text="Sign Up", command=reg, bg=CLR_SUCCESS, fg="white", width=15).pack(pady=20)

    # ================= DASHBOARD =================
    def show_dashboard(self):
        for w in self.root.winfo_children(): w.destroy()
        
        # Sidebar
        side = tk.Frame(self.root, bg=CLR_SIDEBAR, width=260)
        side.pack(side="left", fill="y")
        
        tk.Label(side, text="LIBRARY", font=("Impact", 24), fg=CLR_ACCENT, bg=CLR_SIDEBAR).pack(pady=30)
        tk.Label(side, text=f"Logged: {self.logged_in_user}", fg="white", bg=CLR_SIDEBAR, font=("Segoe UI", 9)).pack()

        # Nav
        nav = [("📚 Inventory", self.view_inventory), ("🤝 Issue Book", self.op_issue), ("↩️ Return Book", self.op_return)]
        if self.user_role == "Admin":
            nav.insert(1, ("➕ Add Book", self.view_add_book))
            nav.append(("✅ Confirm Returns", self.view_pending_returns))
            nav.append(("📊 Reports", self.op_report))

        for text, cmd in nav:
            tk.Button(side, text=text, command=cmd, bg=CLR_SIDEBAR, fg="white", font=("Segoe UI", 11), bd=0, anchor="w", padx=30, pady=15).pack(fill="x")

        tk.Button(side, text="Logout", command=self.show_login, bg=CLR_DANGER, fg="white").pack(side="bottom", fill="x")

        # Main Box
        self.main_area = tk.Frame(self.root, bg=CLR_BG)
        self.main_area.pack(side="right", fill="both", expand=True)
        self.view_inventory()

    # ================= CORE INTERFACE =================
    def view_inventory(self):
        self.clear_main()
        card = tk.Frame(self.main_area, bg=CLR_CARD, padx=30, pady=30, highlightthickness=1, highlightbackground="#dee2e6")
        card.pack(fill="both", expand=True, padx=40, pady=40)
        
        header = tk.Frame(card, bg=CLR_CARD)
        header.pack(fill="x", pady=(0, 20))
        tk.Label(header, text="Global Library Resources", font=("Segoe UI", 18, "bold"), bg=CLR_CARD).pack(side="left")
        
        self.s_var = tk.StringVar()
        self.s_var.trace("w", lambda *a: self.refresh_table(self.s_var.get()))
        tk.Entry(header, textvariable=self.s_var, width=30, font=("Segoe UI", 11)).pack(side="right")
        tk.Label(header, text="Search:", bg=CLR_CARD).pack(side="right", padx=5)

        cols = ("ID", "Title", "Author", "Genre", "Status")
        self.tree = ttk.Treeview(card, columns=cols, show='headings')
        for col in cols: 
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")
        self.tree.pack(fill="both", expand=True)
        self.refresh_table()

    def view_pending_returns(self):
        self.clear_main()
        tk.Label(self.main_area, text="Admin Verification Desk", font=("Segoe UI", 18, "bold"), bg=CLR_BG).pack(pady=20)
        
        cols = ("T_ID", "Book_ID", "Student", "Fine")
        self.p_tree = ttk.Treeview(self.main_area, columns=cols, show='headings')
        for c in cols: self.p_tree.heading(c, text=c); self.p_tree.column(c, anchor="center")
        self.p_tree.pack(fill="both", expand=True, padx=40)

        def confirm():
            sel = self.p_tree.selection()
            if not sel: return
            t_id, b_id = self.p_tree.item(sel)['values'][0], self.p_tree.item(sel)['values'][1]
            conn = sqlite3.connect('library_v5.db')
            conn.execute("UPDATE transactions SET verified=1 WHERE id=?", (t_id,))
            conn.execute("UPDATE books SET status='Available' WHERE id=?", (b_id,))
            conn.commit(); conn.close(); self.view_pending_returns()
            messagebox.showinfo("Verified", "Book is now back on the shelf!")

        tk.Button(self.main_area, text="APPROVE RETURN", command=confirm, bg=CLR_SUCCESS, fg="white", font=("Segoe UI", 12, "bold"), pady=10).pack(pady=20)
        
        conn = sqlite3.connect('library_v5.db')
        data = conn.execute("SELECT id, book_id, username, fine FROM transactions WHERE return_date IS NOT NULL AND verified=0").fetchall()
        for r in data: self.p_tree.insert("", "end", values=r)
        conn.close()

    # ================= OPERATIONS =================
    def op_issue(self):
        sel = self.tree.selection()
        if not sel: return
        b_id, stat = self.tree.item(sel)['values'][0], self.tree.item(sel)['values'][4]
        if stat != "Available": return messagebox.showwarning("Busy", "Book is already out.")
        
        due = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
        conn = sqlite3.connect('library_v5.db')
        conn.execute("UPDATE books SET status='Issued' WHERE id=?", (b_id,))
        conn.execute("INSERT INTO transactions (book_id, username, issue_date, due_date) VALUES (?,?,?,?)",
                     (b_id, self.logged_in_user, datetime.now().strftime("%Y-%m-%d"), due))
        conn.commit(); conn.close(); self.view_inventory()

    def op_return(self):
        sel = self.tree.selection()
        if not sel: return
        b_id, stat = self.tree.item(sel)['values'][0], self.tree.item(sel)['values'][4]
        if stat != "Issued": return
        
        conn = sqlite3.connect('library_v5.db')
        c = conn.cursor()
        c.execute("SELECT due_date, id FROM transactions WHERE book_id=? AND return_date IS NULL", (b_id,))
        res = c.fetchone()
        if res:
            due = datetime.strptime(res[0], "%Y-%m-%d")
            fine = max(0, (datetime.now() - due).days * 10)
            c.execute("UPDATE books SET status='Pending Return' WHERE id=?", (b_id,))
            c.execute("UPDATE transactions SET return_date=?, fine=? WHERE id=?", 
                      (datetime.now().strftime("%Y-%m-%d"), fine, res[1]))
            conn.commit()
            messagebox.showinfo("Process Sent", f"Book marked as returned. Admin must verify. Fine: ${fine}")
        conn.close(); self.view_inventory()

    def view_add_book(self):
        win = tk.Toplevel(self.root); win.geometry("300x400"); win.title("Add Resource")
        fields = ["Title", "Author", "Genre"]
        ents = []
        for f in fields:
            tk.Label(win, text=f).pack(pady=5)
            e = tk.Entry(win, width=30); e.pack(); ents.append(e)
        def save():
            conn = sqlite3.connect('library_v5.db')
            conn.execute("INSERT INTO books (title, author, genre) VALUES (?,?,?)", (ents[0].get(), ents[1].get(), ents[2].get()))
            conn.commit(); conn.close(); win.destroy(); self.view_inventory()
        tk.Button(win, text="Save", bg=CLR_ACCENT, fg="white", command=save).pack(pady=20)

    def op_report(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv")
        if not path: return
        conn = sqlite3.connect('library_v5.db')
        data = conn.execute("SELECT * FROM transactions").fetchall()
        with open(path, 'w', newline='') as f:
            w = csv.writer(f); w.writerow(["ID", "Book", "User", "Issue", "Due", "Return", "Fine", "Verified"]); w.writerows(data)
        conn.close(); messagebox.showinfo("Success", "Report Saved!")

    def refresh_table(self, search=""):
        for i in self.tree.get_children(): self.tree.delete(i)
        conn = sqlite3.connect('library_v5.db')
        q = "SELECT * FROM books"
        if search: q += f" WHERE title LIKE '%{search}%' OR author LIKE '%{search}%'"
        for row in conn.execute(q).fetchall():
            tag = 'red' if row[4] == 'Issued' else 'yellow' if row[4] == 'Pending Return' else 'green'
            self.tree.insert("", "end", values=row, tags=(tag,))
        self.tree.tag_configure('green', foreground=CLR_SUCCESS)
        self.tree.tag_configure('red', foreground=CLR_DANGER)
        self.tree.tag_configure('yellow', foreground=CLR_WARNING)
        conn.close()

    def clear_main(self):
        for w in self.main_area.winfo_children(): w.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryProUltimate(root) 
    root.mainloop()