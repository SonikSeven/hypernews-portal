from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings

import json
import datetime


def load_json():
    with open(settings.NEWS_JSON_PATH) as json_file:
        return json.load(json_file)


class MainView(View):
    def get(self, request):
        news_list = sorted(load_json(), key=lambda x: x["created"], reverse=True)
        if query := request.GET.get("q"):
            news_list = [article for article in news_list if query.lower() in article["title"].lower()]
        context = {"news_list": news_list}
        return render(request, "main.html", context)


class ArticleView(View):
    def get(self, request, article_number):
        for list_item in load_json():
            if list_item["link"] == int(article_number):
                context = {"article": list_item}
                return render(request, "article.html", context)
        return redirect("main_url")


class AddArticleView(View):
    def get(self, request):
        return render(request, "add_article.html")

    def post(self, request):
        title = request.POST.get("title")
        text = request.POST.get("text")
        news_list = load_json()
        new_article = {"created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                       "text": text,
                       "title": title,
                       "link": len(news_list)}
        news_list.append(new_article)
        with open(settings.NEWS_JSON_PATH, "w") as json_file:
            json.dump(news_list, json_file)
        return redirect("main_url")
