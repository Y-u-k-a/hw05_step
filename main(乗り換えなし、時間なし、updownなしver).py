#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from google.appengine.api import urlfetch
import json
import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="templates/") # このディレクトリーからテンプレートを読み込む設定が含まれているオブジェクトを作る。
templateEnv = jinja2.Environment(loader=templateLoader) # テンプレートを上のtemplateLoaderを使って読み込む環境を用意する。
pataTmpl = templateEnv.get_template("pata.html") # パタトクカシーー用のテンプレートを"pata.htmlから読み込む。
networkTmpl = templateEnv.get_template("norikae6.html")  # 乗換案内用のテンプレートを"norikae.html"から読み込む。

networkJson = urlfetch.fetch("http://tokyo.fantasy-transit.appspot.com/net?format=json").content  # ウェブサイトから電車の線路情報をJSON形式でダウンロードする
network = json.loads(networkJson.decode('utf-8'))  # JSONとしてパースする（stringからdictのlistに変換する）

# このRequestHandlerでパタトカシーーのリクエストを処理して、結果を返す。

class Pata(webapp2.RequestHandler):
    def get(self):
        #パタトクカシーーになるように交互にpataに加える
        pata = ""

        difference = len(self.request.get("a"))-len(self.request.get("b"))

        if difference > 0:
            for i in range(len(self.request.get("b"))):
                pata += self.request.get("a")[i]
                pata += self.request.get("b")[i]
            pata += self.request.get("a")[-difference:]
        if difference < 0:
            for i in range(len(self.request.get("a"))):
                pata += self.request.get("a")[i]
                pata += self.request.get("b")[i]
            pata += self.request.get("b")[difference:]
        if difference == 0:
            for i in range(len(self.request.get("a"))):
                pata += self.request.get("a")[i]
                pata += self.request.get("b")[i]
        #pata = self.request.get("a") + self.request.get("b")
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        # テンプレートの内容を埋め込んで、返事を返す。
        self.response.write(pataTmpl.render(pata=pata, request=self.request))
class Norikae(webapp2.RequestHandler):
    def get(self):
        steps = {}
        pata = ""
        train_line = ""
        star_station = 0
        dest_station = 0
        up_queue = []
        down_queue = []

        for line in network:
            if self.request.get("b") in line["Stations"]:
                dest_station += line["Stations"].index(self.request.get("b"))
            if self.request.get("a") in line["Stations"]:
                star_station += line["Stations"].index(self.request.get("a"))
                train_line += line["Name"]

        pata += "Use "+train_line+" to "+self.request.get("b")+", and you can reach "+self.request.get("b")
         
                


        #pata = pata[0]
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write(networkTmpl.render(pata=pata, network=network, request=self.request))

app = webapp2.WSGIApplication([
    ('/pata', Pata),
    ('/norikae', Norikae),
], debug=True)
