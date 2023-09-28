def linear_search_product(Productlist,tar):
  indices=[]
  for index, Product in enumerate(Productlist):
    if Product==tar:
      indices.append(index)

  return indices

Product=["rice","nuts","dals","nuts","fruits","vegetable"]
target="nuts"
result=linear_search_product(Product,target)
print(result)
