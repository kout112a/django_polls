from django.shortcuts import render
from django.http import HttpResponse

# 関数ベースビュー
# ビュー関数
def index (request):
    return HttpResponse("時間と金がほしいわ")