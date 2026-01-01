from django.shortcuts import render

def home(request):
    result = ""
    if request.method == "POST":
        try:
            num1 = float(request.POST.get("num1"))
            num2 = float(request.POST.get("num2"))
            operator = request.POST.get("operator")

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2
        except:
            result = "Invalid Input"

    return render(request, "calculator/home.html", {"result": result})
