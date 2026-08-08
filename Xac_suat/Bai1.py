#-----------------------------------------------------------------------------
# Các kết quả xảy ra: e1, e2, e3, e4, e5, e6                           
# Không gian mẫu:                               
# S = {e1, e2, e3, e4, e5, e6}                  

# Toàn bộ tập hợp S → Biến cố toàn phần
# Tập rỗng ∅ → Biến cố rỗng
# Mỗi phần tử riêng lẻ của S (ví dụ {e1}, {e2}, ...) → Biến cố cơ bản
# Ta có E ∩ O = ∅  → Biến cố xung khắc
#-----------------------------------------------------------------------------
# Không gian mẫu S = {(H, H), (H,T), (T,H), (T,T)}

#-----------------------------------------------------------------------------
# Định nghĩa xác suất                                           
# N   : Số phần tử của không gian mẫu S.                        
# NA  : Số phần tử của biến cố A (số kết quả thuận lợi cho A).  
#                                                               
# P(A) = NA / N                                                 
#                                                               
# P(A)= lim​ NA/N                                                 
#       N→∞                                                     
#-----------------------------------------------------------------------------
# VD: S={(1,1), (1,2), (1,3), ...,(6,6)}, N = 36        
# Xác suất xúc xắc hiển thị các số khác nhau            
# P = (36-6)/36 = 5/6                                   
                                                                                                               
# Xác suất tích 2 xúc xắc số lẻ                         
# Xúc xắc có các mặt 1,3,5 thì tích sẽ ra số lẻ         
# P = (3 * 3)/36 = 1/4                                          
                                                       
# Xác suất tích 2 xúc xắc số chẵn                       
# Chẵn * Chẵn: 3 * 3 = 9                                
# Lẻ * Chãn: 3 * 3 = 9                                  
# Chẵn * Lẻ: 3 * 3 = 9                                  
# P = 27/36 = 3/4                                       
#-----------------------------------------------------------------------------
# Đối với biến cố bất kỳ A, không gian mẫu S và biến cố rỗng ∅
# 0 <= P(A) <= 1
# P(S) = 1
# P(∅) = 0

# Cho các biến số sơ cấp e_i và các xác suất tương ứng p_i giá trị chuẩn hóa  
# p1 + p2 + ... + pN =1

# Cộng xác suất
# Biến cố bất kỳ: A, B 
# P(A∩B) = P(A) + P(B) - P(A∪B)

# VD
# Hộp 10 card, kết quả 1 -> 10
# Xác suất thẻ đc chọn là số chẵn or > 6
# A = {2,4,6,8,10}
# B = {7,8,9,10}
# P(A∩B) = P(A) + P(B) - P(A∪B)
# P(A∩B) = 50% + 40% - 20% = 70%

# Nếu A, B là xung khắc
# P(A∪B) = P(A) + P(B)

# Nếu A, B, C xung khắc
# P(A ∪ B ∪ C) = P(A) + P(B) + P(C)

# Biến cố đối
# Biến cố A, Biến cố đôi A^
# A ∪ A^c = S
# P(A) + P(A^c) = 1
# P(A) = 1 - P(A^c)

#Biến cố bù

# Tung 5 đồng xu, xác suất 1 mặt ngửa là bao nhiêu
# a) Nếu biến cố = "ít nhất 1 đồng xu mặt ngửa", biên cố bù:
# A^C = "Tất cả các dồng xu đều xấp"
# P(A^C) = 1/a^5 = 1/32

# b) Giữa biến cố này là biến cố bù ta có P(A) + P(A^c) = 1
# P(A) = 1 - P(A^c) = 1 - 1/32 = 31/32

#VD
# BÀi thi 5 câu hỏi, 4 đáp án(1 cái đúng)
# Khoang chung 1 đáp án, xác suất đúng ít nhất 1 cấu
# A^c = "Sai cả 5 câu"
# P(A^c) = (3/4)^5 = 243/1024
# P(A) = 1 - 243/1024 = 781/1024


# Xác suất có điều kiện 
# Biến cố A, B khác 0
# Xác suất đk biến cố B đối với biến A ký hiệu: P(B|A)

# P(B|A) = P(A∩B)/P(A)


# A, B phụ thuộc: P(A∩B) = P(A|B)P(B)=P(B|A)P(A)
# and P(A∩B) khác P(A)P(B)

# A, B độc lập: P(A∩B) = P(A)P(B)
# A, B xung khác: P(A∩B) = 0
# Định lý Bayes : P(A|B)P(B) = P(B|A)P(A)

# TRong hộp bút 10 cái, có 4 xanh, 6 đen
# Lấy lần lượt từng cái,ko trả lại vào hộp
# Xác suất để cả 2 cái đều xanh
# P(A∩B) = P(B|A)P(A) = 3/9 * 4/10 = 2/15 = 13.33%

# 50 hộp linh kiện, 1 hộp có 100% linh kiện tốt,những hộp còn lại 50%
# Lấy ngẫu nhiên 1 hộp, sau đó lấy  linh kiện
# Xác suất là hộp đb

# P(A|B) = (P(B|A).P(A))/(P(B|A).P(A) + P(B|A^c).P(A^c))
# P(A|B) = (1 * 1/50) / (1*1/50 + (1/2)^4 * 49/50)
# P(A|B) = 16/65 = 24.62%

