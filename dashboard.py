import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data

# add purple color to the board

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"])

# Chart 1: Bar chart of sales data

def create_sales_chart():
    fig, ax = plt.subplots()
    ax.bar(sales_data.keys(), sales_data.values())
    ax.set_title("Sales by Product")
    ax.set_xlabel("Product")
    ax.set_ylabel("Sales")
    return fig

# Chart 2 : Horizontal bar chart of inventory data
def create_inventory_chart():
    fig, ax = plt.subplots()
    ax.barh(list(inventory_data.keys()), inventory_data.values())
    ax.set_title("Inventory by Product")
    ax.set_xlabel("Inventory")
    ax.set_ylabel("Product")
    return fig

# Chart 3: Pie chart of product data
def create_product_pie_chart():
    fig, ax = plt.subplots()
    ax.pie(product_data.values(), labels=product_data.keys(), autopct='%1.1f%%')
    ax.set_title("Product Breakdown")
    return fig

# Chart 4: Line chart of sales by year
def create_sales_year_chart():
    fig, ax = plt.subplots()
    ax.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
    ax.set_title("Sales by Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sales")
    return fig

# Chart 5: Area chart of inventory by month
def create_inventory_month_chart():
    fig, ax = plt.subplots()
    ax.fill_between(inventory_month_data.keys(), inventory_month_data.values())
    ax.set_title("Inventory by Month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Inventory")
    return fig

#create a function that stops the Tkinter event loop
def stop_event_loop(event, root):
    root.quit()

# Create a window and add charts
def create_dashboard():
    root = tk.Tk()
    # Charts will maximize and take up the whole screen
    root.title("Dashboard")
    root.state('zoomed')
    root.bind('<Destroy>', lambda event: stop_event_loop(event, root))
    

    side_frame = tk.Frame(root, bg="#4C2A85")
    side_frame.pack(side="left", fill="y")

    label = tk.Label(side_frame, text="Dashboard", bg="#4C2A85", fg="#FFF", font=25)
    label.pack(pady=50, padx=20)

	# create a chart frame
    chart_frame = tk.Frame(root)
    chart_frame.pack()

	# upper frame contains 3 charts
    upper_frame = tk.Frame(chart_frame)
    upper_frame.pack(fill="both", expand=True)

    canvas1 = FigureCanvasTkAgg(create_sales_chart(), upper_frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

    canvas2 = FigureCanvasTkAgg(create_inventory_chart(), upper_frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

    canvas3 = FigureCanvasTkAgg(create_product_pie_chart(), upper_frame)
    canvas3.draw()
    canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)

	# create lower frame to include others charts
    lower_frame = tk.Frame(chart_frame)
    lower_frame.pack(fill="both", expand=True)

    canvas4 = FigureCanvasTkAgg(create_sales_year_chart(), lower_frame)
    canvas4.draw()
    canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)

    canvas5 = FigureCanvasTkAgg(create_inventory_month_chart(), lower_frame)
    canvas5.draw()
    canvas5.get_tk_widget().pack(side="left", fill="both", expand=True)

    root.mainloop()


# Call the create_dashboard function to start the program
create_dashboard()
