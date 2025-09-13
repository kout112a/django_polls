from django.shortcuts import render
# from django.http import HttpResponse

# 関数ベースビュー
# ビュー関数
def index (request):
    question_list = [
        "生きている意味は何だ",
        "お前の住所は何だ",
        "銀行口座の番号は何だ",
    ]
    context = {
        "question_list": question_list,
        "is_polled": True,
        "polled_msg": "(￣ー￣)((´∀｀))ｹﾗｹﾗ",
        "not_polled_msg":"(* ´艸｀)ｸｽｸｽ",
        "user-name":"hello"
    }
    return render(request, "main/index.html",context,)