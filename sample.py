import pandas as pd 
information=pd.read_csv("source.csv")
# print(len(information))

# def title():
#     for i in information["title"]:
#         print(i)
# title()

# def title():
#     for i in information["smdName"]:
#         print(i)
# title()

# def title():
#     for i in information["organizationName"]:
#         print(i)
# title()

# def title():
#     for i in information["sourceType"]:
#         print(i)
# title()


# def title():
#     for i in information["sourceUrl"]:
#         print(i)
# title()

# def lang():
#     for i in information["icarUrl"]:
#         print(i)
# lang()

# def lang():
#     for i in information["keywords"]:
#         print(i)
# lang()

def lang():
    for i in information["language"]:
        print(i)
lang()