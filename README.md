# hw05_step
🦔6/24　22:00 乗り換え案内について

分かってること
少なくとも出発と到着を入力しなければならないので、norikae.htmlを変更する必要がある
幅優先探索っぽい

分からないこと
Krisさんのはプルダウン式になってるけどどうしたらいいのか
違う線に乗り換えられない
答えが出力できない
どういうアルゴリズムを使えば良いのか分からない



→結論
とりあえず同じ線、隣の駅で良いから駅を入力すればなんらかの出力ができるようにする
目標：6/24 23:00まで


🦔6/24　23:20 乗り換え案内について
目標は無理

分かったこと
network以外にrequest=self.requestも要りそう
localで確認する方がはるかに便利
network以外にrequestとか入れると上手くいかなくなる
多分パタトクカシーーの書式に似てる気がする(入力するところにおいて)

分からないこと
Krisさんのはプルダウン式になってるけどどうしたらいいのか
違う線に乗り換えられない
答えが出力できない
どういうアルゴリズムを使えば良いのか分からない



→結論
とりあえずnetwork羅列以外で何か出力を成功させる
(出来るだけパタトクカシーーのコード、テンプレートに寄せて上手くいかないか試してみる)
(今はlocal hostで動かせないので一回一回確認するのに時間がかかるから集中して丁寧にやる)
目標：6/25 0:00まで


🦔6/25　0:20 乗り換え案内について
パタトクカシーーのテンプレを使ったらできた

分かったこと
私が今上手くいかないのはテンプレートの作り方が間違っているせい

→結論
テンプレートの作り方のどこが間違ってるのかけんいちさんに教えてもらう(1:30　解決)
それとjinja２をいくら調べても使い方が分からない問題をそのままにしていたけどおそらくそれが原因

とりあえずはパタトクカシーーのテンプレートを使って乗り換え案内を作る
a+bのところに出力させることができるはず


🦔6/25　1:30 乗り換え案内について
テンプレートは分かった(まだ選択肢にはできない)

今度はnetworkの読み方?が分からない


🦔6/25　2:00 乗り換え案内について
networkを読もうとテンプレにif構文とか使い出したらerrorでてきた
networkとテンプレが両立できない

