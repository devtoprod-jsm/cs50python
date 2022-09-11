name = input("What's your name? ").upper()

match name:
  case "Jai" | "Jaisrith" | "JAI" | "JAISRITH" : 
    print("It's Jaisrith Tella")
  case "Sindhu" | "Sindhu sri" :
    print("It's wify")
  case _ :
    print("Who???")