from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# 로그인을 위한 모듈 추출
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import datetime

# pymongo 사용 모듈 추출
import pymongo
import traceback
import json
# log
import logging

# 2020-08-09 추가한 것 condition_exp(request)
# 여기에서 조건식 받는 형태를 정리해서 데이터베이스에 저장해야한다.
# for문으로 중복해서 저장할 수 있게 해야한다.

def search(request):

    indicator_dic ={}
    #for i,indi in enumerate(indicators):
    for i in range(1,4):
        # 받기
        indi_index = "indicator"+str(i)
        indi_min = "indicator_min"+str(i)
        indi_max = "indicator_max"+str(i)
        indicator_dic[indi_index] = request.POST[indi_index]
        indicator_dic[indi_min] = request.POST[indi_min]
        indicator_dic[indi_max] = request.POST[indi_max]
        print(indi_index+" : "+indicator_dic[indi_index])
        print(indi_min +" : "+indicator_dic[indi_min])
        print(indi_max+" : "+indicator_dic[indi_max])

    # pymongo 연결
    client = pymongo.MongoClient("mongodb+srv://user1:start3we@cluster0.mqlrz.mongodb.net/<TEST2>?retryWrites=true&w=majority")
    db = client.pj_sgm ## db name 
    print('MongoDB Connected.')

    #line=json.loads()
    # find()하면 리스트 형식으로 가져옴
    # sort하면 시총순으로 가져온다. ,indicator_dic[indicator2]:{"$gte":int(indicator_dic[indicator_min2]), "$lte": int(indicator_dic[indicator_max2])},indicator_dic[indicator3]:{"$gte":int(indicator_dic[indicator_min3]), "$lte": int(indicator_dic[indicator_max3])}}
    for doc in db.platform2.find({ "$and":[{indicator_dic["indicator1"] : { "$gte" : int(indicator_dic["indicator_min1"] ), "$lte": int(indicator_dic["indicator_max1"])}},{indicator_dic["indicator2"] : { "$gte" : int(indicator_dic["indicator_min2"] ), "$lte": int(indicator_dic["indicator_max2"])}},{indicator_dic["indicator3"] : { "$gte" : int(indicator_dic["indicator_min3"] ), "$lte": int(indicator_dic["indicator_max3"])}}]}).sort([("Market_cap",-1)]):
        print(doc)
    print("0=======================================")
    '''
    for doc in db.platform.find({indicator:{"$gte":indicator_min, "$lte":indicator_max}}):
        print(doc)
    print("1=======================================")
    '''
    '''

    #print(db.platform.find({"code":"005930"}))
    # code가 005930인것 중에 PER의 2019 정보가 2018 보다 크거나 같은 데이터 가져오기
    for doc in db.platform.find({"code":"005930","PER.2019":{"$gte":"2018"}}):
        print(doc)
    print("2=======================================")
    # sort사용 
    #cursor.sort(document)
    # document= {key:value}   key는 field이름 , value : 1이면 오름차순 -1이면 내림차순

    for doc in db.platform.find({"code":"005930","PER.2019":{"$gte":"2018", "$lte":"2020"}}).sort([("EPS.2016",1)]):
        print(doc)


    print("3=======================================")
    #출력할 조절 개수 3개
    for doc in db.platform.find().limit(3):
        print(doc)

    #change_category = Category.objects.get(id = change_category_id)
    #new_res = Restaurant(category = category, restaurant_name = name, restaurant_link = link, restaurant_content = content, restaurant_keyword = keyword)
    #new_res.save()
    '''
    return render(request, 'input_data/crawling.html')

# 요청을 받으면 파일 열어서 저장하는 형식
def index(request):
    return render(request, 'input_data/index.html')

def crawling_index(request):
    return render(request, 'input_data/crawling.html')

def save_data(request):
    try:
        client = pymongo.MongoClient("mongodb+srv://user1:start3we@cluster0.mqlrz.mongodb.net/<TEST1>?retryWrites=true&w=majority")
        db = client.TEST1 ## db name 
        print('MongoDB Connected.')

        inputfile="./json_file/test1.json"
        
        f = open(inputfile, 'r',encoding='UTF8')
        lines = f.readlines()
        for line in lines:  
            line=json.loads(line)
            db.platform2.insert_one(line)

    except Exception as e:
        print(traceback.format_exc())
    finally:
        client.close()
    #return HttpResponseRedirect(reverse('save_data'))
    return render(request, 'input_data/crawling.html')
