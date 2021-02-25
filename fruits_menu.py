import unicodedata

### 引数textの全角文字数カウント
def get_zen_count(text):
	count=0
	for c in text:
		if unicodedata.east_asian_width(c) in "FWA":
			count +=1
	return count


### 商品クラス
class Item:
	def __init__(self,item_code,item_name,price):
		self.item_code=item_code
		self.item_name=item_name
		self.price=price
	
	def get_price(self):
		return self.price


### 注文クラス
class Order:
	def __init__(self,item_master):
		self.item_order_list=[]
		self.item_master=item_master

	def add_item_order(self,item_code):
		for C_key_item in self.item_master:
			if C_key_item.item_code == item_code:
				self.item_order_list.append(item_code)
				return
		print("該当する商品がありません")
	
	def view_item_master(self):
		for item in self.item_master:
			print(f"［{item.item_code}:{item.item_name} {item.price}円］ ",end=" ")
		print("") #商品マスターを横一列で表示後のただの改行

	def view_item_list(self):        #注文リストを表示
		for item in self.item_order_list:
			print(f"商品コード:{item}",end="")

			#商品コードitemに該当する商品の値段をself.item_master[]から取得
			for C_key_item in self.item_master:
				if C_key_item.item_code == item:
					name_width = 10-get_zen_count(C_key_item.item_name)
					print(f" {C_key_item.item_name:{name_width}} {C_key_item.get_price()}円")
