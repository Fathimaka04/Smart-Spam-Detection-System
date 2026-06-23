from django.shortcuts import render
import pickle

model=pickle.load(open("spam_model.pkl","rb"))
vectorizer=pickle.load(open("vectorizer.pkl","rb"))

def home(request):
    result=""
    if request.method=="POST":
        message=request.POST.get("message")
        msg_vector=vectorizer.transform([message])
        prediction=model.predict(msg_vector)
        result=prediction[0]

    return render(request,"index.html",{"result":result})
