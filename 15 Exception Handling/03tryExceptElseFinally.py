def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        # Runs only if no exception occurred
        print("Division successful. Result =", result)
    finally:
        # Always runs, no matter what
        print("Execution complete.")

# Example calls
divide(10, 2)   # No exception → else + finally
divide(10, 0)   # Exception → except + finally
