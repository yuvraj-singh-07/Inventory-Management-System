from add_product import add_product
from view_product import view_product
from search_product import search_product
from update_product import update_product
from delete_product import delete_product
from line_chart import line_chart
from double_line_chart import double_line_chart
from bar_chart import bar_chart
from hbar_chart import hbar_chart
from pie_chart import pie_chart
from scatter_chart import scatter_chart
from histogram_chart import histogram_chart
from box_plot_chart import box_plot_chart
from area_chart import area_chart
from seaborn_line_chart import seaborn_line_chart
from seaborn_bar_chart import seaborn_bar_chart
from seaborn_count_plot_chart import seaborn_count_plot_chart
from seaborn_histogram_plot_chart import seaborn_histogram_plot_chart
from seaborn_box_plot_chart import seaborn_box_plot_chart
while True:
    print("="*50)
    print("="*17,"Inventory Management System","="*17)
    print("="*50)
    print("1. Add Product")
    print("2. View Product")
    print("3. Search Product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Line Chart")
    print("7. Double line Chart")
    print("8. Bar Chart")
    print("9. Hbar Chart")
    print("10. Pie Chart")
    print("11. Scatter Chart")
    print("12. Histogram chart")
    print("13. box plot chart")
    print("14. Area chart")
    print("15. Seaborn line chart")
    print("16. Seaborn Bar Chart")
    print("17. Seaborn Count Plot Chart")
    print("18. Seaborn Histogram Plot Chart")
    print("19. Seaborn Box plot chart")
    print("20. Exit")
    try:
        choice = int(input("Enter Your Choice : "))
    except ValueError:
        print("Please enter a number from 1 to 20.")
        continue
    except EOFError:
        print("\nInput ended. Exiting.")
        break
    if choice == 1:
        add_product()
    elif choice == 2:
        view_product()
    elif choice == 3:
        search_product()
    elif choice == 4:
        update_product()
    elif choice == 5:
        delete_product()
    elif choice == 6:
        line_chart()
    elif choice == 7:
        double_line_chart()
    elif choice == 8:
        bar_chart()
    elif choice == 9:
        hbar_chart()
    elif choice == 10:
        pie_chart()
    elif choice == 11:
        scatter_chart()
    elif choice == 12:
        histogram_chart()
    elif choice == 13:
        box_plot_chart()
    elif choice == 14:
        area_chart()
    elif choice == 15:
        seaborn_line_chart()
    elif choice == 16:
        seaborn_bar_chart()
    elif choice == 17:
        seaborn_count_plot_chart()
    elif choice == 18:
        seaborn_histogram_plot_chart()
    elif choice == 19:
        seaborn_box_plot_chart()
    elif choice == 20:
        print("Thank you! 😊")
        break
    else:
        print("Please choose a number from 1 to 20.")
