from fractions import Fraction


# Xác suất mô tả khả năng xảy ra của một biến cố trong không gian mẫu S.
# Với các kết quả đồng khả năng: P(A) = số kết quả thuận lợi / số kết quả có thể.


print('---------------- Không gian mẫu và biến cố ----------------')
die_outcomes = {1, 2, 3, 4, 5, 6}
coin_outcomes = {('H', 'H'), ('H', 'T'), ('T', 'H'), ('T', 'T')}

print('Không gian mẫu khi gieo một xúc xắc:', die_outcomes)
print('Không gian mẫu khi tung hai đồng xu:', coin_outcomes)
print('Biến cố toàn phần: S')
print('Biến cố rỗng: ∅')
print('Biến cố cơ bản: một kết quả riêng lẻ, ví dụ {1}')

print('---------------- Quy tắc cơ bản ----------------')
print('0 ≤ P(A) ≤ 1')
print('P(S) = 1 và P(∅) = 0')
print('P(A ∪ B) = P(A) + P(B) - P(A ∩ B)')
print('Nếu A và B xung khắc: P(A ∪ B) = P(A) + P(B)')
print('Biến cố bù: P(Aᶜ) = 1 - P(A)')

print('---------------- Ví dụ: hai xúc xắc ----------------')
total_outcomes = 6 * 6

# Hai mặt khác nhau: bỏ 6 trường hợp (1, 1), ..., (6, 6).
probability_different = Fraction(total_outcomes - 6, total_outcomes)
print(f'Xác suất hai mặt khác nhau: {probability_different}')

# Tích là số lẻ khi cả hai xúc xắc đều ra số lẻ.
probability_odd_product = Fraction(3 * 3, total_outcomes)
print(f'Xác suất tích là số lẻ: {probability_odd_product}')

# Tích là số chẵn là biến cố bù của “tích là số lẻ”.
probability_even_product = 1 - probability_odd_product
print(f'Xác suất tích là số chẵn: {probability_even_product}')

print('---------------- Ví dụ: quy tắc cộng ----------------')
# Chọn ngẫu nhiên một thẻ đánh số từ 1 đến 10.
even_numbers = {2, 4, 6, 8, 10}
greater_than_six = {7, 8, 9, 10}
union_numbers = even_numbers | greater_than_six

probability_union = Fraction(len(union_numbers), 10)
print('A = số chẵn:', even_numbers)
print('B = số lớn hơn 6:', greater_than_six)
print(f'P(A ∪ B) = {probability_union}')

print('---------------- Ví dụ: biến cố bù ----------------')
# Tung 5 đồng xu. A là biến cố có ít nhất một mặt ngửa.
probability_no_heads = Fraction(1, 2**5)
probability_at_least_one_head = 1 - probability_no_heads
print(f'P(có ít nhất một mặt ngửa) = {probability_at_least_one_head}')

# Làm bài trắc nghiệm 5 câu, mỗi câu có 4 đáp án và chọn ngẫu nhiên.
probability_all_wrong = Fraction(3, 4) ** 5
probability_at_least_one_correct = 1 - probability_all_wrong
print(f'P(đúng ít nhất một câu) = {probability_at_least_one_correct}')

print('---------------- Xác suất có điều kiện ----------------')
print('P(B | A) = P(A ∩ B) / P(A), với P(A) > 0')
print('Nếu A, B độc lập: P(A ∩ B) = P(A) × P(B)')
print('Công thức Bayes: P(A | B) = P(B | A) × P(A) / P(B)')

# Hộp có 4 bút xanh và 6 bút đen. Lấy hai bút không hoàn lại.
probability_two_blue = Fraction(4, 10) * Fraction(3, 9)
print(f'P(lấy được hai bút xanh) = {probability_two_blue}')

print('---------------- Ví dụ: định lý Bayes ----------------')
# Có 50 hộp linh kiện: 1 hộp toàn linh kiện tốt, 49 hộp còn lại có xác suất
# 1/2 cho mỗi linh kiện tốt. Chọn một hộp, rút được liên tiếp 4 linh kiện tốt.
probability_special_box = Fraction(1, 50)
probability_four_good_given_special = Fraction(1, 1)
probability_four_good_given_normal = Fraction(1, 2) ** 4

probability_four_good = (
    probability_four_good_given_special * probability_special_box
    + probability_four_good_given_normal * (1 - probability_special_box)
)
probability_special_given_four_good = (
    probability_four_good_given_special * probability_special_box
    / probability_four_good
)

print('P(hộp đặc biệt | rút được 4 linh kiện tốt) = '
      f'{probability_special_given_four_good}')
print(f'≈ {float(probability_special_given_four_good):.2%}')
