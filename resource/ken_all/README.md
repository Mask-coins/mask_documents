日本郵政グループの公開する  
「郵便番号データダウンロード」  
https://www.post.japanpost.jp/zipcode/download.html  
を RDF の形式に変換しました．

Ontology は  
- https://github.com/Mask-coins/mask_documents/blob/master/ontology/mo.ttl
- https://github.com/Mask-coins/mask_documents/blob/master/ontology/geo_jp.ttl

にあります．

試作品につき，今後大幅な変更がありうることをご承知おきください．


### 未解決の問題

- 大字・小字・特殊な中字等の区別はつけていません．
- 建物名などの不適切なエンティティが存在するかもしれません．
- 同じ自治体内に同じ町名がある場合は区別できていません．
  - 特に京都の同名町名，大字と住居表示が同じ名前であるとき．

