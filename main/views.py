from django.shortcuts import render
# from django.http import HttpResponse

# 関数ベースビュー
# ビュー関数
def index (request):
    question_list = [
        "生きている意味は何ですか",
        "お前の住所は何ですか",
        "銀行口座の番号は何ですか",
    ]
    context = {
        "question_list": question_list,
        "is_polled": True,
        "polled_msg": "(￣ー￣)((´∀｀))ｹﾗｹﾗ",
        "not_polled_msg":"(* ´艸｀)ｸｽｸｽ",
        "user-name":"hello"
    }
    return render(request, "main/index.html",context,)

from  .models import Question

def index(request):
    all_question = Question.objects.all()
    context = {
        "all_question":all_question
    }

    return render(request,"main/index.html",context)