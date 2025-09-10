import sqlite3
from contextlib import closing
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

DB_PATH = "inventory.db"

# ========== Database Layer ==========
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with closing(get_conn()) as conn:
        cur = conn.cursor()
        cur.executescript("""
        CREATE TABLE IF NOT EXISTS products (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          code TEXT UNIQUE NOT NULL,
          name TEXT NOT NULL,
          category TEXT,
          cost REAL NOT NULL DEFAULT 0,
          price REAL NOT NULL DEFAULT 0,
          stock INTEGER NOT NULL DEFAULT 0,
          supplier TEXT,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS sales (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          invoice_no TEXT UNIQUE,
          sale_date DATETIME DEFAULT CURRENT_TIMESTAMP,
          total_amount REAL NOT NULL,
          paid_amount REAL NOT NULL,
          cashier TEXT
        );

        CREATE TABLE IF NOT EXISTS sale_items (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          sale_id INTEGER NOT NULL,
          product_id INTEGER NOT NULL,
          quantity INTEGER NOT NULL,
          selling_price REAL NOT NULL,
          subtotal REAL NOT NULL,
          FOREIGN KEY (sale_id) REFERENCES sales(id),
          FOREIGN KEY (product_id) REFERENCES products(id)
        );
        """)
        conn.commit()

def add_product(code, name, category, cost, price, stock, supplier=None):
    with closing(get_conn()) as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO products (code,name,category,cost,price,stock,supplier) VALUES (?,?,?,?,?,?,?)",
            (code, name, category, cost, price, stock, supplier)
        )
        conn.commit()
        return cur.lastrowid

def update_product(prod_id, **fields):
    if not fields:
        return
    cols = ", ".join(f"{k}=?" for k in fields.keys())
    vals = list(fields.values()) + [prod_id]
    with closing(get_conn()) as conn:
        conn.execute(f"UPDATE products SET {cols} WHERE id = ?", vals)
        conn.commit()

def delete_product(prod_id):
    with closing(get_conn()) as conn:
        conn.execute("DELETE FROM products WHERE id = ?", (prod_id,))
        conn.commit()

def get_product(prod_id):
    with closing(get_conn()) as conn:
        cur = conn.execute("SELECT * FROM products WHERE id = ?", (prod_id,))
        return cur.fetchone()

def list_products(limit=100):
    with closing(get_conn()) as conn:
        cur = conn.execute("SELECT * FROM products ORDER BY name LIMIT ?", (limit,))
        return cur.fetchall()

def create_sale(invoice_no, items, paid_amount, cashier=None):
    total = sum(i['quantity'] * i['selling_price'] for i in items)
    with closing(get_conn()) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO sales (invoice_no,total_amount,paid_amount,cashier) VALUES (?,?,?,?)",
                    (invoice_no, total, paid_amount, cashier))
        sale_id = cur.lastrowid
        for it in items:
            subtotal = it['quantity'] * it['selling_price']
            cur.execute(
                "INSERT INTO sale_items (sale_id,product_id,quantity,selling_price,subtotal) VALUES (?,?,?,?,?)",
                (sale_id, it['product_id'], it['quantity'], it['selling_price'], subtotal)
            )
            cur.execute("UPDATE products SET stock = stock - ? WHERE id = ?", (it['quantity'], it['product_id']))
        conn.commit()
        return sale_id

# ========== Tkinter UI Layer ==========
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inventory Manager - Single File")
        self.geometry("800x500")

        top = ttk.Frame(self)
        top.pack(fill="x", padx=8, pady=8)

        ttk.Button(top, text="Add Product", command=self.add_product_dialog).pack(side="left")
        ttk.Button(top, text="Make Sale", command=self.make_sale_dialog).pack(side="left", padx=8)
        ttk.Button(top, text="Refresh", command=self.load_products).pack(side="left")

        self.tree = ttk.Treeview(self, columns=("id","code","name","price","stock"), show="headings")
        for col, w in [("id",40),("code",100),("name",300),("price",80),("stock",80)]:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=w, anchor="w")
        self.tree.pack(fill="both", expand=True, padx=8, pady=8)

        self.load_products()

    def load_products(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for p in list_products(1000):
            self.tree.insert("", "end", values=(p["id"], p["code"], p["name"], p["price"], p["stock"]))

    def add_product_dialog(self):
        dlg = AddProductDialog(self)
        self.wait_window(dlg)
        if getattr(dlg, "saved", False):
            self.load_products()

    def make_sale_dialog(self):
        pid = simpledialog.askinteger("Product ID", "Enter product ID:")
        if not pid:
            return
        prod = get_product(pid)
        if not prod:
            messagebox.showerror("Error", "Product not found")
            return
        qty = simpledialog.askinteger("Quantity", f"Enter quantity (available {prod['stock']}):", minvalue=1)
        if not qty:
            return
        if qty > prod['stock']:
            messagebox.showerror("Error", "Not enough stock")
            return
        price = prod['price']
        invoice = f"INV{prod['id']}{int(__import__('time').time())}"
        sale_id = create_sale(invoice, [{'product_id': pid, 'quantity': qty, 'selling_price': price}], paid_amount=price*qty, cashier="cashier1")
        messagebox.showinfo("Sale recorded", f"Sale id {sale_id} | total {price*qty}")
        self.load_products()

class AddProductDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add Product")
        self.transient(parent)
        self.resizable(False, False)
        frm = ttk.Frame(self, padding=10)
        frm.pack(fill="both", expand=True)
        labels = ["Code","Name","Category","Cost","Price","Stock","Supplier"]
        self.vars = {}
        for i,lab in enumerate(labels):
            ttk.Label(frm, text=lab).grid(row=i, column=0, sticky="w", pady=4)
            v = tk.StringVar()
            ttk.Entry(frm, textvariable=v, width=40).grid(row=i, column=1, pady=4)
            self.vars[lab.lower()] = v

        ttk.Button(frm, text="Save", command=self.save).grid(row=len(labels), column=0, columnspan=2, pady=8)

    def save(self):
        try:
            code = self.vars['code'].get().strip()
            name = self.vars['name'].get().strip()
            category = self.vars['category'].get().strip()
            cost = float(self.vars['cost'].get() or 0)
            price = float(self.vars['price'].get() or 0)
            stock = int(self.vars['stock'].get() or 0)
            supplier = self.vars['supplier'].get().strip() or None
            if not code or not name:
                raise ValueError("Code and Name required")
            add_product(code, name, category, cost, price, stock, supplier)
            self.saved = True
            self.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

# ========== Main ==========
if __name__ == "__main__":
    init_db()
    app = App()
    app.mainloop()
