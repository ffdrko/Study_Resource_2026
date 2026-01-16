country = input("Enter your country: ")

match country.lower():
    case "usa" | "uk" | "canada":
        print("You are from an English-speaking country.")
    case "spain" | "mexico" | "argentina":
        print("You are from a Spanish-speaking country.")
    case "france" | "belgium" | "switzerland":
        print("You are from a French-speaking country.")