import fruits_menu
import csv

### csvファイルの読み込み
def set_item_master_csv(csv_file):
	with open(csv_file,encoding="utf_8",newline="") as items_csv:
		item_master = csv.reader(items_csv)
		
		# for文で、アイテム数分リストに.append
		L_items = []
		for item in item_master:
			L_items.append(fruits_menu.Item(item[0],item[1],item[2]))

	# 商品クラスの入ったリストを返す
	return L_items


### メイン処理
def main():
	# マスタ登録
	item_master = set_item_master_csv("item_master.csv")
	

	# オーダー登録
	order=fruits_menu.Order(item_master)
	order.add_item_order("001")
	order.add_item_order("002")
	order.add_item_order("003")
	
	while True:
		# オーダー一覧を表示
		print("\n---現在の注文状況---")
		order.view_item_list()

		while True:
			f_oder=input("注文を追加しますか？(y/n)")
			if f_oder == "n":
				break
			elif f_oder == "y":
				#注文できる商品を表示
				order.view_item_master()
				input_code = input("注文する商品のコードを入力して下さい:")
				input_code = input_code.zfill(3)
				order.add_item_order(input_code)
				break
			else:
				print("y か n を入力して下さい：")
				continue
		if f_oder == "n":
			break
	
	print("注文を受け付けました。")


if __name__ == "__main__":
	main()
