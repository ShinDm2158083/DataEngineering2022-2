#202158083 과제1

#러블리 러브시트 설명과 가격 저장
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white. "
lovely_loveseat_price = 254.00

#스타일리시 세티 설명과 가격
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black. "
stylish_settee_price = 180.50

#럭셔리 램프 설명과 가격
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade. "
luxurious_lamp_price = 52.15

#판매세 8.8%
sales_tax = .088

#첫 손님의 총 지불금액과 구매 아이템들 목록
customer_one_total = 0
customer_one_itemization = ""

#첫 손님이 러블리 러브시트와 럭셔리 램프 선택
customer_one_total+=lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
customer_one_total+=luxurious_lamp_price
customer_one_itemization+=luxurious_lamp_description

#판매세를 더해 최종 지불 금액 나옴
customer_one_tax = sales_tax * customer_one_total
customer_one_total+=customer_one_tax

#첫 손님이 구매한 물건들과 총 지불 금액 표시
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)