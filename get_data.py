def get_data(days):
    dates = ["2022-25-10","2022-26-10", "2022-27-10"]
    temperatures = [10, 15, 18]
    temperatures = [days * i for i  in temperatures ]
    return dates, temperatures