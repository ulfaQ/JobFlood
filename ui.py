from tkinter import *
from jobmanager import JM

class Main:

    def __init__(self):
        """ Create main window and add buttons to menu on the left """

        ## ***** Create main window with menu *****
        self.main = Tk()
        self.main.geometry("600x600")
        self.menu = Frame(self.main)
        self.menu.grid(column=0, row=0, sticky=NW)

        ## ***** Create Buttons *****
        self.view_all_b = Button(self.menu, text="View All", fg="black")
        self.view_acc_b = Button(self.menu, text="View Acceccible", fg="black")
        self.view_wait_b = Button(self.menu, text="View Waiting", fg="black")
        self.view_hist_b = Button(self.menu, text="View History", fg="black")
        self.add_new_b = Button(self.menu, text="Add New Job", fg="black")

        ## ***** Grid container and menu *****
        self.menu.grid(column=0, row=0, sticky=NW)

        ## ***** Grid Buttons *****
        self.view_all_b.grid(row=1, sticky=NW)
        self.view_acc_b.grid(row=2, sticky=NW)
        self.view_wait_b.grid(row=3, sticky=NW)
        self.view_hist_b.grid(row=4, sticky=NW)
        self.add_new_b.grid(row=5, sticky=NW)

        ## ***** Button Bindings *****
        self.view_all_b.bind("<Button-1>") # add ", behavior" inside 
        self.view_acc_b.bind("<Button-1>")
        self.view_wait_b.bind("<Button-1>")
        self.view_hist_b.bind("<Button-1>")
        self.add_new_b.bind("<Button-1>", self.show_job_frame)

        ## ***** Mainloop *****
        self.main.mainloop()

    def show_job_frame(self, filler):

        # These values are going to be sent to jobmanager,
        # after they are filled with relevant info.

        ######
        ## I'm defining a class to hold these variables because when I declare them normally,
        ## I can't access them inside functions even with using global???
        ## I need to learn something about variable scoping, because this happens relatively often.
        ## I can't understand why the objects is acceccible inside functions and variables aren't.
        ## I'm apparently missing something profound here.
        ######

        class TempCustomer:
            def __init__(self):
                self.prod_num = 0
                self.all_products = {}
                self.cust_num = 0
                self.customer = None

        current_customer = TempCustomer()

        def commit_job():
            """ This collects all the information concerning the job in one dictionary, and sends it forward
            This should send it so that the job gets into the all_jobs dict in jobmanager.
            """
            JM.job_list.update({ 
                current_customer.cust_num : {
                    "customer" : str(self.customer_e.get()),
                    "products" : current_customer.all_products
                    }
                })
            current_customer.cust_num += 1
            print(" Job sended to JM, current_customer.cust_num = {}, and JM.job_list = {}".format(
                current_customer.cust_num, JM.job_list))

        def show_product_window():
            """ This opens the window where are the fields for the product's information """

            def add_product():
                """ This adds a product to all products for this customer """

                current_customer.all_products.update({

                    # TODO: add other information conserning the product to this dictionary below

                    current_customer.prod_num : { str(product_entry.get()) : str(amount_entry.get()) }
                    })

                current_customer.prod_num += 1
                print(" Adding product to this customers all_products dictionary ********************")
                print(current_customer.all_products)

            ## ***** Make a new window for products entry *****
            product_window = Tk()

            ## ***** Product field *****
            Label(product_window, text="Product: ").pack(side=LEFT)
            product_entry = Entry(product_window)
            product_entry.pack(side=LEFT)

            ## ***** Amount field *****
            Label(product_window, text="Amount: ").pack(side=LEFT)
            amount_entry = Entry(product_window)
            amount_entry.pack(side=LEFT)

            ## ***** Commit button *****
            Button(product_window, text="Add job", command=add_product).pack()

            ## ***** Mainloop *****
            product_window.mainloop()

        Label(self.main, text="Add new job").grid(column=1, row=0)
        Label(self.main, text="Customer: ").grid(column=1, row=1)
        self.customer_e = Entry(self.main)
        self.customer_e.grid(column=2, row=1)
        Button(self.main, text="Add Product: ", command=show_product_window).grid(column=1, row=3)
        Button(self.main, text="Commit Job", command=commit_job).grid(column=1, row=4)

if __name__ == "__main__":
    mainWindow = Main()
