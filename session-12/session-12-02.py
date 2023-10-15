import pandas as pd
def selling_zara_results() :
    print("Hello! This program shows the selling results at Zara in September.")
    print("For more information, please follow the instructions and answer the questions.")
    print("Thank you :)")

    articles = []
    prices = []

    grades = {'A': [], 'B': [], 'C': [], 'D': [], 'E': []}

    f = open("zara.csv", "r")
    txt_a=""
    for line in f:
        txt_a+=line
        
    words=txt_a.strip.split()
    for i in words:
        articles.append(article)
        prices.append(price)

    for i in range(len(articles)):
        article = articles[i]
        price = prices[i]

        if price >= 20000:
            grades['A'].append((article, price))
        elif 15000 <= price < 20000:
            grades['B'].append((article, price))
        elif 10000 <= price < 15000:
            grades['C'].append((article, price))
        elif 5000 <= price < 10000:
            grades['D'].append((article, price))
        elif price < 5000:
            grades['E'].append((article, price))

    # Create a list of dictionaries to the data
    data = []

    # extract the article and price
    for grade, items in grades.items():
        for item in items:
            article, price = item
            data.append({'Grade': grade, 'Article': article, 'Price': price})


    df = pd.DataFrame(data)
    print(df)

selling_zara_results()